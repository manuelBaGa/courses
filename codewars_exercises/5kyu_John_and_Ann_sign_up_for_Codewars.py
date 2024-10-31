'''
John and his wife Ann have decided to go to Codewars. On the first day Ann will do one kata and John - he wants to know how it is working - 0 kata.

Let us call a(n) - and j(n) - the number of katas done by Ann - and John - at day n. We have a(0) = 1 and in the same manner j(0) = 0.

They have chosen the following rules:

On day n the number of katas done by Ann should be n minus the number of katas done by John at day t, t being equal to the number of katas done by Ann herself at day n - 1

On day n the number of katas done by John should be n minus the number of katas done by Ann at day t, t being equal to the number of katas done by John himself at day n - 1

Whoops! I think they need to lay out a little clearer exactly what there're getting themselves into!

Could you write:

functions ann(n) and john(n) that return the list of the number of katas Ann/John does on the first n days;
functions sum_ann(n) and sum_john(n) that return the total number of katas done by Ann/John on the first n days

Examples:

john(11)  -->  [0, 0, 1, 2, 2, 3, 4, 4, 5, 6, 6]
ann(6)    -->  [1, 1, 2, 2, 3, 3]

sum_john(75)  -->  1720
sum_ann(150)  -->  6930

Note:

Keep an eye on performance.
'''
import sys

john_days={0:0}
ann_days={0:1}
def john_katas_at_day(n):
    # your code
    if n == 0:
        return john_days[0]
    else:
        if n-1 in john_days.keys():
            return n - ann_katas_at_day(john_days[n-1])
        else:
            return n - ann_katas_at_day(john_katas_at_day(n-1))   

def ann_katas_at_day(n):
    if n == 0:
        return ann_days[0]
    else:
        if n-1 in ann_days.keys():
            return n - john_katas_at_day(ann_days[n-1])
        else:
            return n - john_katas_at_day(ann_katas_at_day(n-1))

def john(n):
    # your code
    if n in john_days.keys():
        return list(john_days.values()[0:n])
    else:
        for i in range(len(john_days),n):
            john_days[i]=john_katas_at_day(i)
        
        return list(john_days.values())

    
def ann(n):
    if n in ann_days.keys():
        return list(ann_days.values()[0:n])
    else:
        for i in range(len(ann_days),n):
            ann_days[i]=ann_katas_at_day(i)

        return list(ann_days.values())
    
    
def sum_john(n):
    # your code
    if n in john_days.keys():
        return sum(list(john_days.values())[0:n])
    else:
        return sum(john(n))
    
def sum_ann(n):
    # your code
    if n in ann_days.keys():
        return sum(list(ann_days.values())[0:n])
    else:
        return sum(ann(n))


print(sum_ann(int(sys.argv[1])))
print(ann_days)