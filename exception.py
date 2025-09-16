try:
    n=int(input("Enter a value:" ))
    res=50/n
except ZeroDivisionError:
    print("u have given 0 as the value.it is division by zero error")
else:
    print(res)
finally:
    print("Good bye")