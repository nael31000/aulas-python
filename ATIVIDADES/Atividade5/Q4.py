mes=input("digite o numero correspondente a um mes")
match mes:
    case "12" | "1" | "2" :
        print("Verao")
    case  "3" | "4" | "5" :
        print("Outono")
    case "6" | "7" | "8" :
        print("Inverno")
    case "9" | "10" | "11" :
        print("Primaveira")
    case _:
        print("mes invalido")