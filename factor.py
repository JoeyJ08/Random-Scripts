input_num = int(input("please put in a whole number "))
divide_num = 1
factor_tree = ''

while divide_num <= input_num:
    x = input_num % divide_num
    if x == 0:
        y = input_num / divide_num
        factor_tree = factor_tree + f'{divide_num} | {int(y)} \n'
    divide_num += 1

print(factor_tree)