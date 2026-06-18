print("Hello python")

# Store user text in variables using input()
name = input("Enter your name: ")
birth_year = input("Enter your birth year: ")

# Convert the text input into a whole number (integer)
age = 2026 - int(birth_year)

# Display a combined message using an f-string
print(f"Hello {name}! You will turn {age} years old this year.")