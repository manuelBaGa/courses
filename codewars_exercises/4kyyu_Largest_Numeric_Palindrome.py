'''
Create a function that finds the largest palindromic number made from the product of at least 2 of the given arguments.

Notes
Only non-negative numbers will be given in the argument
You don't need to use all the digits of the products
Single digit numbers are considered palindromes
Optimization is needed: dealing with ones and zeros in a smart way will help a lot
Examples
[937, 113] --> 81518
As 937 * 113 = 105881 and the largest palindromic number that can be arranged from the digits of result is: 81518

Another one:

[57, 62, 23] --> 82128

             product     palindrome
57 * 62      = 3534   -->  353
57 * 23      = 1311   -->  131
62 * 23      = 1426   -->  6
57 * 62 * 23 = 81282  -->  82128
One more:

[15, 125, 8] --> 8

             product     palindrome
15 * 125     = 1875   -->  8
15 * 8       = 120    -->  2
125 * 8      = 1000   -->  1
15 * 125 * 8 = 15000  -->  5

TESTS:
test.assert_equals(numeric_palindrome(937,113),81518)
test.assert_equals(numeric_palindrome(657,892),484)
test.assert_equals(numeric_palindrome(48,9,3,67),868)

'''
from itertools import combinations


def get_sub_arg_product(args):
    index=2
    comb=[]
    while index <= len(args):
        sub_comb=combinations(set(args), r = index)
        for combination in set(sub_comb):
            product_result = 1
            if sum(combination) == len(combination):
                product_result = 1
            else:
                for number in combination:
                    product_result *= number
            comb.append(product_result)
        index+=1
    if args.count(1) > 1:
        comb.append(1)

    return comb

def find_palindrome(test_number):
    str_number = str(test_number)
    middle_number=''
    palindrome=''
    for number in sorted(set(str_number),reverse=True):
        if str_number.count(number)>1:
            palindrome+=number*int(str_number.count(number)/2)
            if str_number.count(number)%2==1 and number>middle_number:
                middle_number = number
        elif number>middle_number:
            middle_number=number

    return int(palindrome+middle_number+palindrome[::-1]) if palindrome != '0' else int(middle_number)


def get_max_palindrome(sub_products_list):
    max_palindrome = 0
    for number in sub_products:
        palindrome_num=find_palindrome(number)
        if palindrome_num > max_palindrome:
            max_palindrome=palindrome_num

    return print(max_palindrome)

args = [274, 17, 9773, 3016, 5, 9, 6, 849, 2, 6085]

sub_products=get_sub_arg_product(args)
get_max_palindrome(sub_products)
'''

'''