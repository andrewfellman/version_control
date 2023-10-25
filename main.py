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
            print(f"The encoded password is {store_password}, and the original password is {decode(store_password)}")


def decode(password):
    """Decodes the password
    
    Arguements: password (string, the password to decode)
    Returns: string (the decoded password)"""

    password = str(password)
    decoded_password = []

    for char in password:
        decoded_password.append(str(abs(int(char) - 3)))

    return "".join(decoded_password)


if __name__ == "__main__":
    main()