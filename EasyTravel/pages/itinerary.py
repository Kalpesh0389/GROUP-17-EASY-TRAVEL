import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class ItineraryPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#F0F8FF")
        self.controller = controller
        self.itineraries = []

        # Header
        tk.Label(self, text="Trip Itinerary Planner", font=("Arial", 20, "bold"), bg="#4682B4", fg="white", pady=10).pack(fill="x")

        form_frame = tk.Frame(self, bg="#F0F8FF")
        form_frame.pack(pady=20)

        # Day Selector
        tk.Label(form_frame, text="Day:", bg="#F0F8FF", font=("Arial", 12)).grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.day_var = tk.StringVar()
        self.day_selector = ttk.Combobox(form_frame, textvariable=self.day_var, state="readonly", width=10)
        self.day_selector['values'] = [f"Day {i+1}" for i in range(10)]
        self.day_selector.current(0)
        self.day_selector.grid(row=0, column=1, padx=5, pady=5)

        # Time
        tk.Label(form_frame, text="Time:", bg="#F0F8FF", font=("Arial", 12)).grid(row=0, column=2, sticky="e", padx=5, pady=5)
        self.time_entry = tk.Entry(form_frame, font=("Arial", 12), width=10)
        self.time_entry.grid(row=0, column=3, padx=5, pady=5)

        # Activity
        tk.Label(form_frame, text="Activity/Description:", bg="#F0F8FF", font=("Arial", 12)).grid(row=1, column=0, columnspan=2, sticky="e", padx=5, pady=5)
        self.activity_entry = tk.Entry(form_frame, font=("Arial", 12), width=40)
        self.activity_entry.grid(row=1, column=2, columnspan=2, padx=5, pady=5)

        # Add Button
        tk.Button(self, text="Add to Itinerary", command=self.add_itinerary, bg="#32CD32", fg="white",
                  font=("Arial", 12, "bold"), padx=10, pady=5).pack(pady=10)

        # Itinerary List
        self.itinerary_listbox = tk.Listbox(self, font=("Arial", 12), width=80, height=10, bg="white",
                                            fg="black", selectbackground="#4682B4", selectforeground="white")
        self.itinerary_listbox.pack(pady=10)

        # Action Buttons
        button_frame = tk.Frame(self, bg="#F0F8FF")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Remove Selected", command=self.remove_itinerary, bg="#FF4500", fg="white",
                  font=("Arial", 12, "bold"), padx=10, pady=5).grid(row=0, column=0, padx=10)

        tk.Button(button_frame, text="Back to Dashboard", command=lambda: controller.show_frame("DashboardPage"),
                  bg="#1E90FF", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5).grid(row=0, column=1, padx=10)

    def add_itinerary(self):
        day = self.day_var.get()
        time = self.time_entry.get().strip()
        activity = self.activity_entry.get().strip()

        if not time or not activity:
            messagebox.showwarning("Missing Info", "Please enter time and activity.")
            return

        item = f"{day} - {time} - {activity}"
        self.itinerary_listbox.insert(tk.END, item)

        # Optional: Store in a list (you could save to DB later)
        self.itineraries.append({
            "day": day,
            "time": time,
            "activity": activity
        })

        # Clear input
        self.time_entry.delete(0, tk.END)
        self.activity_entry.delete(0, tk.END)

        messagebox.showinfo("Added", "Itinerary item added successfully!")

    def remove_itinerary(self):
        selected = self.itinerary_listbox.curselection()
        if selected:
            index = selected[0]
            self.itinerary_listbox.delete(index)
            del self.itineraries[index]  # also remove from internal list
            messagebox.showinfo("Removed", "Itinerary item removed.")
        else:
            messagebox.showwarning("No Selection", "Please select an item to remove.")
