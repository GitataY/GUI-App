print()
print('**UNIT CONVERTOR**')
print()

conversions_available = [(1, 'Temperature'),
                         (2, 'Speed')
                         ]

print('conversion available')
print()


for conversion_number, from_unit, to_unit in conversions_available:
    print(f'{conversion_number}) {from_unit} -> {to_unit}')

print()

conversion = input('Enterthe conversion number of the conversion to use --> ')
conversion_index = int(conversion) -1

conversion_number, from_unit, to_unit = conversions_available[conversion_index]