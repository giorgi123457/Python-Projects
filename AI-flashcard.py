import random
flashcard_data = {
    "python": [
        ("What does 'print' do?", "It outputs data to the console."),
        ("What is a list?", "A collection of ordered items."),
        ("What is a function?", "A reusable block of code."),
        ("What keyword starts a loop?", "'for' or 'while'."),
        ("What is a variable?", "A named storage for data.")],
        "math": [
            ("What is 2+2?", "4"),
            ("What is the derivative of x^2?", "2x"),
            ("What is pi approximately?", "3.14"),
            ("What is the square root of 16?", "4"),
            ("What is the integral of 1/x?", "ln|x| + C" ),
    

    ]
}

topic = input("Enter a topic (e.g., 'python', 'math'): ").lower()
if topic in flashcard_data:
    cards = flashcard_data[topic]
    random.shuffle(cards)
    print(f"\n Flashcards for '{topic.title()}':\n")
    for i, (q, a) in enumerate(cards, 1):
        input(f"{i}. Q: {q} \nPress Enter to see the answer...")
        print(f" A: {a}\n")
else:
    print("Sorry, nothing found. Try 'math or 'python'.")
