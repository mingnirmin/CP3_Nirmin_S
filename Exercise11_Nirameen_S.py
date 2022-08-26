number = int(input("Input your number :"))
for a in range(number):
    print(" " * (number-a) + "*" * (int(a+1) + a))