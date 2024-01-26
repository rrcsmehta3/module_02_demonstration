

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
number_list = [1,2,3,4,5,6,7,8,9,10]
print("Type of variable number_list: ", type(number_list))
print(number_list)

number_list.insert(5, "Sapana")
print(number_list)

number_list.remove(9)
print(number_list)

number_list_2 = ["A","B","C"]

number_list_3 = ["D","E","F",11,12]

print(number_list + number_list_2 + number_list_3)

#TUPLES
provinces = ('Quebec' , 'Alberta' , 'Manitoba' , 'Nunavut')
print("Type of variable provinces: ", type(provinces))

#DICTIONARIES
coins = {'nickel':0.05, 'dime':0.10, 'quarter':0.25 }
print(coins)
print("Type of variable coins: ",type(coins))
 
coins['nickel'] = 5  #Changing the value of key 'nickel'
coins[ 'dime' ] = 10 #Changing the value of key 'dime'
coins['quarter'] = 25  #Changing the value of key 'quarter'

print(coins)

coins['loonie'] = 100  #Adding a new key 'loonie' with a value 
coins['toonie'] = 200 #Adding a new key 'toonie' with a value 

print(coins)




#SETS
even_numbers = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
print(even_numbers)
print(type(even_numbers))

multiples_of_five = {5, 10, 15, 20}
print(multiples_of_five)

union = even_numbers.union(multiples_of_five)
print(union)

common_values = even_numbers.intersection(multiples_of_five)
print(common_values)

difference_first_set = even_numbers.difference(multiples_of_five)
print(difference_first_set)

difference_second_set = multiples_of_five.difference(even_numbers)
print(difference_second_set)




