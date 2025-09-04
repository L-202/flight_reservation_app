import tkinter as tk
from database import init_db
from home import home_page
from booking import booking_page
from reservations import reservations_page
from edit_reservation import edit_reservation_page

# Initialize database
init_db()

# Function to switch pages
def show_page(page_function, *args):
    for widget in root.winfo_children():
        widget.destroy()
    page_function(root, show_page, *args)

# Main window
root = tk.Tk()
root.geometry("600x400")

# Start on Home page
show_page(home_page)

root.mainloop()
