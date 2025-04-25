


def signup(self):
    """Validate and store user signup details."""
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

            # Insert user into the database
            cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", 
                           (name, email, password))
            
            conn.commit()
            conn.close()

            messagebox.showinfo("Signup Successful", "Account created successfully!")
            self.controller.show_frame("LoginPage")  # Redirect to login page

        except sqlite3.IntegrityError:
            messagebox.showerror("Signup Failed", "Email already exists.")

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
