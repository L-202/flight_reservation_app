import tkinter as tk
import sqlite3

def reservations_page(root, show_page):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Reservations - Flight Reservation App")

    tk.Label(root, text="All Reservations", font=("Arial", 16)).pack(pady=10)

    frame = tk.Frame(root)
    frame.pack(pady=10)

    headers = ["ID", "Name", "Flight", "Departure", "Destination", "Date", "Seat", "Actions"]
    for i, h in enumerate(headers):
        tk.Label(frame, text=h, borderwidth=1, relief="solid", width=12).grid(row=0, column=i)

    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations")
    rows = cursor.fetchall()
    conn.close()

    for r, row in enumerate(rows, start=1):
        for c, value in enumerate(row):
            tk.Label(frame, text=value, borderwidth=1, relief="solid", width=12).grid(row=r, column=c)

        from edit_reservation import edit_reservation_page
        tk.Button(frame, text="Edit", command=lambda rid=row[0]: show_page(edit_reservation_page, rid)).grid(row=r, column=len(row))

    if not rows:
        tk.Label(root, text="No reservations found.", fg="red").pack(pady=10)

    # Back to Home
    from home import home_page
    tk.Button(root, text="⬅ Back to Home", command=lambda: show_page(home_page)).pack(pady=20)
