# This is a sample Python script.

# Press Mayús+F70 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

test_str=('abcxyzABCxyz 123',2,'cdezabCDEzab 123')
def caesar_cypher(string_2_encrypt,encryption_num,test_str):
    encrypted_str=''
    if str(encryption_num).isnumeric()==False or 0 > encryption_num > 25:
        print('please enter a valid number betwenn 1-25')
    for letter in string_2_encrypt:
        if letter == 'z':
            encrypted_str+='a'
        else:
            encrypted_str+=chr(ord(letter)+encryption_num)
    print(encrypted_str)
    print(test_str)
    assert encrypted_str==test_str


caesar_cypher('abcxyzABCxyz 123',2,'cdezabCDEzab 123')