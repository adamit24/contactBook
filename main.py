import time
names = []
phoneNumbers = []
num = 3

for i in range(num):
    name = input('Name: ').upper()
    phoneNumber = input('Phone Nunber: ')

    names.append(name)
    phoneNumbers.append(phoneNumber)

print('\nName: \t\t\tPhone Number: \n')

for i in range(num):
    print('{} \t\t\t{}'.format(names[i], phoneNumbers[i]))

searchName = input('\n What is the persons name?').upper()

print('Searching...')
time.sleep(3)

if searchName in names:
    index = names.index(searchName) # .index only returns the first instant of the value
    phoneNumber = phoneNumbers[index]
    print('Someone was found!')
    time.sleep(1)
    print('Name: {}, phone Number: {}'.format(searchName, phoneNumber))

else:
    print('Sorry, we couldn\'t find anyone by that name.')
