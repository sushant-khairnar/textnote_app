import json                      # Used for JSON file operations
from note_manager.note import Note  # Import Note class

FILE_NAME = "notes.json"         # File to store notes data


# Save all notes to JSON file
def save_notes(notes):
    with open(FILE_NAME, "w") as file:
        # Convert Note objects to dictionaries before saving
        json.dump([note.save() for note in notes], file, indent=2)


# Load notes from JSON file
def load_notes():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

            # Convert dictionary data back to Note objects
            return [
                Note(
                    n["title"],
                    n["content"],
                    n["tags"],
                    n["timestamp"]
                )
                for n in data
            ]

    # Handle missing or corrupted file
    except (FileNotFoundError, json.JSONDecodeError):
        return []
