import os; os.system('cls')

#HEADER
print('PLATESPOTTING')
print('-' * 12)

#INITIALIZE
plates = 1
while plates <= 999:

#INPUT VALIDATION
    try:
        plate = input('> ').upper()
        if len(plate) != 6:
            raise ValueError
        if not (plate[0:3].isalpha() and plate[3:6].isdigit()):
            raise ValueError
    except ValueError:
        print('WRONG FORMAT: ABC123')
        continue
    
#PLATE CHECKING
    number = int(plate[3:6])
    if number == plates:
        print('PLATES FOUND:', plates, '\n', plate, '\n', '-' * 12)
        plates += 1
    else:
        print('WRONG PLATE', plate, '\nEXPECTED:', f'***{plates:03d}', '\n', '-' * 12)

#COMPLETION
print('ALL PLATES FOUND!')