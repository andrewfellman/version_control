def main():
    pick = None

    while pick != '3':

        print(f'Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
        pick = input('Please enter an option: ')

        if pick == '1':
            pass #FIXME implement incode function

        if pick == '2':#FIXME need stored password variable
            #print(f"The encoded password is {'stored pass'}, and the original password is {decode('stored pass')}")
            pass

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