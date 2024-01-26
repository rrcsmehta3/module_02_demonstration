

#SIMPLE DATA TYPES

# Variable for name
name = "Sapana"
print("Value: " + name + "  Type: ", type(name))

# Variable for Driver License Value
driver_license ="True"    
print("Value: " + driver_license + " Type: " , type(True))

# Variable for storing year
year = 2024
print("This year: " + str(year) + " Type: " , type(2024))

increment = 1
next_year = year + increment
print("Next year: " + str(next_year) + " Type: " , type(2025))

#CALCULATIONS
# Declared variable for canadian gst and manitoba pst
canadian_gst_rate = 0.05  
manitoba_pst_rate = 0.07  

# Declared variable for the price of the vehicle
vehicle_price = 82050.02

# Calculate the  tax value
federal_tax = vehicle_price * canadian_gst_rate
provincial_tax = vehicle_price * manitoba_pst_rate

# Calculate the total cost of the vehicle
total_cost = vehicle_price + federal_tax + provincial_tax

print("Pre-tax value: ", vehicle_price, "Provincial Tax:", provincial_tax, "Federal Tax: ", federal_tax, "Total: ", total_cost)

#  using f-string
print(f"Pre-tax value: ${vehicle_price:,.2f} Provincial Tax: ${provincial_tax:,.2f} Federal Tax: ${federal_tax:,.2f} Total: ${total_cost:,.2f}")


#LISTS

#TUPLES

#DICTIONARIES

#SETS

