def triangle(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("*", end="")
        print("\r")


n = eval(input("Enter value: "))
triangle(n)
