total=0
def sum(a,b=0):
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


n=sum(1000,3000)
print(total)
print("total outside the function:",total)

n=sum(2000,6000)
print(total)
print("total outside the function:",total)