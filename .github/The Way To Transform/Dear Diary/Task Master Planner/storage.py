from datetime import datetime
from typing import List, Dict, Optional
from models import Entry, User
from werkzeug.security import generate_password_hash, check_password_hash

class MemStorage:
    def __init__(self):
        self.entries: Dict[int, Entry] = {}
        self.users: Dict[int, User] = {}
        self.current_entry_id: int = 1
        self.current_user_id: int = 1

    def get_entries(self) -> List[Entry]:
        return list(self.entries.values())

    def get_entries_by_date(self, date: datetime, user_id: int) -> List[Entry]:
        target_date = date.date()
        return [
            entry for entry in self.entries.values()
            if entry.date.date() == target_date and entry.user_id == user_id
        ]

    def get_entries_by_user(self, user_id: int) -> List[Entry]:
        return [
            entry for entry in self.entries.values()
            if entry.user_id == user_id
        ]

    def create_entry(self, entry: Entry) -> Entry:
        entry.id = self.current_entry_id
        # Ensure we have a proper datetime object
        if isinstance(entry.date, str):
            entry.date = datetime.fromisoformat(entry.date)
        self.entries[self.current_entry_id] = entry
        self.current_entry_id += 1
        return entry

    def update_entry(self, entry_id: int, updates: dict) -> Entry:
        if entry_id not in self.entries:
            raise KeyError("Entry not found")

        entry = self.entries[entry_id]

        if 'title' in updates:
            entry.title = updates['title']
        if 'content' in updates:
            entry.content = updates['content']
        if 'type' in updates:
            entry.type = updates['type']
        if 'date' in updates:
            entry.date = datetime.fromisoformat(updates['date'])
        if 'completed' in updates:
            entry.completed = updates['completed']

        return entry

    def search_entries(self, query: str, user_id: int) -> List[Entry]:
        query = query.lower()
        return [
            entry for entry in self.entries.values()
            if (query in entry.title.lower() or query in entry.content.lower()) and
            entry.user_id == user_id
        ]

    def create_user(self, username: str, password: str) -> User:
        if self.get_user_by_username(username):
            raise ValueError("Username already exists")

        user = User(
            id=self.current_user_id,
            username=username,
            password=generate_password_hash(password)
        )
        self.users[self.current_user_id] = user
        self.current_user_id += 1
        return user

    def get_user(self, user_id: int) -> Optional[User]:
        return self.users.get(user_id)

    def get_user_by_username(self, username: str) -> Optional[User]:
        return next(
            (user for user in self.users.values() if user.username == username),
            None
        )

    def verify_user(self, username: str, password: str) -> Optional[User]:
        user = self.get_user_by_username(username)
        if user and check_password_hash(user.password, password):
            return user
        return None