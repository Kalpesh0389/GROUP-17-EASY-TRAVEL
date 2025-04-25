import tkinter as tk
from tkinter import messagebox
from db import connect_db
import hashlib

class SignupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#E8F0FE")

        tk.Label(self, text="Sign Up", font=("Helvetica", 24, "bold"), bg="#E8F0FE", fg="#1A73E8").pack(pady=20)
        tk.Label(self, text="Name:", font=("Helvetica", 12), bg="#E8F0FE", fg="#1A73E8").pack()
        self.name_entry = tk.Entry(self, font=("Helvetica", 12))
        self.name_entry.pack(pady=5)

        tk.Label(self, text="Email:", font=("Helvetica", 12), bg="#E8F0FE", fg="#1A73E8").pack()
        self.email_entry = tk.Entry(self, font=("Helvetica", 12))
        self.email_entry.pack(pady=5)

        tk.Label(self, text="Password:", font=("Helvetica", 12), bg="#E8F0FE", fg="#1A73E8").pack()
        self.password_entry = tk.Entry(self, show="*", font=("Helvetica", 12))
        self.password_entry.pack(pady=5)

        tk.Label(self, text="Confirm Password:", font=("Helvetica", 12), bg="#E8F0FE", fg="#1A73E8").pack()
        self.confirm_password_entry = tk.Entry(self, show="*", font=("Helvetica", 12))
        self.confirm_password_entry.pack(pady=5)

        tk.Button(self, text="Sign Up", font=("Helvetica", 12), bg="#34A853", fg="white",
                  command=self.signup).pack(pady=10)

        tk.Button(self, text="Back to Login", font=("Helvetica", 12), bg="#1A73E8", fg="white",
                  command=lambda: controller.show_frame("LoginPage")).pack(pady=5)

    def signup(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        confirm_password = self.confirm_password_entry.get().strip()

        if not name or not email or not password or not confirm_password:
            messagebox.showerror("Error", "All fields are required!")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        conn = connect_db()
        cursor = conn.cursor()

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        try:
            cursor.execute("INSERT INTO users (name, email, password_hash) VALUES (%s, %s, %s)",
                           (name, email, hashed_password))
            conn.commit()
            messagebox.showinfo("Success", "Account created successfully!")
            self.controller.show_frame("LoginPage")
        except Exception as e:
            messagebox.showerror("Error", f"Database error: {str(e)}")
        finally:
            cursor.close()
            conn.close()
