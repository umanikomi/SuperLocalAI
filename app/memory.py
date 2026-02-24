import os
import sqlite3
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from .config import DB_PATH, INDEX_PATH, EMBED_MODEL, TOP_K

embedder = SentenceTransformer(EMBED_MODEL)
dimension = 384

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT,
    content TEXT
)
""")
conn.commit()

if os.path.exists(INDEX_PATH):
    index = faiss.read_index(INDEX_PATH)
else:
    index = faiss.IndexFlatL2(dimension)

def save_message(role, content):
    cur.execute("INSERT INTO messages (role, content) VALUES (?, ?)", (role, content))
    conn.commit()

    vector = embedder.encode([content]).astype("float32")
    index.add(vector)
    faiss.write_index(index, INDEX_PATH)

def retrieve_context(query):
    if index.ntotal == 0:
        return ""

    query_vec = embedder.encode([query]).astype("float32")
    D, I = index.search(query_vec, TOP_K)

    cur.execute("SELECT content FROM messages ORDER BY id ASC")
    rows = [r[0] for r in cur.fetchall()]

    context = []
    for idx in I[0]:
        if idx < len(rows):
            context.append(rows[idx])

    return "\n".join(context)
