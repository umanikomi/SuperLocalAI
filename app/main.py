from .memory import save_message
from .llm import ask_llm

print("Super AI Started")
print("Type 'q' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "q":
        break

    answer = ask_llm(user_input)

    print("\nAI:", answer, "\n")

    save_message("user", user_input)
    save_message("assistant", answer)
