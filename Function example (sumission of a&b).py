total=0
def sum(a,b):
    print("a:",a)
    print("b:",b)
    """summision of two values
    :param a:
    :param b:
    :return:
    """
    total=a+b
    print("total inside the function",total)
    return total


n=sum(6,5)
print(total)
print("total outside the function:",total)