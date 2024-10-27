import random

# Lists of truths and dares
truths = [
    "What is your biggest secret?",
    "If you could change one thing about your life, what would it be?",
    "What is the most embarrassing thing you've ever done?",
    "Who is your crush?",
    "Have you ever cheated on a test?"
]

dares = [
    "Do 20 push-ups.",
    "Sing a song of your choice.",
    "Dance without music for 1 minute.",
    "Imitate your favorite celebrity.",
    "Let someone else style your hair."
]

def lie_detector(confidence):
    # Simple logic based on confidence
    if confidence.lower() in ['high', 'very high']:
        return "True"
    elif confidence.lower() in ['low', 'very low']:
        return "False"
    else:
        return random.choice(["True", "False"])

def play_game():
    print("Welcome to Truth or Dare!")
    while True:
        choice = input("Type 'truth' or 'dare' (or 'quit' to exit): ").strip().lower()

        if choice == 'truth':
            question = random.choice(truths)
            print("Truth: " + question)
            answer = input("Your answer: ")
            confidence = input("How confident are you in your answer? (high/medium/low): ")
            result = lie_detector(confidence)
            print(f"Lie Detector says: {result}!")

        elif choice == 'dare':
            print("Dare: " + random.choice(dares))

        elif choice == 'quit':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    play_game()
