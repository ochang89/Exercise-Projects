#password generator
import random

letters = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
numbers = '0123456789'
symbols = "!@#$%^&*?:;"

rand_list = []

'''
    Gets length of list passed through the function

    Parameters:
        random_list -> int:
            pass in a random_list to get the length
    
    Return:
        length -> int
            length random of list as int
'''

def string_length(random_string):
    length = len(random_string)-1
    return length

def randomize_list(a_list, b_list, c_list):
    
    list_of_lists = [a_list, b_list, c_list]

    for list in list_of_lists:
        index = random.randrange(0, len(list)+1)
        rand_list.append(random.choice(list))
        choice = random.choice(rand_list)
    return choice

def main():
    print("Welcome to the PyPassword Generator!")
    user_num = input("How many letters would you like in your password?\n")

    # random operations
    rand_num = random.randrange(0,10)
    rand_index_num = random.randrange(0, len(user_num)+1)

    # initialize pw_list and add first index for checks
    pw_list = []
    pw_list.append(randomize_list(letters, symbols, numbers))

    for i in range(0, int(user_num)-1):
        if pw_list[i] in pw_list:
            r = randomize_list(letters, symbols, numbers)
            pw_list.append(r)
        else:
            result = randomize_list(letters, symbols, numbers)
            pw_list.append(result)

    random.shuffle(pw_list)
    pw_string = ''.join(pw_list)
    print(pw_string)
    return pw_string
