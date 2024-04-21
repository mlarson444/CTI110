# Matthew Larson
# 21 April 2024
# P5LAB
# This program takes in a year and determines the number of days in February for that year.

def days_in_feb(user_year): 
    if user_year % 4 == 0 and user_year % 100 != 0:  
        return 29
    elif user_year % 400 == 0:                      
        return 29
    else:                                           
        return 28

if __name__ == '__main__':
    year = int(input("Enter year:"))
    feb_days = days_in_feb(year)
    print(f'{year} has {feb_days} days in February.')
