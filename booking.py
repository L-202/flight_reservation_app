import tkinter as tk
from tkinter import messagebox
import sqlite3

def booking_page(root, show_page):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Book Flight - Flight Reservation App")

    tk.Label(root, text="Passenger Name").pack(pady=5)
    entry_name = tk.Entry(root, width=40)
    entry_name.pack()

    tk.Label(root, text="Flight Number").pack(pady=5)
    entry_flight = tk.Entry(root, width=40)
    entry_flight.pack()

    tk.Label(root, text="Departure").pack(pady=5)
    entry_departure = tk.Entry(root, width=40)
    entry_departure.pack()

    tk.Label(root, text="Destination").pack(pady=5)
    entry_destination = tk.Entry(root, width=40)
    entry_destination.pack()

    tk.Label(root, text="Date (YYYY-MM-DD)").pack(pady=5)
    entry_date = tk.Entry(root, width=40)
    entry_date.pack()

    tk.Label(root, text="Seat Number").pack(pady=5)
    entry_seat = tk.Entry(root, width=40)
    entry_seat.pack()

    def save_booking():
        name = entry_name.get()
        flight_number = entry_flight.get()
        departure = entry_departure.get()
        destination = entry_destination.get()
        date = entry_date.get()
        seat_number = entry_seat.get()

        if not all([name, flight_number, departure, destination, date, seat_number]):
            messagebox.showerror("Error", "All fields are required!")
            return

        conn = sqlite3.connect("flights.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, flight_number, departure, destination, date, seat_number))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Flight booked successfully!")

        entry_name.delete(0, tk.END)
        entry_flight.delete(0, tk.END)
        entry_departure.delete(0, tk.END)
        entry_destination.delete(0, tk.END)
        entry_date.delete(0, tk.END)
        entry_seat.delete(0, tk.END)

    tk.Button(root, text="Submit Booking", command=save_booking, bg="green", fg="white").pack(pady=20)

    # Back to Home
    from home import home_page
    tk.Button(root, text="⬅ Back to Home", command=lambda: show_page(home_page)).pack(pady=10)
