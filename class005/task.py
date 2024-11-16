# def temp_func():
#     y = 20,
#     print('Inside function:',y)
# temp_func()
#print(y)


# import math
# print(math.sqrt(16))

# import datetime
# now = datetime.datetime.now()
# print('Current date and time:',now)


x = 20
def my_function():
    global x
    x = 30
    print("Inside function", x)
# my_function()
print("Outside function", x)
