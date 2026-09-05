
codigo=int(input("digite o codigo do produto de 1 a 4"))
match codigo:
   case 1 :
    print("cachorro quente no valor de R$ 10,00")
   case 2:
    print("hamburger a R$ 15,00")
   case 3:
    print("batata frita a R$ 8,00")
   case 4:
    print("refrigerante a R$ 5,00")
   case _:
    print("opcao invalida")