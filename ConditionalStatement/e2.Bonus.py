number = int(input())
bonus = 0
if number <= 100:
   bonus = 5
elif 100 < number <= 1000:
    bonus = 0.2 * number
elif 1000 < number:
    bonus = 0.1 * number
if number % 2 == 0:
    bonus = bonus +1
if number % 10 == 5:
    bonus = bonus + 2
print(f'{bonus}')
number_total = number + bonus
print(f'{number_total}')