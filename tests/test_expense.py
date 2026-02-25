from expensetracker.domain.models import Expense
import pytest


def test_creating_valid_expense():
    expense = Expense(1, "food", 20)

    assert expense.id == 1
    assert expense.description == "food"
    assert expense.amount == 20

def test_empty_description_raises_error():
    with pytest.raises(ValueError):
         Expense(1,"",20)

def test_negative_amount_raises_value_error():
    with pytest.raises(ValueError):
         Expense(1, "h", -20)

def test_amount_must_be_int():
    with pytest.raises(ValueError):
        Expense(1, "h", "2")
        

