x = int(input("Unesi iznos za x: "))

y = int(input("Unesi iznos za y: "))

operation = input("Izaberi matematicku operaciju  (+, -, *, /): ")

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    print(x / y)
else:
    print("Nije prepoznata matematicka operacija.")