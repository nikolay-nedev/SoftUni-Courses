record = float(input())
distance = float(input())
time_per_meter = float(input())
from math import floor
delay = floor(distance / 15) *  12.5
total_time = distance * time_per_meter + delay

if total_time >= record:
    print(f'No, he failed! He was {(total_time-record):.2f} seconds slower.')
else:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')