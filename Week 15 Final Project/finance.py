class Personal_Individual_Finance:
    """Personal Individual Finance Calculator for 2025 tax brackets (single taxpayers)."""
    TAX_BRACKETS = [
        (11925, 0.10),   # Income between $0 up to $11,925, the tax rate is 10%
        (48475, 0.12),   # Income between $11,926 up to $48,475, the tax rate is 12%
        (103350, 0.22),  # Income between $48,476 up to $103,350, the tax rate is 22%
        (197300, 0.24),  # Income between $103,351 up to $197,300, the tax rate is 24%
        (250525, 0.32),  # Income between $197,301 up to $250,525, the tax rate is 32%
        (626350, 0.35),  # Income between $250,526 up to $626,350, the tax rate is 35%
        (float('inf'), 0.37) # Income $626,351 and up, the tax rate is 37%
    ]
    
    def __init__(self): 
        self.income_streams = []  # Store multiple sources of incomes
        self.expenses = []        # Store expenses
    


    """The input validation method before starting any calculations. It need to check if the numbes are integer or negative."""
    def _validate_values(self, values, value_type="value"):
         
        for val in values:
            if not isinstance(val, (int, float)) or isinstance(val, bool):   # Check the the input whether it was number, decimal or true/false
                raise ValueError(f"Invalid {value_type}: {val}. Must be a number.") # If the input is not a number, it will state error message with "Must be a Number"
            if val < 0:
                raise ValueError(f"Invalid {value_type}: {val}. Cannot be negative.") # If the input is in number but the values are negative, it will state error message with "Cannot be negative"   




    """Calculate total income from all sources."""         
    def calculate_gross_income(self):
    
        return sum(self.income_streams) # Adding all multiple sources types of incomes together




    """Calculate total tax based on the 2025 tax brackets."""
    def calculate_total_tax(self):
    
        try:
            self._validate_values(self.income_streams, "income") # Ensure all income is valid
        except ValueError as e:                                  # Error occurs during validation, it will state error message
            raise ValueError(f"Error validating income_streams: {e}") # Inform the user about the error in income_streams validation
        
        income_before_tax = sum(self.income_streams)  # Adding all multiple sources of incomes
        tax_total = 0                                 # Tax only applies to income earned, baseline starts at $0
        lower_limit = 0                               # The beginning path for tax brackets starts at $0
        
        """ Calculation for incomes that fall into specific category of tax brackets"""
        for upper_limit, rate in self.TAX_BRACKETS:   # Maximum income for bracket and tax rate
            if income_before_tax > lower_limit:
                taxable_income_in_bracket = min(income_before_tax, upper_limit) - lower_limit # All income within the bracket is taxable
                tax_total += taxable_income_in_bracket * rate  # Math logic to calculate the amount of tax for the income in the bracket
                lower_limit = upper_limit    # Update lower limit for next bracket to avoid duplicate calculations
            else:
                break              # If income is lower than lower limit, stop calculating
        return round(tax_total, 2) # Rounding total tax to 2 decimal places
    



    """Calculation for Income after tax, which is total income minus total tax."""
    def calculate_after_tax_income(self):
        return round(self.calculate_gross_income() - self.calculate_total_tax(), 2)
    



    """Calculation for Net Income, which is after tax income minus total expenses."""
    def calculate_net_income(self):
        try:
            self._validate_values(self.expenses, "expense")  # Ensure all expenses are valid
        except ValueError as e:                              # Error occurs during validation, it will state error message
            raise ValueError(f"Error validating expenses: {e}") # Inform the user about the error in expenses validation
        
        after_tax_income = self.calculate_after_tax_income()  # Total income after tax deduction
        total_expenses = sum(self.expenses)                   # Add up all expenses
        net_income = after_tax_income - total_expenses        # Subtract expenses from after-tax income
        return round(net_income, 2)                           # Net income rounded to 2 decimal places
    