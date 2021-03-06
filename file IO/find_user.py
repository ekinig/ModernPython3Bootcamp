'''
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''
from csv import DictReader


def find_user(first, last):

    with open('users.csv') as csvfile:
        reader = DictReader(csvfile)
        contador = 1
        for row in reader:
            if row['First Name'] == first and row['Last Name'] == last:
                return print(contador)
            contador += 1
        return print('{} {} not found.'.format(first, last))


find_user("Colt", "Steele")  # 1
find_user("Alan", "Turing")  # 3
find_user("Hola", "Here")  # 'Not Here not found.'
