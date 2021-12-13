exp = [2500, 3000, 4200, 3500, 5000]
total=0
for i in range(len(exp)):
      print('Month:', (i+1), 'Expense:', exp[i])
      total= total + exp[i]

print('my total expense :', total)