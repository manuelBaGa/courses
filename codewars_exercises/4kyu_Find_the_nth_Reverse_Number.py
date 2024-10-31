'''
Reverse Number is a number which is the same when reversed.

For example, the first 20 Reverse Numbers are:

0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101

TASK:

You need to return the nth reverse number. (Assume that reverse numbers start from 0 as shown in the example.)

NOTES:

1 < n <= 100000000000
'''

def find_reverse_number(n):
    if n <= 10:
        return print(n-1)
    else:
        level=1
        upper_limit = '0'
        previous_limit = 0
        while n >  int(upper_limit):
            previous_limit = upper_limit
            if level%2 == 0:
                upper_limit = int('1'+'9'*(level//2))
            else:
                upper_limit = int('10'+'9'*(level//2))
            level+=1
    return (level-1, upper_limit, previous_limit)

test_number = 100000000000
a=find_reverse_number(test_number)
print(a[0],a[1], test_number,a[1]-test_number, test_number-a[2])