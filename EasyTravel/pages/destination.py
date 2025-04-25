import tkinter as tk
from tkinter import ttk, messagebox

class DestinationFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f0f0f0")

        # Header Frame
        header_frame = tk.Frame(self, bg="#2c3e50")
        header_frame.pack(fill="x", pady=(0, 20))

        tk.Label(
            header_frame,
            text="Select Your Destination",
            font=("Arial", 16, "bold"),
            bg="#2c3e50",
            fg="white"
        ).pack(pady=10)

        # Main Content Frame
        content_frame = tk.Frame(self, bg="#f0f0f0")
        content_frame.pack(fill="both", expand=True, padx=50, pady=20)

        # Country Selection
        tk.Label(
            content_frame,
            text="Choose your country:",
            font=("Arial", 12),
            bg="#f0f0f0"
        ).pack(pady=(0, 10))

        self.countries = {
            "India": ["Maharashtra", "Goa", "Gujarat", "Karnataka", "Rajasthan"],
            "USA": ["California", "New York", "Texas", "Florida", "Illinois"],
            "Canada": ["Ontario", "British Columbia", "Quebec", "Alberta", "Manitoba"],
            "Australia": ["New South Wales", "Victoria", "Queensland", "Western Australia", "Tasmania"]
        }

        self.country_var = tk.StringVar()
        self.country_dropdown = ttk.Combobox(
            content_frame,
            textvariable=self.country_var,
            values=list(self.countries.keys()),
            state="readonly",
            font=("Arial", 11),
            width=30
        )
        self.country_dropdown.pack(pady=5)
        self.country_dropdown.bind("<<ComboboxSelected>>", self.update_states)

        # State Selection
        tk.Label(
            content_frame,
            text="Choose your state:",
            font=("Arial", 12),
            bg="#f0f0f0"
        ).pack(pady=(10, 10))

        self.state_var = tk.StringVar()
        self.state_dropdown = ttk.Combobox(
            content_frame,
            textvariable=self.state_var,
            state="readonly",
            font=("Arial", 11),
            width=30
        )
        self.state_dropdown.pack(pady=5)

        # Select Button
        select_btn = tk.Button(
            content_frame,
            text="Confirm Destination",
            command=self.select_destination,
            bg="#9b59b6",
            fg="white",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=8,
            relief="raised",
            borderwidth=2
        )
        select_btn.pack(pady=20)

        # Back Button
        back_btn = tk.Button(
            self,
            text="Back to Dashboard",
            command=lambda: controller.show_frame("DashboardPage"),
            bg="#7f8c8d",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=5
        )
        back_btn.pack(side="bottom", pady=10)

    def update_states(self, event=None):
        """Update state dropdown based on selected country"""
        selected_country = self.country_var.get()
        if selected_country in self.countries:
            self.state_dropdown["values"] = self.countries[selected_country]
            self.state_dropdown.current(0)  # Set first state as default
        else:
            self.state_dropdown["values"] = []

    def select_destination(self):
        """Handle destination selection"""
        selected_country = self.country_var.get()
        selected_state = self.state_var.get()

        if selected_country and selected_state:
            self.controller.current_destination = f"{selected_state}, {selected_country}"
            messagebox.showinfo(
                "Destination Selected",
                f"You've selected: {selected_state}, {selected_country}\nYou can now plan your trip!"
            )
            self.controller.show_frame("DashboardPage")
        else:
            messagebox.showwarning("No Selection", "Please select both a country and a state.")
