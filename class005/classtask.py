import random
result = 50
def check_random_number(result):
    random_number = random.randint(1,100)
    print(f"Generated random_number :{random_number}")

    if random_number>result:
        print(f"The random {random_number}")
        result = "Greater"
    else:
        print(f"The random number {random_number}")
        result = "Lesser or Equal"
    return result
check = check_random_number(result)
print(f"The result is {check}")
