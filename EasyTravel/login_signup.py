import tkinter as tk
from tkinter import messagebox
import sqlite3


def initialize_db():
    """Create users table if it doesn't exist."""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()


# Call this function at the start of your program
initialize_db()


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#E8F0FE")  # Light blue background

        # Title
        tk.Label(self, text="Login", font=("Helvetica", 24, "bold"), bg="#E8F0FE", fg="#1A73E8").pack(pady=20)

        # Username Entry
        tk.Label(self, text="Email:", font=("Helvetica", 12), bg="#E8F0FE", fg="#1A73E8").pack()
        self.username_entry = tk.Entry(self, font=("Helvetica", 12))
        self.username_entry.pack(pady=5)

        # Password Entry
        tk.Label(self, text="Password:", font=("Helvetica", 12), bg="#E8F0FE", fg="#1A73E8").pack()
        self.password_entry = tk.Entry(self, show="*", font=("Helvetica", 12))
        self.password_entry.pack(pady=5)

        # Login Button
        tk.Button(self, text="Login", font=("Helvetica", 12), bg="#1A73E8", fg="white",
                  activebackground="#1967D2", activeforeground="white", relief="flat",
                  command=self.login).pack(pady=10)

        # Signup Button
        tk.Button(self, text="Sign Up", font=("Helvetica", 12), bg="#34A853", fg="white",
                  activebackground="#2D8C47", activeforeground="white", relief="flat",
                  command=lambda: controller.show_frame("SignupPage")).pack(pady=5)

    def login(self):
        """Validate login credentials from the database."""
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        # Check if user exists in the database
        cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            messagebox.showinfo("Login Successful", "Welcome!")
            self.controller.show_frame("DashboardPage")  # Redirect to main app
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")


class SignupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#E8F0FE")  # Light blue background

        # Title
        tk.Label(self, text="Sign Up", font=("Helvetica", 24, "bold"), bg="#E8F0FE", fg="#1A73E8").pack(pady=20)

        # Name Entry
        tk.Label(self, text="Name:", font=("Helvetica", 12), bg="#E8F0FE", fg="#1A73E8").pack()
        self.name_entry = tk.Entry(self, font=("Helvetica", 12))
        self.name_entry.pack(pady=5)

        # Email Entry
        tk.Label(self, text="Email:", font=("Helvetica", 12), bg="#E8F0FE", fg="#1A73E8").pack()
        self.email_entry = tk.Entry(self, font=("Helvetica", 12))
        self.email_entry.pack(pady=5)

        # Password Entry
        tk.Label(self, text="Password:", font=("Helvetica", 12), bg="#E8F0FE", fg="#1A73E8").pack()
        self.password_entry = tk.Entry(self, show="*", font=("Helvetica", 12))
        self.password_entry.pack(pady=5)

        # Confirm Password Entry
        tk.Label(self, text="Confirm Password:", font=("Helvetica", 12), bg="#E8F0FE", fg="#1A73E8").pack()
        self.confirm_password_entry = tk.Entry(self, show="*", font=("Helvetica", 12))
        self.confirm_password_entry.pack(pady=5)

        # Signup Button
        tk.Button(self, text="Sign Up", font=("Helvetica", 12), bg="#34A853", fg="white",
                  activebackground="#2D8C47", activeforeground="white", relief="flat",
                  command=self.signup).pack(pady=10)

        # Back to Login Button
        tk.Button(self, text="Back to Login", font=("Helvetica", 12), bg="#1A73E8", fg="white",
                  activebackground="#1967D2", activeforeground="white", relief="flat",
                  command=lambda: controller.show_frame("LoginPage")).pack(pady=5)

    def signup(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        confirm_password = self.confirm_password_entry.get().strip()

        if not name or not email or not password or not confirm_password:
            messagebox.showwarning("Empty Fields", "Please fill in all fields.")
        elif password != confirm_password:
            messagebox.showwarning("Password Mismatch", "Passwords do not match.")
        else:
            try:
                conn = sqlite3.connect("users.db")
                cursor = conn.cursor()
                cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", 
                               (name, email, password))
                conn.commit()
                conn.close()

                messagebox.showinfo("Signup Successful", "Account created successfully!")
                self.controller.show_frame("LoginPage")  # Redirect to login page

            except sqlite3.IntegrityError:
                messagebox.showerror("Signup Failed", "Email already exists.")