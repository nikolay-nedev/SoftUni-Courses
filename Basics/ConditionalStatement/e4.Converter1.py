number = float(input())
input_unit = str(input())
output_unit = str(input())
output_number = 0

if input_unit == "mm":
    if output_unit == "cm":
        output_number = number * 0.1
    elif output_unit == "m":
        output_number = number * 0.001
if input_unit == "m":
    if output_unit == "cm":
        output_number = number * 100
    elif output_unit == "mm":
        output_number = number * 1000
if input_unit == "cm":
    if output_unit == "mm":
        output_number = number * 10
    elif output_unit == "m":
        output_number = number * 0.01
print(f'{output_number:.3f}')

