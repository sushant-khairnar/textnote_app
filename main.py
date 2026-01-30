from note_manager import Note, save_notes, load_notes


# Display menu options
def show_menu():
    print("\n--- Note Manager ---")
    print("1. Add Note")
    print("2. View All Notes")
    print("3. Search Notes")
    print("4. Delete Note")
    print("5. Filter by Tag")
    print("6. Exit")


# Add a new note
def add_note(notes):
    title = input("Title: ").strip()
    content = input("Content: ").strip()
    tags = input("Tags (comma-separated): ").split(",")

    # Clean and store tags
    tags = [tag.strip() for tag in tags if tag.strip()]
    notes.append(Note(title, content, tags))
    save_notes(notes)  # Save to file
    print("Note added successfully.")


# View all notes
def view_notes(notes):
    if not notes:
        print("No notes available.")
        return

    # Display notes with numbering
    for i, note in enumerate(notes, start=1):
        print(f"\nNote #{i}")
        note.display()


# Search notes by keyword
def search_notes(notes):
    term = input("Enter search keyword: ")
    results = [note for note in notes if note.matches_search(term)]

    if not results:
        print("No matching notes found.")
        return

    for note in results:
        note.display()


# Delete a note by index
def delete_note(notes):
    view_notes(notes)
    if not notes:
        return

    try:
        index = int(input("Enter note number to delete: "))

        # Validate index
        if 1 <= index <= len(notes):
            notes.pop(index - 1)
            save_notes(notes)
            print("Note deleted.")
        else:
            print("Invalid note number.")

    except ValueError:
        print("Please enter a valid number.")


# Filter notes by tag
def filter_by_tag(notes):
    tag = input("Enter tag to filter: ").lower()

    # Match notes containing the given tag
    filtered = [note for note in notes if tag in [t.lower() for t in note.tags]]

    if not filtered:
        print("No notes found with that tag.")
        return

    for note in filtered:
        note.display()


# Main program loop
def main():
    notes = load_notes()  # Load notes from file

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_note(notes)
        elif choice == "2":
            view_notes(notes)
        elif choice == "3":
            search_notes(notes)
        elif choice == "4":
            delete_note(notes)
        elif choice == "5":
            filter_by_tag(notes)
        elif choice == "6":
            save_notes(notes)
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


# Program entry point
if __name__ == "__main__":
    main()
