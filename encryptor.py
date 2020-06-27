import random

result = ''
message = ''
choice = ''

print(' ')
print(' ______    _         ______    ______    _    _    ______    ______    ______    ______')
print('|  ____|  | \   ||  |  ____|  |  __  |  | |  | |  |  __  |  |__  __|  |  __  |  |  __  |')
print('| |____   ||\\  ||  | |       | |__| |  | |__| |  | |__| |     ||     | |  | |  | |__| |')
print('|  ____|  || \\ ||  | |       |  _  _|  |__  __|  |  ____|     ||     | |  | |  |  _  _|')
print('| |____   ||  \\||  | |____   | | ||       ||     | |          ||     | |__| |  | | ||')
print('|______|  ||   \_|  |______|  |_| ||       ||     |_|          ||     |______|  |_| ||')
print(' ')
print('www.x-industries.co.uk/slate-tech')

while choice != '-1':
    choice = input("\nDo you want to encrypt or decrypt a message?\nEnter 1 to Encrypt, 2 to Decrypt: ")

    if choice == '1':
        for x in range(10):
            cypher = random.randint(1,31)

        print("Your Key is ", cypher, "! (Note: Don't enter the exclamation mark)")
        
        message = input("\nEnter the message to encrypt: ")

        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) - cypher)

        print (result + '\n\n')
        result = ''

    elif choice == '2':
        key = input("Enter key: ")
        message = input("\nEnter the message to decrypt: ")

        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) + int(key))

        print (result + '\n\n')
        result = ''

    elif choice == 'no':
        print('Hey, you started this program; do not blame me for doing as you say!')

    else:
        print('Invalid choice, please try again')
