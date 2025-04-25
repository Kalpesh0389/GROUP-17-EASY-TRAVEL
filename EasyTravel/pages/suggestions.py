import tkinter as tk
from tkinter import ttk
import pandas as pd

class SuggestionsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#F0F8FF")
        self.controller = controller

        self.country_state_data = {
            "India": ["Maharashtra", "Goa", "Gujarat", "Karnataka", "Rajasthan"],
            "USA": ["California", "New York", "Texas", "Florida", "Illinois"],
            "Canada": ["Ontario", "British Columbia", "Quebec", "Alberta", "Manitoba"],
            "Australia": ["New South Wales", "Victoria", "Queensland", "Western Australia", "Tasmania"]
        }

        # Header
        tk.Label(self, text="Select Your Travel Preferences", font=("Arial", 18, "bold"), bg="#4682B4", fg="white").pack(fill="x")

        selection_frame = tk.Frame(self, bg="#F0F8FF")
        selection_frame.pack(pady=10)

        # Country Dropdown
        tk.Label(selection_frame, text="Country:", bg="#F0F8FF", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
        self.country_var = tk.StringVar()
        self.country_combo = ttk.Combobox(selection_frame, textvariable=self.country_var, values=list(self.country_state_data.keys()), state="readonly", font=("Arial", 12))
        self.country_combo.grid(row=0, column=1, padx=10, pady=5)
        self.country_combo.bind("<<ComboboxSelected>>", self.update_states)

        # State Dropdown
        tk.Label(selection_frame, text="State:", bg="#F0F8FF", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5)
        self.state_var = tk.StringVar()
        self.state_combo = ttk.Combobox(selection_frame, textvariable=self.state_var, state="readonly", font=("Arial", 12))
        self.state_combo.grid(row=1, column=1, padx=10, pady=5)

        # Preferences
        preferences = ["Ocean", "Forest", "Hills", "Desert", "Heritage"]
        self.preference_vars = []
        for i, pref in enumerate(preferences):
            tk.Label(selection_frame, text=f"{pref}:", bg="#F0F8FF", font=("Arial", 12)).grid(row=i+2, column=0, padx=10, pady=5, sticky="w")
            var = tk.StringVar(value="None")
            dropdown = ttk.Combobox(selection_frame, textvariable=var, values=["None", pref], state="readonly", font=("Arial", 12), width=15)
            dropdown.grid(row=i+2, column=1, padx=10, pady=5)
            self.preference_vars.append(var)

        # Buttons
        button_frame = tk.Frame(self, bg="#F0F8FF")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Get Suggestions", command=self.show_suggestions, bg="#32CD32", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="Back to Dashboard", command=lambda: controller.show_frame("DashboardPage"), bg="#DC143C", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10)

        # Results Box
        self.result_text = tk.StringVar()
        self.result_label = tk.Label(self, textvariable=self.result_text, justify="left", font=("Arial", 12), bg="white", fg="black", relief="solid", padx=10, pady=10, width=50, height=10)
        self.result_label.pack(pady=10)

    def update_states(self, event):
        country = self.country_var.get()
        states = self.country_state_data.get(country, [])
        self.state_combo['values'] = states
        self.state_var.set(states[0] if states else "")

    def get_suggestions(self, selected_prefs, selected_country, selected_state):
        try:
            df = pd.read_csv("places.csv")
            filtered_df = df[(df["Country"] == selected_country) & (df["State"] == selected_state)]
            for pref in selected_prefs:
                filtered_df = filtered_df[filtered_df[pref] == 1]
            return filtered_df["Place"].tolist()
        except Exception as e:
            return [f"Error loading data: {e}"]

    def show_suggestions(self):
        selected_prefs = [var.get() for var in self.preference_vars if var.get() != "None"]
        selected_country = self.country_var.get()
        selected_state = self.state_var.get()

        if not selected_country or not selected_state:
            self.result_text.set("Please select both country and state!")
        elif selected_prefs:
            suggestions = self.get_suggestions(selected_prefs, selected_country, selected_state)
            self.result_text.set("\n".join(suggestions) if suggestions else "No places found.")
        else:
            self.result_text.set("Please select at least one preference!")
