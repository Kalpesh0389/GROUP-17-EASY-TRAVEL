import tkinter as tk
from tkinter import messagebox, ttk

class ReviewsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#E6E6FA")  # Lavender background
        self.controller = controller

        # In-memory storage for reviews
        self.reviews = []

        # Title Label
        tk.Label(self, text="🌟 Customer Reviews", font=("Arial", 18, "bold"), 
                 bg="#6A5ACD", fg="white", padx=20, pady=10).pack(fill="x")

        # Form Frame
        form_frame = tk.Frame(self, bg="#E6E6FA")
        form_frame.pack(pady=10)

        # Name Entry
        tk.Label(form_frame, text="👤 Name:", font=("Arial", 12), bg="#E6E6FA").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.name_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Place Entry
        tk.Label(form_frame, text="📍 Place:", font=("Arial", 12), bg="#E6E6FA").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.place_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        self.place_entry.grid(row=1, column=1, padx=5, pady=5)

        # Review Entry
        tk.Label(self, text="📝 Write your Review:", font=("Arial", 12), bg="#E6E6FA").pack()
        self.review_entry = tk.Text(self, height=5, width=50, font=("Arial", 12))
        self.review_entry.pack(pady=5)

        # Buttons Section
        button_frame = tk.Frame(self, bg="#E6E6FA")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="✅ Submit Review", font=("Arial", 12, "bold"), 
                  bg="#008000", fg="white", command=self.submit_review).grid(row=0, column=0, padx=5, pady=5)
        
        tk.Button(button_frame, text="📜 View All Reviews", font=("Arial", 12, "bold"), 
                  bg="#FFA500", fg="white", command=self.view_reviews).grid(row=0, column=1, padx=5, pady=5)

        # Dropdown for Place Selection
        tk.Label(self, text="🔍 Select Place to View Reviews:", font=("Arial", 12), bg="#E6E6FA").pack(pady=5)
        self.place_var = tk.StringVar()
        self.place_dropdown = ttk.Combobox(self, textvariable=self.place_var, state="readonly", 
                                           font=("Arial", 12), width=27)
        self.place_dropdown.pack(pady=5)
        self.update_place_dropdown()

        # Frame to hold "Show Reviews by Place" and "Back to Dashboard" buttons
        bottom_button_frame = tk.Frame(self, bg="#E6E6FA")
        bottom_button_frame.pack(pady=10)

        # Show Reviews by Place Button
        tk.Button(bottom_button_frame, text="📌 Show Reviews by Place", font=("Arial", 12, "bold"), 
                  bg="#4682B4", fg="white", command=self.view_reviews_by_place).grid(row=0, column=0, padx=5, pady=5)

        # Back to Dashboard Button (Placed to the right of "Show Reviews by Place")
        tk.Button(bottom_button_frame, text="⬅ Back to Dashboard", font=("Arial", 12, "bold"), 
                  bg="#8B0000", fg="white", padx=20, pady=10, 
                  command=lambda: controller.show_frame("DashboardPage")).grid(row=0, column=1, padx=5, pady=5)

        print("Back button added")  # Debugging check

    def update_place_dropdown(self):
        """Update the dropdown with unique places from the reviews."""
        places = sorted(set(review["place"] for review in self.reviews)) if self.reviews else []
        self.place_dropdown["values"] = places

    def submit_review(self):
        """Submit a new review and store it in memory."""
        name = self.name_entry.get().strip()
        place = self.place_entry.get().strip()
        review_text = self.review_entry.get("1.0", tk.END).strip()

        if name and place and review_text:
            # Add review to the in-memory list
            self.reviews.append({"name": name, "place": place, "review": review_text})
            
            messagebox.showinfo("Thank You!", "Your review has been submitted.")
            self.name_entry.delete(0, tk.END)
            self.place_entry.delete(0, tk.END)
            self.review_entry.delete("1.0", tk.END)
            self.update_place_dropdown()  # Update dropdown with new place
        else:
            messagebox.showwarning("⚠ Empty Fields", "Please enter name, place, and review before submitting.")

    def view_reviews(self):
        """Display all reviews in a message box with custom formatting."""
        if self.reviews:
            reviews_text = ""
            for review in self.reviews:
                reviews_text += (
                    f"📝 Name: {review['name']}\n"
                    f"🏙 City: {review['place']}\n"
                    f"💬 Review: {review['review']}\n\n"
                )
            messagebox.showinfo("📖 All Reviews", reviews_text.strip())  # Remove extra newline at the end
        else:
            messagebox.showinfo("📭 No Reviews", "No reviews yet.")

    def view_reviews_by_place(self):
        """Display reviews for the selected place in a message box."""
        selected_place = self.place_var.get()
        if selected_place:
            filtered_reviews = [review for review in self.reviews if review["place"] == selected_place]
            if filtered_reviews:
                reviews_text = "\n\n".join([f"👤 {review['name']}: 💬 {review['review']}" for review in filtered_reviews])
                messagebox.showinfo(f"📍 Reviews for {selected_place}", reviews_text)
            else:
                messagebox.showinfo("📭 No Reviews", f"No reviews for {selected_place} yet.")
        else:
            messagebox.showwarning("⚠ No Selection", "Please select a place to view reviews.")