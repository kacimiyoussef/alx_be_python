# Prompt the user to input their monthly income and expenses
monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings
monthly_savings = monthly_income - total_monthly_expenses

# Display Monthly Savings
print(f"Your monthly savings are ${monthly_savings}.")

# Calculate Projected Savings for One Year with 5% interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Display Projected Savings after one year with interest
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
