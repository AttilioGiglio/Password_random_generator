import random
from string import ascii_letters

def password_generator():

    upper_case = ['A', 'B', 'C', 'D', 'E']
    lower_case = ['a', 'b', 'c', 'd', 'e']
    simbols = ['!', '#', '$', '&', '?']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9' '0']

    character = upper_case + lower_case + simbols + numbers

    password = []    

    for i in range(10) :
        character_random = random.choice(character)
        password.append(character_random)

    new_password = ''.join(password)
    
    return new_password

def run():
    secure_password = password_generator()
    print('your new password is: ' + secure_password)



if __name__ == '__main__':
    run()