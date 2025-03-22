def display_menu():
    print("\nWelcome to the Slam Book!")
    print("1. Add a new entry")
    print("2. View all entries")
    print("3. Remove an entry")
    print("4. Delete all entries")
    print("5. Search for an entry")
    print("6. Exit")

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

def remove_entry(slam_book):
    name = input("Enter the name of the entry you want to remove: ")
    if name in slam_book:
        del slam_book[name]
        print(f"Entry for {name} removed successfully!")
    else:
        print("No entry found with that name.")

def delete_all_entries(slam_book):
    confirm = input("Are you sure you want to delete all entries? (yes/no): ")
    if confirm.lower() == "yes":
        slam_book.clear()
        print("All entries have been deleted.")
    else:
        print("Operation canceled.")

def search_entry(slam_book):
    name = input("Enter the name you want to search for: ")
    if name in slam_book:
        print(f"\nName: {name}")
        for question, answer in slam_book[name].items():
            print(f"{question} {answer}")
    else:
        print("No entry found with that name.")

slam_book = {}
while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add_entry(slam_book)
    elif choice == "2":
        view_entries(slam_book)
    elif choice == "3":
        remove_entry(slam_book)
    elif choice == "4":
        delete_all_entries(slam_book)
    elif choice == "5":
        search_entry(slam_book)
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")