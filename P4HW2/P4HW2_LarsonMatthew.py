# Matthew Larson

# 14 April 2024

# P4HW2

# This program calculates gross pay and total amount

#Initialize variables for totals
#Begin main loop
#Input employee's name or 'None' to terminate
#If employee name is 'None', exit loop
#Input hours worked
#Input pay rate
#If hours worked <= 40, calculate regular pay and set overtime pay to 0
#Else, calculate regular pay for 40 hours and overtime pay for additional hours
#Calculate gross pay as the sum of regular pay and overtime pay
#Update total employees, total regular pay, total overtime pay, and total gross pay
#Display employee details
#End main loop
#Display total number of employees entered
#Display total amount paid for overtime
#Display total amount paid for regular hours
#Display total amount paid in gross

total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
total_employees = 0
overtime_hours = 0

while True:
    employee_name = input("Enter employee's name or 'Done' to terminate: ")
    
    if employee_name.lower() == 'done':
        break
    
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
    
    if hours_worked <= 40:
        regular_pay = hours_worked * pay_rate
        overtime_pay = 0
    else:
        regular_pay = 40 * pay_rate
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
    
    gross_pay = regular_pay + overtime_pay
    
    total_employees += 1
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay
    
    print("Employee Name:\t", employee_name)
    print()
    print(f"{'Hours Worked':<13}  {'Pay Rate':<8}  {'Overtime':<10}  {'Overtime Pay':<13}  {'RegHour Pay':<11}  {'Gross Pay':<10}")
    print("-----------------------------------------------------------------------------------------")
    print(f"{hours_worked:<13.1f}  {pay_rate:<8.1f}  {overtime_hours:<10.1f}  {overtime_pay:<12.2f}   ${regular_pay:<11.2f} ${gross_pay:<9.2f}")

print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
