import datetime

class Expense: 
    """Expense entity with validated fields: id, description, amount, and date."""

    def __init__(self, id: int, description: str, amount: int, expense_date: datetime.date | None = None ):

        if not isinstance(description, str) or not description.strip():
            raise ValueError("Description must be a non-empty string.")
        
        if not isinstance(amount, int) or amount <= 0 :
            raise ValueError("Amount must be a positive integer.")
        
        if not isinstance(id, int) or isinstance(id, bool) or id <= 0:
            raise ValueError("Id must be a positive integer")
        
        if expense_date is not None and not isinstance(expense_date, datetime.date):
            raise ValueError("Date must be of type datetime.date or None")

        self.id = id
        self.description = description.strip()
        self.amount = amount
        self.date = expense_date or datetime.date.today()




