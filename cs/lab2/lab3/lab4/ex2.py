# for i in range(4,0,-1):
#     print("*"*i)
# for i in range(0,4):
#     print(" "*i+"*"*4)
n = int(input("the value of n:"))
# for i in range(n):
#     print("-" * i + '*' + '+' * (n - i - 1))
    # if i == 0:
    #     print('*' + '+' * (n - 1) )
    # elif i == 1:
    #     print('-' + '*' + '+' * (n - 2))
    # elif i == 2:
    #     print('-' * (n - 2) + '*' + '+')
    # elif i == 3:
    #     print('-' * (n - 1) + '*')        

# for i in range(n):
#     if i == 0 or i == n - 1:
#         print('*' * n)  
#     else:
#         print('*' + ' ' * (n - 2) + '*')

# for i in range(n):
#     if i == 0 or i == n - 1:
#         print('*' + ' ' * (n - 2) + '*')
#     else:
#         print(' ' + '*' * (n - 2) + ' ')    
for i in range(n):
    print(' ' * i + '*' + " " * (n - i - 1) + "*" + ' ' * i)