import pytest
from finance import Personal_Individual_Finance

def test_zero_state():
    """Test 1: Verifies that if $0 income and $0 expenses, the total tax, after tax income, net income are all $0, and no crashes occur."""
    pf = Personal_Individual_Finance()
    assert pf.calculate_total_tax() == 0.0 # If the income is zero, then the tax should also be zero.
    assert pf.calculate_after_tax_income() == 0.0 # If the income is zero, then the after-tax income should also be zero.
    assert pf.calculate_net_income() == 0.0 # If the income is zero, then the net income should also be zero.

def test_single_bracket_income():
    """Test 2: Verifies the income within the first tax bracket which is 10% for income up to $11,925."""
    pf = Personal_Individual_Finance()
    pf.income_streams = [11000] # Input of income that falls within the first tax bracket.
    assert pf.calculate_total_tax() == 1100.0 # 11,000 * 10% = 1,100
    assert pf.calculate_after_tax_income() == 9900.0 # 11,000 - 1,100 = 9,900
    assert pf.calculate_net_income() == 9900.0 # No expenses, so net income = after-tax income


def test_progressive_tax_spillover():
    """Test 3: Verifies that multiple tax brackets are correctly calculated when income progesses over into next brackets."""
    pf = Personal_Individual_Finance()
    pf.income_streams = [16000] # Input of income that spills over multiple tax brackets with no expenses.
    # Tax Calculation:
    # First tax bracket: 11,925 * 10% = 1,192.50
    # Second tax bracket: (16,000 - 11,925) * 12% = 4,075 * 0.12 = 489.00
    # Total tax => 1,192.50 + 489.00 = 1,681.50
    assert pf.calculate_total_tax() == 1681.50
    # After-tax income: 16,000 - 1,681.50 = 14,318.50
    assert pf.calculate_after_tax_income() == 14318.50
    # Net income with no expenses: 14,318.50
    assert pf.calculate_net_income() == 14318.50

def test_net_income_with_expenses():
    """Test 4: Verifies that net income is calculated correctly by subtracting total expenses from after-tax income."""
    pf = Personal_Individual_Finance()
    pf.income_streams = [10000] # 10,000 * 10% = 1,000 tax, so after-tax income is 9,000
    pf.expenses = [2000, 500, 150] # Total Expenses: 2000 + 500 + 150 = 2,650
    # Tax Calculation: 10,000 * 10% = 1,000
    assert pf.calculate_total_tax() == 1000.0
    # After-tax income: 10,000 - 1,000 = 9,000
    assert pf.calculate_after_tax_income() == 9000.0
    # Net income: 9,000 - 2,650 = 6,350
    assert pf.calculate_net_income() == 6350.0

def test_multiple_income_sources():
    """Test 5: Verifies that multiple income sources are correctly added before proceeding with tax calculations."""
    pf = Personal_Individual_Finance()
    pf.income_streams = [10000, 40000] # Total income before tax is 10,000 + 40,000 = 50,000
    # Tax Calculation:
    # First tax bracket: 11,925 * 10% = 1,192.50
    # Second tax bracket: (48,475 - 11,925) * 12% = 36,550 * 0.12 = 4,386.00
    # Third tax bracket: (50,000 - 48,475) * 22% = 1,525 * 0.22 = 335.50
    # Total tax => 1,192.50 + 4,386.00 + 335.50 = 5,914.00
    assert pf.calculate_total_tax() == 5914.0
    # After-tax income: 50,000 - 5,914.00 = 44,086.00
    assert pf.calculate_after_tax_income() == 44086.0
    # Net income with no expenses: 44,086.00
    assert pf.calculate_net_income() == 44086.0

def test_high_income():
    """Test 6: Verifies that high income is taxed correctly across all brackets without issues."""
    pf = Personal_Individual_Finance()
    pf.income_streams = [700000, 2500, 500, 3500, 5000] # Total income: 700,000 + 2,500 + 500 + 3,500 + 5,000 = 711,500
    pf.expenses = [60000, 15000, 4000] # Total Expenses: 60,000 + 15,000 + 4,000 = 79,000
    # Tax Calculation:
    # Bracket 1: 11,925 * 10% = 1,192.50
    # Bracket 2: (48,475 - 11,925) * 12% = 36,550 * 0.12 = 4,386.00
    # Bracket 3: (103,350 - 48,475) * 22% = 54,875 * 0.22 = 12,072.50
    # Bracket 4: (197,300 - 103,350) * 24% = 93,950 * 0.24 = 22,548.00
    # Bracket 5: (250,525 - 197,300) * 32% = 53,225 * 0.32 = 17,032.00
    # Bracket 6: (626,350 - 250,525) * 35% = 375,825 * 0.35 = 131,538.75
    # Bracket 7: (711,500 - 626,350) * 37% = 85,150 * 0.37 = 31,505.50
    
    assert pf.calculate_total_tax() == 220275.25
    # Total tax: 1,192.50 + 4,386.00 + 12,072.50 + 22,548.00 + 17,032.00 + 131,538.75 + 31,505.50 = 220,275.25
    assert pf.calculate_after_tax_income() == 491224.75
    # After-tax income: 711,500 - 220,275.25 = 491,224.75
    assert pf.calculate_net_income() == 412224.75
    # Net income: 491,224.75 - 79,000 = 412,224.75

def test_error_handling_negative_income():
    """Test 7: It should verifies for negative income, if there is it should trigger the error"""
    pf = Personal_Individual_Finance()
    pf.income_streams = [-1000]  # Negative income is unrealistic and should show an error.
    with pytest.raises(ValueError, match="Cannot be negative"): # If the income in negative it will triger the error message.
        pf.calculate_total_tax()

def test_error_handling_negative_expenses():
    """Test 8: It should verifies for negative expenses, if there is it should trigger the error"""
    pf = Personal_Individual_Finance()
    pf.income_streams = [10000] # Input of income streams
    pf.expenses = [-500]  # Negative expenses is unrealistic because we are spending and it should show an error.
    with pytest.raises(ValueError, match="Cannot be negative"): # If the expenses in negative it will triger the error message.
        pf.calculate_net_income()

def test_error_handling_invalid_income_type():
    """Test 9: If the input values of income is not a number, it should trigger the error."""
    pf = Personal_Individual_Finance()
    pf.income_streams = ["invalid"]  # Anything beside number will be invalid
    with pytest.raises(ValueError, match="Must be a number"):  # There may be an error in the future, if the input value is non-numeric, it will triger the error.
        pf.calculate_total_tax()

def test_error_handling_invalid_expense_type():
    """Test 10: If the input values of expenses is not a number, it should trigger the error."""
    pf = Personal_Individual_Finance()
    pf.income_streams = [10000]
    pf.expenses = ["invalid"]  # Anything beside number will be invalid
    with pytest.raises(ValueError, match="Must be a number"): # There may be an error in the future, if the input value is non-numeric, it will triger the error.
        pf.calculate_net_income()
