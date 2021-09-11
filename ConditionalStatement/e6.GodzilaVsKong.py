budget = float(input())
statists_number = int(input())
price_clothes_statists = float(input())

decor_price = 0.1 * budget
if statists_number > 150:
    price_clothes_statists *= 0.9
statists_price = statists_number * price_clothes_statists
difference = budget - decor_price - statists_price
if difference < 0:
    print('Not enough money!')
    print(f'Wingard needs {-difference:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {difference:.2f} leva left.')

