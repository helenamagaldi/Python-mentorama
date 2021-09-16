def fizz(var1):
    var1 = int(input("Please type a number bigger than 0: "))

    if var1 % 5 == 0 and var1  % 7 == 0:
        print("fizzbuzz")

    elif var1 % 7 == 0:
        print("buzz")

    elif var1 % 5 == 0:
        print("fizz")

    else:
        print("miss")

    return var1
