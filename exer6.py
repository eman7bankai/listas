turno = str(input("Em qual turno você estuda:\nM-matutino\nV-vespertino\nN-noturno\n:"))
match turno.lower():
    case 'm':
        print("Bom dia")
    case 'v':
        print("Boa tarde")
    case 'n':
        print("Boa noite")   
    case _:
        print("invalido")     