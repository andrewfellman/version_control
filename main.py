
def main():
    pick = None
    store_password = ""
    while pick != '3':

        print(f'\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
        pick = input('Please enter an option: ')

        if pick == '1':
            password = input('Please enter your password to encode: ')
            for num in password:
                num = int(num)
                num += 3
                num = str(num)
                store_password += num
            print('Your password has been encoded and stored!')


        if pick == '2':
            pass #FIXME implement decode function

if __name__ == "__main__":
    main()