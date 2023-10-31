operations = []

a = int(input("a: "))
b = int(input("b: "))

while True:
    if a==b:
        print("True", operations[::-1])
        break
    elif b%2 == 0:
        if b<a:
            print("No")
            break
        b = b//2
        operations.append(b)
    else:
        if b<a:
            print("No")
            break
        b = (b - 1)//10
        operations.append(b)