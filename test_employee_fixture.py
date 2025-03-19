import pytest
from employee import Employee

@pytest.fixture
def test_employee():
    """An instance of the Employee class for testing."""
    
    test_employee = Employee('John', 'Doe', 50000)
    return test_employee

def test_give_default_raise(test_employee):
    """Test that a default raise works correctly."""

    test_employee.give_raise()
    assert test_employee.salary == 55000

def test_give_custum_raise(test_employee):
    """Test that a custom raise works correctly."""
    
    test_employee.give_raise(10000)
    assert test_employee.salary == 60000