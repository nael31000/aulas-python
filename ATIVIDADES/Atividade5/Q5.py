
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))


operador = input("Digite o operador (+, -, *, /): ")


match operador:
    case "+":
        print(num1, "+", num2, "=", num1 + num2)
    case "-":
        print(num1, "-", num2, "=", num1 - num2)
    case "*":
        print(num1, "*", num2, "=", num1 * num2)
    case "/":
        print(num1, "/", num2, "=", num1 / num2)
    case _:
        print("Operação inválida!")