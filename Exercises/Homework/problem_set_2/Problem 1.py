# calculate_paint_volume computes the number of gallons of paint required
# calculate_labor_hours computes the hours of labor required
# calculate_paint_cost computes the cost of the paint
# calculate_labor_cost computes the labor charges
# total_cost computes the total cost of the paint job

def calculate_paint_volume(area):
	return area/112

def calculate_labor_hours(area):
	return (area/112)*8

def calculate_paint_cost(area, money):
	return calculate_paint_volume(area)*money

def calculate_labor_cost(area):
	return calculate_labor_hours(area)*35

def total_cost(area,money):
	return calculate_paint_cost(area, money) + calculate_labor_cost(area)

area = float(input('Please input the amount of area you want to paint:'))
paint_money = float(input('Please input the money for a gallen of paint:'))

print(calculate_paint_volume(area))
print(calculate_labor_hours(area))
print(calculate_paint_cost(area, paint_money))
print(calculate_labor_cost(area))
print(total_cost(area,paint_money))
