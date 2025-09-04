# ✈️ Flight Reservation Desktop App

A simple **Flight Reservation System** built with **Python, Tkinter, and SQLite**.
This project allows users to **book flights, view reservations, update, and delete them** using a desktop application.

---

## 📂 Project Structure

```
/flight_reservation_app
├── main.py              # Main application entry point
├── database.py          # SQLite database connection and setup
├── home.py              # Home page UI
├── booking.py           # Flight booking form
├── reservations.py      # View reservations list
├── edit_reservation.py  # Update/Delete reservations
├── flights.db           # SQLite database file (auto-created)
├── requirements.txt     # Required libraries
├── README.md            # Project documentation
└── .gitignore           # Git ignore file
```

---

## 🚀 Features

* **Home Page** → Navigate to Booking or Reservations
* **Book Flight** → Add new flight reservations
* **View Reservations** → Display all reservations in a table
* **Edit Reservation** → Update details of an existing booking
* **Delete Reservation** → Remove a booking from the database

---

## 🛠 Requirements

* Python 3.x
* Tkinter (comes pre-installed with Python; on Linux install via `sudo apt install python3-tk`)
* SQLite3 (built-in with Python)
* PyInstaller (for exporting to `.exe`)

Install dependencies (only PyInstaller is required via pip):

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App

In the project folder, run:

```bash
python main.py
```

---

## 💾 Export to EXE

To package into an executable (Windows):

```bash
pip install pyinstaller
pyinstaller --onefile main.py
```

The `.exe` will be created inside the `dist/` folder.

---

## 📷 Sample UI

* Home page with **Book Flight** and **View Reservations** buttons
* Booking form for adding new flights
* Reservation list with **Edit/Delete** options

---

## 📌 Author

**L-202** – Senior Computer Engineering student at Kafr El-Sheikh University  
[GitHub Profile](https://github.com/L-202)

