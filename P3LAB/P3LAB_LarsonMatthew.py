# Matthew Larson

# 17 March 2024

# P3LAB

# This program checks to see if conditions are met to print whether the input year is a leap year or not.

is_leap_year = False
   
input_year = int(input("Enter a year: "))

if input_year % 4 == 0:
    if input_year % 100 == 0:
        if input_year % 400 == 0:
            is_leap_year = True
    else:
        is_leap_year = True

if is_leap_year:
    print(f"{input_year} - leap year")
else:
    print(f"{input_year} - not a leap year")
