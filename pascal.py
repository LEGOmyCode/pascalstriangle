from math import factorial

def max_num(one, two, three):
    highest_num = [one, two, three]
    return max(highest_num)

def multi_list(list):
    multiplied = 1
    for x in list:
        multiplied *= x
    return multiplied

def rev_string(reverse):
    return reverse[::-1]


def num_within(num, begin, end):
    if num in range(begin, end):
        return True
    else:
        return False


def pascal(triangle):
    for i in range(triangle):
        for j in range(triangle-i+1):
            print(end = ' ')
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)),end=' ')


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(max_num( 1, 100, 500))
print(multi_list(list))
print(rev_string('Raymond'))
num_within(3,2,4)
num_within(1,3,5)
pascal(5)