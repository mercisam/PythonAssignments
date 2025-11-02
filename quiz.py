
def run_quiz():
    questions = [
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A. def", "B. function", "C. fun", "D. define"],
            "answer": "A"
        },
        {
            "question": "Which movie features the quote: 'I'll be back'?",
            "options": ["A. The Terminator", "B. Die Hard", "C. Rambo", "D. Predator"],
            "answer": "A"
        },
        {
            "question": "What is the correct file extension for Python files?",
            "options": ["A. .pt", "B. .py", "C. .pyt", "D. .pyn"],
            "answer": "B"
        },
        {
            "question": "In which movie does a clown named Pennywise appear?",
            "options": ["A. Joker", "B. It", "C. Saw", "D. Scream"],
            "answer": "B"
        },
        {
            "question": "Which of the following is a Python data type?",
            "options": ["A. integer", "B. string", "C. boolean", "D. All of the above"],
            "answer": "D"
        }
    ]

    score = 0

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.")

    print(f"\n🏁 Quiz Complete! You scored {score} out of {len(questions)}. 🏆")

# Main game loop
while True:
    run_quiz()
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! 👋")
        break
