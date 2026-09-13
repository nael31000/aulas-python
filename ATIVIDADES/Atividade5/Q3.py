turno=input("informe seu turno, M para matutino, V para Vespertino e N para Noturno")
match turno:
         case "M":
             print("Bom dia!")
         case "V":
             print("Boa tarde!")
         case "N":
             print("Boa noite!")
         case _:
             print("turno invalido")