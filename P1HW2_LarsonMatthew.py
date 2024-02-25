# Matthew Larson

# 25Feb2024

# P1HW2

# This assignment will help us understand the use of using input and output functions on a day to day basis with an example of using it for a travel budget.


print("This program calculates and displays travel expenses\n")


budget = float(input("Enter Budget: "))


destination = input("\nEnter your travel destination: ")


gas = float(input("\nHow much do you think you will spend on gas? "))


accomodation = float(input("\nApproximately, how much will you need for accomodation/hotel? "))


food = float(input("\nLast, how much do you need for food? "))

print("\n------------Travel Expenses------------")

print("Location:",destination)
print("Initial Budget:",budget)
print("\nFuel:",gas)
print("Accomodation:",accomodation)
print("Food",food)


balance = budget - gas - accomodation - food


print("\nRemaining Balance:",balance)
