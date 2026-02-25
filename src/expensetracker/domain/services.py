from expensetracker.domain.models import Expense
from expensetracker.data.repository import ExpenseRepository
import datetime


def add_expense(repo: ExpenseRepository, id: int, description: str, amount: int) -> None:

    """Create an Expense and persist it using the repository."""
    
    this_expense = Expense(id, description, amount)
    repo.add(this_expense)   
   

def update_expense(repo: ExpenseRepository, id: int, description: str, amount: int) -> bool:
    """
    Update an expense using the repository

    Returns:
            bool: True if the expense was updated, False otherwise.
    """
    this_expense = Expense(id, description, amount)
    updated = repo.update(this_expense)
    return updated
    

def delete_expense(repo: ExpenseRepository, id: int) -> bool:
    """
    Delete an expense using the repository

    Returns:
        bool: True if the expense was deleted, False otherwise.
    """
    deleted = repo.delete(id)
    return deleted
    

def get_expenses(repo: ExpenseRepository) -> list[Expense]:
    """
    Return all expenses using the repository.
    """
    expense_list = repo.fetch()
    return expense_list
    
def get_summary(repo: ExpenseRepository, month: int | None = None) -> int:
    """
    Sum expenses in the repository.
    If month is provided (1-12), sum only expenses from that month in the current year.
    """
    
    expense_list = repo.fetch()
    expense_summary = 0

    if len(expense_list) == 0:
        return 0
    else:
        if not month:
            for expense in expense_list:
                expense_summary += expense.amount
        else:
            for expense in expense_list:
                if expense.date.month == int(month) and expense.date.year == datetime.date.today().year:
                    expense_summary += expense.amount
        return expense_summary
    



    



