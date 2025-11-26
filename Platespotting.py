import os; os.system('cls')

#HEADER
print('PLATESPOTTING', '\n', '-' * 12)

found = 1

while found <= 999:
    plate = input('> ').upper()

#CHECK FORMAT
    if len(plate) == 6 and plate[0:3].isalpha() and plate[3:6].isdigit():
        number = int(plate[3:6])
#CHECK NUMBER
        if found == number:
            found += 1
            print('PLATE FOUND!:['+ plate +']', '\n', '-' * 12)
#WHY CHECK FAILED
        else:
            print('WRONG NUMBER!')
    else:
        print('WRONG FORMAT')

# FINISH
print('ALL PLATES FOUND!')