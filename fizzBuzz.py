number = 100
for n in range(1,number+1):
    if n % 3 == 0:
        if n % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)