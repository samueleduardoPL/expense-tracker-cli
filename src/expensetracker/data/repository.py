import json
from pathlib import Path
from expensetracker.domain.models import Expense
import datetime


class ExpenseRepository:
    """Repository for persisting and retrieving expenses from a JSON file.

    The file stores a JSON array of objects with keys: id, description, amount, date.
    """

    def __init__(self, path: Path):
        """Create a repository that uses the given file path as storage.

        Args:
            path: Path to the JSON file used for persistence.
        """
        self.path = path

    def ensure_file(self) -> None:
        """Ensure the data file exists, is non-empty, and contains valid JSON.

        If the file does not exist or is empty, it is initialized with an empty JSON list: [].

        Raises:
            ValueError: If the file contains invalid JSON (corrupted) or cannot be accessed
                due to permissions.
        """
        if not self.path.exists() or self.path.stat().st_size == 0:
            self.path.write_text("[]", encoding="utf-8")
        
        try:
            with open(self.path) as f:
                json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Your file {self.path} is corrupted") from e
        except PermissionError as e:
            raise ValueError(f"Permission denied when accesing data file {self.path}") from e

    def add(self, expense : Expense) -> None:
        """Persist a new expense to the JSON file.

        Args:
            expense: Expense entity to be stored.

        Raises:
            ValueError: If the data file is corrupted or cannot be accessed (via ensure_file()).
        """
        print("step5: DATA")

        expense_dict = {"id" : expense.id, 
                        "description": expense.description, 
                        "amount" : expense.amount, 
                        "date" : expense.date.isoformat()
                       }
        
        self.ensure_file()
        
        with open(self.path) as f:
            expense_list = json.load(f)
        
        expense_list.append(expense_dict)

        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(expense_list, f, indent=2)
    
    def update(self, expense : Expense) -> bool:
        """Update an existing expense in the JSON file.

        Matches by expense.id. If found, updates description and amount.

        Args:
            expense: Expense entity containing the id to match and new values.

        Returns:
            bool: True if an expense with the given id was found and updated, False otherwise.

        Raises:
            ValueError: If the data file is corrupted/cannot be accessed (via ensure_file()),
                or if an expense record is missing expected keys (invalid record format).
        """
        self.ensure_file()

        with open(self.path) as f:
            expense_list = json.load(f)
        
        updated = False
        for this_expense in expense_list:
            try:
                if this_expense["id"] == expense.id:
                    this_expense["amount"] = expense.amount
                    this_expense["description"] = expense.description
                    print("reached")
                    updated = True
                    print(updated)
                    break
            except KeyError as e:
                raise ValueError("Invalid expense record in data file.") from e
            
        with open(self.path, "w") as f:
            json.dump(expense_list, f, indent=2) 

        return updated     

    def delete(self, id):
        """Delete an expense by id from the JSON file.

        Args:
            id: The expense id to delete.

        Returns:
            bool: True if an expense with the given id was found and deleted, False otherwise.

        Raises:
            ValueError: If the data file is corrupted or cannot be accessed (via ensure_file()).
        """

        self.ensure_file()

        with open(self.path) as f:
            expense_list = json.load(f)
        
        for this_expense in expense_list:
            if this_expense["id"] == id:
                expense_list.remove(this_expense)
                deleted = True
                break
        else:
            deleted = False
        
        with open(self.path, "w") as f:
            json.dump(expense_list, f, indent=2)
        
        return deleted
    
    def fetch(self) -> list[Expense]:
        """Load all expenses from the JSON file as Expense entities.

        Returns:
            list[Expense]: A list of Expense objects built from the stored records.

        Raises:
            ValueError: If the data file is corrupted/cannot be accessed (via ensure_file()),
                or if a stored record is invalid (missing keys or invalid date format).
        """
        self.ensure_file()

        with open(self.path) as f:
            expenses_list = json.load(f)
        
        expenses = []
        try:
            for item in expenses_list:
                expense = Expense(item["id"],
                                  item["description"],
                                  item["amount"],
                                  datetime.date.fromisoformat(item["date"]))
                expenses.append(expense)
        except Exception as e:
            raise ValueError("Invalid expense record in data file.") from e

        return expenses




                







    


    
