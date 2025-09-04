import sqlite3

def init_db():
    # Connect (creates flights.db if it doesn't exist)
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()

    # Create reservations table if not exists
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reservations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        flight_number TEXT NOT NULL,
        departure TEXT NOT NULL,
        destination TEXT NOT NULL,
        date TEXT NOT NULL,
        seat_number TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("✅ Database initialized: flights.db created with reservations table.")
