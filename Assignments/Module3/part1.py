#constant
TIP_RATE=0.18
TAX_RATE=0.07

# input total number of meals
total_meal=int(input("Enter total number of meals: "))

# input meals
meals = {}

for meal in range(total_meal):
    meal_name = input("Enter meal name: ")
    meal_price = float(input("Enter meal price: "))
    meals[meal_name] = meal_price

# receipt header
print("\n" + "=" * 35)
print(f"          YOUR RECEIPT")
print("=" * 35)
print(f"{'Item':20}{'Price':>10}")
print("-" * 35)

# print meal items
for meal_name, meal_price in meals.items():
    print(f"{meal_name:20}{meal_price:>9.2f} $")

print("-" * 35)

# calculations
food_charge = sum(meals.values())
tip = food_charge * TIP_RATE
tax = food_charge * TAX_RATE
total_bill = food_charge + tip + tax

# summary section
print(f"{'Subtotal':20}{food_charge:>9.2f} $")
print(f"{'Tip (18 %)':20}{tip:>9.2f} $")
print(f"{'Tax (7 %)':20}{tax:>9.2f} $")
print("-" * 35)
print(f"{'TOTAL':20}{total_bill:>9.2f} $")
print("=" * 35)
print("     Thank you! Visit again   ")
print("=" * 35)