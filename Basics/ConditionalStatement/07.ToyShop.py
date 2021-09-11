puzzle = 2.60
talking_doll = 3
teddy_bear = 4.10
minion = 8.20
truck = 2

trip_price = float(input())
number_puzzles = int(input())
number_talking_dolls = int(input())
number_teddy_bears = int(input())
number_minions = int(input())
number_trucks = int(input())
total_cost = puzzle * number_puzzles + talking_doll * number_talking_dolls + teddy_bear * number_teddy_bears + minion * \
             number_minions + truck * number_trucks

if number_puzzles + number_talking_dolls + number_teddy_bears + number_minions + number_trucks > 50:
    total_cost *= 0.75

income = 0.9 * total_cost

if income >= trip_price:
    print(f'Yes! {(income - trip_price):.2f} lv left.')
else:
    print(f'Not enough money! {(trip_price - income):.2f} lv needed.')
