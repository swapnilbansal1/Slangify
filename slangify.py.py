import csv
import re

print("Time 2 speak some real language lads!")
print('===================================================')

def translator(user_string):
    user_string = user_string.split(" ")
    j = 0
    for i in user_string:
        name = "C:\\Users\\swapn_000\\Desktop\\sf.txt"
        mode = "r"
        with open(name, mode) as file:
            data = csv.reader(file, delimiter="=")
            i = re.sub('[^a-zA-Z0-9-_.]', '', i)
            for row in data:
                if i.casefold() == row[0].casefold():
                    user_string[j] = row[1].lower()
            file.close()
        j = j + 1
    print(' '.join(user_string))
    print('===================================================')
    print('')

while True:
    print("Provide Input below or print exit or EXIT to end script")
    user = input()
    if user.upper() == 'EXIT':
        print("Exiting Script")
        break
    translator(user)
