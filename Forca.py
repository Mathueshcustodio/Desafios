import random

boneco = ["""----------
|.         |
|.         
|.        
|.         
|.        
""", """----------
|.         |
|.         @
|.        
|.         
|.        
""", """----------
|.         |
|.         @
|.        /|
|.         
|.        
""", """----------
|.         |
|.         @
|.        /|\\
|.         
|.        
""",  """----------
|.         |
|.         @
|.        /|\\
|.         |
|.        
""", """----------
|.         |
|.         @
|.        /|\\
|.         |
|.        / 
""", """----------
|.         |
|.         @
|.        /|\\
|.         |
|.        / \\
"""]

erros = 0
lista_palavras = ["carro", "arara", "moto", "batata", "cajueiro", "metarmofose", "nota"]
letras_erradas = []
letras_corretas = []
palavra_escolhida = random.choice(lista_palavras)


while True:
    print(boneco[erros])
    if erros == 6:
        print("VOCÊ PERDEU!")
        break
    elif ''.join(letras_corretas) == palavra_escolhida:
        print("VENCEU!")
        break

    print("Palavra: ", end='')
    for letra in palavra_escolhida:
        if letra in letras_corretas:
            print(letra, end='')
        else:
            print("_", end='')
    print("")

    letra = input("Digite uma letra: ").lower()

    if not letra.isalpha():
        print("Digite apenas letras!")
        continue

    if letra in letras_erradas or letra in letras_corretas:
        print("Esta letra já foi usada")
        continue

    if letra in palavra_escolhida:
        letras_corretas.append(letra)
    else:
        letras_erradas.append(letra)
        erros += 1
        print("ERROU!")