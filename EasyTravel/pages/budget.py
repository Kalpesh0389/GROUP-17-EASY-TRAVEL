import tkinter as tk
from tkinter import messagebox

class BudgetPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#F0F8FF")  # Light blue background
        self.controller = controller
        
        # In-memory storage for budget and expenses
        self.total_budget = 0
        self.expenses = []

        # Header
        tk.Label(self, text="Budget Tracker", font=("Arial", 18, "bold"), bg="#4682B4", fg="white", padx=20, pady=10).pack(fill="x")

        # Total Budget Section
        tk.Label(self, text="Enter Total Budget:", font=("Arial", 12), bg="#F0F8FF").pack(pady=(20, 5))
        self.budget_entry = tk.Entry(self, font=("Arial", 12), width=20)
        self.budget_entry.pack(pady=5)
        tk.Button(self, text="Set Budget", command=self.set_budget, bg="#32CD32", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5).pack(pady=5)

        # Expense Section
        tk.Label(self, text="Expense Name:", font=("Arial", 12), bg="#F0F8FF").pack(pady=(15, 5))
        self.expense_name_entry = tk.Entry(self, font=("Arial", 12), width=20)
        self.expense_name_entry.pack(pady=5)

        tk.Label(self, text="Amount Spent:", font=("Arial", 12), bg="#F0F8FF").pack(pady=(10, 5))
        self.amount_entry = tk.Entry(self, font=("Arial", 12), width=20)
        self.amount_entry.pack(pady=5)

        tk.Button(self, text="Add Expense", command=self.add_expense, bg="#FFA500", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5).pack(pady=10)

        # Buttons Section
        button_frame = tk.Frame(self, bg="#F0F8FF")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Show Budget Summary", command=self.show_summary, bg="#1E90FF", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5).grid(row=0, column=0, padx=10)

        tk.Button(button_frame, text="Back to Dashboard", command=lambda: controller.show_frame("DashboardPage"), bg="#DC143C", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5).grid(row=0, column=1, padx=10)

    def set_budget(self):
        """Set the total budget."""
        budget = self.budget_entry.get().strip()
        if budget.isdigit():
            self.total_budget = float(budget)
            self.budget_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"Budget set to ₹{self.total_budget}")
        else:
            messagebox.showwarning("Input Error", "Please enter a valid budget amount.")

    def add_expense(self):
        """Add a new expense."""
        expense_name = self.expense_name_entry.get().strip()
        amount = self.amount_entry.get().strip()

        if expense_name and amount.isdigit():
            self.expenses.append({"name": expense_name, "amount": float(amount)})
            self.expense_name_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"Expense '{expense_name}' of ₹{amount} added.")
        else:
            messagebox.showwarning("Input Error", "Please enter a valid expense name and amount.")

    def show_summary(self):
        """Display budget summary in a message box."""
        if self.total_budget == 0:
            messagebox.showwarning("No Budget", "Please set a budget first.")
            return

        total_expense = sum(expense["amount"] for expense in self.expenses)
        money_left = self.total_budget - total_expense

        # Prepare summary message
        summary = f"Total Budget: ₹{self.total_budget}\n"
        summary += f"Total Expenses: ₹{total_expense}\n"
        summary += f"Money Left: ₹{money_left}\n\n"
        summary += "Expenses:\n"
        for expense in self.expenses:
            summary += f"{expense['name']} - ₹{expense['amount']}\n"

        # Show summary in a message box
        messagebox.showinfo("Budget Summary", summary)
