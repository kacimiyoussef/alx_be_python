# finance_calculator.py

# Prompt user for input
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with a 5% interest rate
annual_savings = monthly_savings * 12  # total savings over 12 months
projected_savings = annual_savings + (annual_savings * 0.05)  # adding 5% interest

# Output the results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
