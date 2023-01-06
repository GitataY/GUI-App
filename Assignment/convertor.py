print()
print('**Unit Convertor**')
print()

conversions_available = ['(1 Temperature)',
                         '(2 Speed)']

def tempConversion(scale = None, source_temp= None):
    if scale == 'F':
        return 'C' , (source_temp - 32.0 ) * (5.0/9.0)
    elif scale == 'C':
        return 'F', (source_temp * (9.0/5.0)) + 32.0

def speedConversion(scale = None, source_speed = None):
    
    pass


print('What do you want to convert? ' + str(conversions_available))

input = input('Enter number of the conversion available : ')

if input == 1 :
    input = input ('Enter the temp number to convert: ')
    input = input ('Enter the current unit (C/F): ')

elif input == 2 : 
    input = input ('Enter the temp number to convert: ')
    input = input ('Enter the current unit (C/F): ')
     



