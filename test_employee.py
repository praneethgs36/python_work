from employee import Employee


def test_give_default_raise():
    """Test that a default raise works correctly."""
    
    test_employee = Employee('John', 'Doe', 50000)
    test_employee.give_raise()
    assert test_employee.salary == 55000


def test_give_custum_raise():
    """Test that a custom raise works correctly."""
    
    test_employee = Employee('John', 'Doe', 50000)
    test_employee.give_raise(10000)
    assert test_employee.salary == 60000