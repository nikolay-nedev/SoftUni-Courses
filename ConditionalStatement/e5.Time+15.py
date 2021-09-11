hours = int(input())
minutes = int(input())
new_minutes = minutes + 15
new_hours = hours

if new_minutes >= 60:
    new_minutes = minutes + 15 - 60
    new_hours = new_hours + 1
    if new_hours > 23:
        new_hours = new_hours - 24
elif new_minutes < 60:
    new_minutes = minutes + 15

if new_minutes < 10:
        print(f'{new_hours}:0{new_minutes}')
else:
    print(f'{new_hours}:{new_minutes}')