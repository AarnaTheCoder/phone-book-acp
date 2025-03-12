def display_menu():
    print("\nWelcome to the Slam Book!")
    print("1. Add a new entry")
    print("2. View all entries")
    print("3. Exit")

def add_entry(slam_book):
    name = input("Enter your name: ")
    answers = {}
    questions = [
        "What's your favorite color?",
        "What's your favorite food?",
        "What's a fun fact about you?",
        "What's your dream job?"
    ]
    for question in questions:
        answers[question] = input(question + " ")

    slam_book[name] = answers
    print("Entry added successfully!")

def view_entries(slam_book):
    if not slam_book:
        print("No entries found!")
    else:
        for name, answers in slam_book.items():
            print(f"\nName: {name}")
            for question, answer in answers.items():
                print(f"{question} {answer}")

slam_book = {}
while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add_entry(slam_book)
    elif choice == "2":
        view_entries(slam_book)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
