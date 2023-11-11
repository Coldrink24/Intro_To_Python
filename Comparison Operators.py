# Comparisons Operators

def max_num(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n3 and n2 >= n1:
        return n2
    else:
        return n3


print(max_num(879, 556, 6900))


def match(str1, str2):
    if str1 == str2:
        print("matchyy")
    else:
        print("Oh noo, Try again..")


match(input(), input())

print(3 > 4)
print(80 < 4)
print(5 == 4)
print(9 != 10)

