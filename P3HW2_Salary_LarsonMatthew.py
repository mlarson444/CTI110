# Matthew Larson
# 24 March 2024
# P3HW2
# This program helps calculate an employee's payroll based on the amount of time worked and pay rate of the employee followed by results.

# Pseudocode:
# Ask user for employee's name.
# Ask user for the number of hours worked by employee.
# Ask user for the pay rate of employee.
# Check if employee has worked overtime.
# Calculate overtime pay owed to employee.
# Calculate the pay for regular hours worked by employee.
# Calculate the gross pay (total amount to be paid to employee).
# Display a separator line.
# Display employee's name.
# Display the financial data in a formatted table.

employee_name = input("Enter employee's name: ")

hours_worked = float(input("Enter the number of hours worked: "))

pay_rate = float(input("Enter the employee's pay rate: "))

if hours_worked > 40:
    overtime_hours = hours_worked - 40
else:
    overtime_hours = 0

overtime_pay = overtime_hours * 1.5 * pay_rate

regular_pay = min(hours_worked, 40) * pay_rate

gross_pay = regular_pay + overtime_pay
print("---------------------------------------")

print("Employee Name:\t", employee_name)
print()
print(f"{'Hours Worked':<13}  {'Pay Rate':<8}  {'Overtime':<10}  {'Overtime Pay':<13}  {'RegHour Pay':<11}  {'Gross Pay':<10}")
print("-----------------------------------------------------------------------------------------")
print(f"{hours_worked:<13.1f}  {pay_rate:<8.1f}  {overtime_hours:<10.1f}  {overtime_pay:<12.2f}  ${regular_pay:<11.2f}  ${gross_pay:<9.2f}")
