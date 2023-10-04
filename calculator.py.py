def addition():
    first_value = int(input("Enter the first value: "))
    second_value = int(input("Enter the second value: "))
    result = first_value + second_value
    print(f'The result of {first_value} + {second_value} is: {result}')


def subtraction():
    first_value = int(input("Enter the first value: "))
    second_value = int(input("Enter the second value: "))
    result = first_value - second_value
    print(f'The result of {first_value} - {second_value} is: {result}')


def multiplication():
    first_value = int(input("Enter the first value: "))
    second_value = int(input("Enter the second value: "))
    result = first_value * second_value
    print(f'The result of {first_value} * {second_value} is: {result}')


def division():
    first_value = int(input("Enter the first value: "))
    second_value = int(input("Enter the second value: "))
    if second_value == 0:
        print("Cannot divide by zero.")
    else:
        result = first_value / second_value
        print(f'The result of {first_value} / {second_value} is: {result}')


user_choice = input("1 - for addition\n2 - for subtraction\n3 - for multiplication\n4 - for division: ")


if user_choice == "1":
    addition()
elif user_choice == "2":
    subtraction()
elif user_choice == "3":
    multiplication()
elif user_choice == "4":
    division()
else:
    print("Invalid choice.")
