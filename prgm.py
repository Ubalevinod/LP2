# Initialize the sum variable
total_sum = 0

# Loop through and ask the user to input 10 numbers
for i in range(10):
    number = float(input(f"Enter number {i+1}: "))  # Ask user for input and convert it to float
    total_sum += number  # Add the number to the sum

# Display the total sum
print(f"The total sum of the 10 numbers is: {total_sum}")
