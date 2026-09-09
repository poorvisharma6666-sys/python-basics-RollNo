#  Take a number as input from the user
n = int(input("Enter a number:"))

# Start factorial with 1
factorial = 1

# Multiply numbers from 1 to n
for i in range(1, n+1):
  factorial *=i

  # Display the final factorial
  print("Fcatorial =", factorial)
