from datetime import datetime  # Used to generate timestamps


class Note:
    # Constructor to initialize note details
    def __init__(self, title, content, tags, timestamp=None):
        self.title = title              # Note title
        self.content = content          # Note body/content
        self.tags = tags                # List of tags
        # Use current time if timestamp not provided
        self.timestamp = timestamp or datetime.now().isoformat()

    # Convert note object to dictionary (for file storage)
    def save(self):
        return {
            "title": self.title,
            "content": self.content,
            "tags": self.tags,
            "timestamp": self.timestamp
        }

    # Display note in readable format
    def display(self):
        print(f"Title: {self.title}")
        print(f"Timestamp: {self.timestamp}")
        print(f"Tags: {', '.join(self.tags)}")
        print(f"Content: {self.content}")
        print("-" * 30)

    # Check if note matches search term
    def matches_search(self, term):
        term = term.lower()
        return (
            term in self.title.lower()        # Match in title
            or term in self.content.lower()   # Match in content
            or any(term in tag.lower() for tag in self.tags)  # Match in tags
        )
