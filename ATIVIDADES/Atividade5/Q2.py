
letra=input("Digite uma letra: ")

match letra:
    case "a" | "e" | "i" | "u" |"o":
       print("Voce digitou uma vogal")
    case _:
       print("Não é uma vogal.")