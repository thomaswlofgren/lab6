def encode(password):
    encoded_pas = ''
    for digit in password:
        digit = int(digit)
        if 0 <= digit <= 6:
            digit += 3
            encoded_pas += str(digit)
        elif digit == 7:
            digit = '0'
            encoded_pas += digit
        elif digit == 8:
            digit = '1'
            encoded_pas += digit
        elif digit == 9:
            digit = '2'
            encoded_pas += digit
    return encoded_pas

def main():
    password = input('Enter a password: ')
    print('Menu')
    print('1. Encode password')
    print('2. Decode password')
    print('3. Exit')
    print()
    option = int(input('Select a option: '))
    while True:
        if option == 1:
            password = encode(password)
            print(password)
            print()
        elif option == 2:
            pass
        #to be completed by partner
        elif option == 3:
            break
        else:
            print('Invalid Input')
        option = int(input('Select a option: '))





if __name__ == '__main__':
    main()


