num = int(input("Enter a number: "))

fact = 1

if num < 0:
    print("Factorial not possible")
else:
    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial =", fact)