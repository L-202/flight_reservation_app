import tkinter as tk

def home_page(root, show_page):
    root.title("Flight Reservation App")

    tk.Label(root, text="Welcome to Flight Reservation App", font=("Arial", 16)).pack(pady=20)

    # Navigate using show_page
    from booking import booking_page
    from reservations import reservations_page

    tk.Button(root, text="✈️ Book Flight", width=20, height=2,
              command=lambda: show_page(booking_page)).pack(pady=10)

    tk.Button(root, text="📋 View Reservations", width=20, height=2,
              command=lambda: show_page(reservations_page)).pack(pady=10)
