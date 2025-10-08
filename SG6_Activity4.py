full_name = input("Enter your full name (First Name, Middle Name, Last Name): ")

try:
    first_name, middle_name, last_name = [name.strip().capitalize() for name in full_name.split(",")]

    middle_initial = middle_name[0] + "."

    formatted_name = f"{last_name}, {first_name} {middle_initial}"

    print("Formatted Name:", formatted_name)

except ValueError:
    print("Invalid input format. Please enter your name as: First Name, Middle Name, Last Name")
