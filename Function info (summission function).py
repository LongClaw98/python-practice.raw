def Calculate_total(exp):
    """
    For adding each item in te list
    :param exp:
    :return:
    """
    total=0
    for item in exp:
        total=total+item
        return total

ram_exp_list=[3000,2000,4000]
sham_exp_list=[300,200,400]

rams_total_exp = Calculate_total(ram_exp_list)
shams_total_exp = Calculate_total(sham_exp_list)

print("Ram total exp:", rams_total_exp)
print("shams total exp",shams_total_exp)




