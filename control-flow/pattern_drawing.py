# pattern_drawing.py

# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a row counter for the while loop
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print the asterisks for each row
    for col in range(size):
        print("*", end="")
    
    # Print a new line after each row is printed
    print()
    
    # Increment the row counter
    row += 1