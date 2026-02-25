from expensetracker.ui.cli import run_cli
from expensetracker.ui.render import render_expenses
from expensetracker.ui.render import render_summary
from expensetracker.ui.render import render_add_success
from expensetracker.ui.render import render_update_success
from expensetracker.ui.render import render_delete_success
from expensetracker.ui.render import render_search_failure
from expensetracker.ui.render import render_error
from expensetracker.domain.services import add_expense
from expensetracker.domain.services import update_expense
from expensetracker.domain.services import delete_expense
from expensetracker.domain.services import get_summary
from expensetracker.domain.services import get_expenses
from expensetracker.domain.idgenerator import idgenerator
from expensetracker.data.repository import ExpenseRepository
from pathlib import Path
import calendar
import datetime


def run_app():
    """Orchestrate the UI, domain services, and repository.

    Parses CLI arguments, dispatches the requested command, renders output,
    and reports domain/data errors to the user.
    """
    print("step2 : APP")

    args = run_cli()
    repo = ExpenseRepository(Path("expenses.json"))

    match args.command:

        case "add":
            try:
                expenseid = idgenerator(Path("id.json"))
                add_expense(repo, expenseid, args.description, args.amount)
                render_add_success(expenseid)

            except ValueError as e:
                render_error(e)
        
        case "update":
            try:
                updated = update_expense(repo, args.id, args.description, args.amount)
                if updated:
                    render_update_success(args.id)
                else:
                    render_search_failure(args.id)

            except ValueError as e:
                render_error(e)

        case "delete":
            try:
                deleted = delete_expense(repo, args.id)
                if deleted:
                    render_delete_success(args.id)
                else:
                    render_search_failure(args.id)

            except ValueError as e:
                render_error(e)
        
        case "list":
            try:
                expenses = get_expenses(repo)
                render_expenses(expenses)
            
            except ValueError as e:
                render_error(e)

        case "summary":
            try:
                total_expenses = get_summary(repo, args.month)
                month_name = None
                if args.month is not None and isinstance(args.month, int):
                    if args.month > 12 or args.month < 1:
                        raise ValueError("Month must be an int between 1 and 12")
                    month_name = calendar.month_name[args.month]
                year = datetime.date.today().year
                render_summary(total_expenses, month_name, year)

            except ValueError as e:
                render_error(e)


    
    

    
    