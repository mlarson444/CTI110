# Matthew Larson

# 3Mar2024

# P2LAB1

# This program inputs gas mileage and cost of gas and outputs the gas cost for specific mileage.

m1 = 20
m2 = 75
m3 = 500
print("Input:")

gas_mileage = float(input())
cost = float(input())

your_value1 = (m1/gas_mileage)*cost
your_value2 = (m2/gas_mileage)*cost
your_value3 = (m3/gas_mileage)*cost

print("Output:")
print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f}')
