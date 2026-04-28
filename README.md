# Individual Taxpayers Financial Calculator

## What the code essentially do?

This Python tool was created to assist users in calculating net income, income before tax, tax total, total expenses, and total income. It provided users with tax brackets of 2025 according to the IRS website and it also calculated according to individual incomes.

---

## Implementation

### Prerequisites
- Python 3.8+
- pip

### Method for Setup

**Step 1: Procedures to Clone the Project**

```bash
git clone https://github.com/saygg-157/IS4010-Final-Project.git
```

**⚠️ Note:** The project will work normally if the user clone correctly and it will not have issue with the file path. 

**Step 2: Instalattion and Creation of Virtual Environment**

```bash
# How to activate and produce virtual environment
python -m venv venv
source venv/Scripts/activate   # GitBash for Window
# OR
source venv/bin/activate  # GitBash for macOS/Linux

# Dowload and configuration the files for your project
pip install pytest

# Evaluate the setup process
python -m pytest test_finance.py -v
```

---

## Usage

### Normal Example

```python
from finance import Personal_Individual_Finance

pf = Personal_Individual_Finance()
pf.income_streams = [50000, 15000]  # Multiple Income Sources
pf.expenses = [5000, 2000]          # Multiple Expenses

print(f"Gross Income: ${pf.calculate_gross_income():,.2f}")  
# Adding up all the sources of income
print(f"Total Tax: ${pf.calculate_total_tax():,.2f}")
# It show the total tax by calculating the income with each span of tax brackets
print(f"After-Tax Income: ${pf.calculate_after_tax_income():,.2f}")
# It show the income after minus the total tax 
print(f"Net Income: ${pf.calculate_net_income():,.2f}")
# It show the net income after excluded both expenses and taxes
```

### Run Tests

```bash
python -m pytest test_finance.py -v
```

Expected Output: All 10 tests pass ✅

---

## Examples

### Example 1: Part-Time Job
Student earning $12,000/year, no expenses

```python
pf = Personal_Individual_Finance()
pf.income_streams = [12000]
print(f"Tax: ${pf.calculate_total_tax():,.2f}")  # Result = $1,201.50
print(f"After-Tax Income: ${pf.calculate_after_tax_income():,.2f}") # Result = $10,798.5
```

### Example 2: Freelancer with Expenses
Freelancer: $50,000 salary + $25,000 side gig - $6,000 expenses

```python
pf = Personal_Individual_Finance()
pf.income_streams = [50000, 25000]
pf.expenses = [1000, 2500, 2500]
print(f"Net Income: ${pf.calculate_net_income():,.2f}")  
# Result = $57,586.00
```

### Example 3: High Income
Multiple streams ($711,500) with $80,000 expenses

```python
pf = Personal_Individual_Finance()
pf.income_streams = [700000, 2500, 500, 3500, 5000]
pf.expenses = [60000, 15000, 4000, 1000]
print(f"Net Income: ${pf.calculate_net_income():,.2f}")  
# Result = $411,224.75
```

---

## Single Taxpayers (2025) Tax Brackets 

| Bracket | Income Range        | Rate |
|---------|---------------------|------|
| 1       | $0 - $11,925        | 10% |
| 2       | $11,926 - $48,475   | 12% |
| 3       | $48,476 - $103,350  | 22% |
| 4       | $103,351 - $197,300 | 24% |
| 5       | $197,301 - $250,525 | 32% |
| 6       | $250,526 - $626,350 | 35% |
| 7       | $626,351+           | 37% |

---

## Unique Attributes

✅ Progressive tax bracket calculations  
✅ Multiple income streams  
✅ Multiple expenses  
✅ Verification of inputs (no negative numbers)  
✅ 10 wide-ranging tests  

---

## Recognized Restrictions

- Only applied to federal tax (no local, state, and FICA tax)
- Only applied to Single taxpayer 
- No listing, credits, or penalties
- Only for 2025 brackets (Update each year accordingly)

---

## Evaluation

All 10 tests pass:
- Zero state
- Single bracket income
- Progressive tax spillover
- Net income with expenses
- Multiple income sources
- High income 
- Addressing error for negative income
- Addressing error for negative expenses
- Addressing error for various types of incorrect income
- Addressing error for various types of incorrect expenses

Run: `python -m pytest test_finance.py -v`

---

## Project Files

```
├── AGENTS.md          # AI conversation records
├── finance.py         # Main calculator
├── README.md          # This file
├── requirement.txt    # Dependencies
└── test_finance.py    # 10 wide-ranging tests
```

---

## Author

**Name:** Geachkeang Say
**Course:** IS 4010  
**Date:** April 2026  
**Version:** 1.0
