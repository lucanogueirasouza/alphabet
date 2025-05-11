print (
    "ALFABETO NOMEADO EM MAISCULAS E MINUSCULAS"
)

lista_maisculas = []
lista_minusculas = []

while True:
    try:  
        escolha = int(input(
            "[1] - Adicionar\n[2] - Mostrar lista maiscula\n[3] - Mostrar lista minuscula\n[4] - Remover letra\n[5] - Sair\nEscolha: "
        ))


    except (NameError , ValueError): 
        print (
            "ESCOLHA UMA OPÇÃO VÁLIDA"
        )
        continue

    if escolha == 1: 
        letra = str(input(
            "Digite a letra: "
        ))

        if letra == "": 
            print (
                "Utilize caracteres válidos"
            )
            continue

        if len(letra) > 1: 
            print (
                "PODE-SE APENAS 1 LETRA POR VEZ!"
            )
            continue

        if letra.isnumeric(): 
            print (
                "ACEITAMOS APENAS LETRAS!!"
            )
            continue

        if letra.islower(): 
            lista_minusculas.append(letra)
        else: 
            lista_maisculas.append(letra)

    elif escolha == 2: 
        print (*lista_maisculas, sep=", ")
    
    elif escolha == 3: 
        print (*lista_minusculas, sep=", ")

    elif escolha == 4: 
        escolha_retirar = int(input(
            "[1] - Lista maiscula\n[2] - Lista minuscula\nEscolha: "
        ))
        if escolha_retirar == 1: 
            indice_retirar_maiscula = int(input(
                "Digite o indice para retirar: "
            ))
            lista_maisculas.pop(indice_retirar_maiscula)
        else: 
            indice_retirar_minuscula = int(input(
                "Digite o indice para retirar: "
            ))
            lista_minusculas.pop(indice_retirar_minuscula)
    else: 
        break