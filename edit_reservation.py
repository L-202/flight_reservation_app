import tkinter as tk
from tkinter import messagebox
import sqlite3

def edit_reservation_page(root, show_page, reservation_id):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Edit Reservation - Flight Reservation App")

    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations WHERE id=?", (reservation_id,))
    reservation = cursor.fetchone()
    conn.close()

    if not reservation:
        messagebox.showerror("Error", "Reservation not found.")
        return

    labels = ["Passenger Name", "Flight Number", "Departure", "Destination", "Date (YYYY-MM-DD)", "Seat Number"]
    entries = []

    for i, label in enumerate(labels, start=1):
        tk.Label(root, text=label).pack(pady=5)
        entry = tk.Entry(root, width=40)
        entry.insert(0, reservation[i])
        entry.pack()
        entries.append(entry)

    def update_reservation():
        updated_values = [e.get() for e in entries]

        if not all(updated_values):
            messagebox.showerror("Error", "All fields are required!")
            return

        conn = sqlite3.connect("flights.db")
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE reservations
            SET name=?, flight_number=?, departure=?, destination=?, date=?, seat_number=?
            WHERE id=?
        """, (*updated_values, reservation_id))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Reservation updated successfully!")

    def delete_reservation():
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this reservation?")
        if confirm:
            conn = sqlite3.connect("flights.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM reservations WHERE id=?", (reservation_id,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Deleted", "Reservation deleted successfully!")
            from reservations import reservations_page
            show_page(reservations_page)

    tk.Button(root, text="Update Reservation", command=update_reservation, bg="blue", fg="white").pack(pady=10)
    tk.Button(root, text="Delete Reservation", command=delete_reservation, bg="red", fg="white").pack(pady=10)

    # Back to Reservations
    from reservations import reservations_page
    tk.Button(root, text="⬅ Back to Reservations", command=lambda: show_page(reservations_page)).pack(pady=10)
