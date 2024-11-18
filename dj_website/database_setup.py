import sqlite3

# Connect to SQLite database
connection = sqlite3.connect('database.db')

# Create messages table
with connection:
    connection.execute("""
        CREATE TABLE messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        );
    """)

print("Database setup complete!")
