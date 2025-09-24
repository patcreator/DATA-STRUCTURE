from array import array
print("-------Project 95: Car Rental Records-------\n\n\n")
print("TASK 1: Integers")
rent_costs = [10000, 89000, 32000, 56000, 23000, 67000, 33000, 56000, 34000]
rent_costs_total = sum(rent_costs)
rent_costs_average = rent_costs_total / len(rent_costs)
min_costs = min(rent_costs)
max_costs = max(rent_costs)
print('Output after work with integers type')
print("rent costs\n", rent_costs)
print('Total Rent Costs', rent_costs_total)
print('Average Rent Cost', rent_costs_average)
print('Minimum Rent Cost', min_costs)
print('Maximum Rent Cost', max_costs)
print("----- TASK 2: Strings -----")
print("Report for Car Rental Records that summarize totals and averages. ")
print(f"Total Rent Costs report:{rent_costs_total} and Average Rent Costs: {rent_costs_average}")

# task 3
print("----- TASK 3: Booleans -----")
print(f"threshold as 30,000 frw If the average exceeds the threshold 'Above Standard' will be printed else 'Below Standard' will be printed. and maximum must be exceeds 80,000 frw")
threshold = 30000
print(rent_costs_average >= threshold and max_costs >= 80000)

# task 4
print("----- TASK 4: Lists -----")

rent_days = [5 , 7, 14, 28, 29, 30, 31, 60]
print('list before add, remove element, sort', rent_days)
rent_days.append(21)
print('list after append 21 days', rent_days)
rent_days = [ day for day in rent_days if day <= 30 ]
print("list after removing all element above 30", rent_days)
rent_days.sort()
print("list after sorting all element", rent_days)

# task 5
print("----- TASK 5: Arrays -----")
rent_costs_in_array = array('i', rent_costs)
total_of_rent_costs_in_array = sum(rent_costs_in_array)
print('Rent costs in array ', rent_costs_in_array)
print('Rent costs in array sum ', total_of_rent_costs_in_array)
print('Sums comparision ', rent_costs_total == total_of_rent_costs_in_array)

# task 5
print("----- TASK 5: Dictionaries -----")
car_rental_recods = [
    {'id': 1, 'name':'TOYOTA', 'value':50320000},
    {'id': 2, 'name':'NISSAN', 'value':24046670},
    {'id': 3, 'name':'HONDA', 'value':62200000},
    {'id': 4, 'name':'MAZDA', 'value':79933320},
    {'id': 5, 'name':'MITSUBISHI', 'value':33000000},
    {'id': 5, 'name':'SUBARU', 'value':63139020},
    {'id': 7, 'name':'SUZUKI', 'value':24000000},
    {'id': 8, 'name':'ISUZU', 'value':57855420},
    {'id': 9, 'name':'DAIHATSU', 'value':32000000},
    {'id': 10, 'name':'HINO', 'value':56125670},
    {'id': 11, 'name':'LEXUS', 'value':175839400},
]
print("Dictionary:", car_rental_recods)

car_rental_recods[0] = {
    'id':0,'name':'V8','value':60000000
}
print("Dictionary After update index 0 element:", car_rental_recods)

del car_rental_recods[10]

print("Dictionary After deleting index 10 element:", car_rental_recods)

car_rental_recods_total = sum([rec['value'] for rec in car_rental_recods ])
print("Dictionary total from (value field):", car_rental_recods_total)
