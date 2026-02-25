from expensetracker.domain.models import Expense

def render_expenses(expenses: list[Expense]) -> None:
    """
    Print any given expenses in the cli

    Args:
        expenses: A list of expense objects
    """

    if not expenses:
        print("There are no expenses to print")
        return

    print(f"{'ID':<4}{'Date':<12}{'Description':<14}{'Amount':<4}")
    for expense in expenses:
        print(f"{expense.id:<4}{expense.date.isoformat():<12}{expense.description:<14}${expense.amount:<4,}")


def render_summary(summary: int, month: str | None = None, year: int | None = None) -> None:
    """
    Print a summary in the cli. If month and year are given as arguments, says it in the cli. 

    Args:
        summary: An int representing a sum of expenses
        month: A str representing the name of a month
        year: An int representing the current year
    """

    if month and year:
        print(f"Total expenses for {month} {year}: ${summary:,}")
    else:
        print(f"Total expenses: ${summary:,}")

def render_add_success(id: int) -> None:
    """
    Print a success message for adding an expense

    Args:
        id (int): The id of the added expense
    """
    print(f"Expense added successfully (ID: {id})") 

def render_update_success(id: int) -> None:
    """
    print a success message for updating an expense

    Args:
        id (int): The id of the updated expense
    """
    print(f"Expense updated successfully (ID: {id})") 

def render_delete_success(id: int) -> None:
    """
    print a success message for deleting an expense

    Args:
        id (int): The id of the deleted expense
    """
    print(f"Expense deleted successfully (ID: {id})")

def render_search_failure(id: int) -> None:
    """
    print an error message for failure to find an expense with a given id

    Args:
        id (int): The id of the expense
    """
    print(f"Could not find the expense with the id: {id}")

def render_error(error: Exception ) -> None:
    """
    print an error to the cli

    Args:
        error(Exception): Error to print
    """
    print(error)
    