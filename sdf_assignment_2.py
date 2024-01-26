

#SIMPLE DATA TYPES
name = "Sapana"
print("Value: " + name + "  Type: ", type(name))

license ="True"    
print("Value: " + license + " Type:" , type(True))

Year = "2024"
print("this year: " + Year+ " Type:" , type(2024))

Year = "2025"
print("next year: " +Year + " Type: " , type(2025))

#CALCULATIONS
Canadian_gst_rate = 0.05  
Mnaitoba_pst_rate = 0.07  

# Constant for the price of the vehicle
vehicle_price = 80000.0  

# Calculate the  tax value
federal_tax = vehicle_price * Canadian_gst_rate
provincial_tax = vehicle_price * Mnaitoba_pst_rate

# Calculate the Total cost of the vehicle
Total = vehicle_price + federal_tax + provincial_tax

print("Vehicle Price: ", vehicle_price, "\nFederal Tax: ", federal_tax, "\nProvincial Tax:", provincial_tax, "\nTotal: ", Total)


# Constants for tax rates
Canadian_gst_rate = 0.05  
Mnaitoba_pst_rate = 0.07 

# Constant for the price of the vehicle
vehicle_price = 70000.0  

# Calculate the  tax value
federal_tax = vehicle_price * Canadian_gst_rate
provincial_tax = vehicle_price * Mnaitoba_pst_rate

# Calculate the Total cost of the vehicle
Total = vehicle_price + federal_tax + provincial_tax

#  using f-string
print(f"Vehicle Price: ${vehicle_price}\nFederal Tax: ${federal_tax}\nProvincial Tax: ${provincial_tax}\nTotal: ${Total}")



#LISTS

#TUPLES

#DICTIONARIES

#SETS

