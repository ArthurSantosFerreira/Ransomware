import os

def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]

        # uper case
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        # lower case
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


ori_file = "original.txt"
back_file = "backup.txt"

if os.path.exists(ori_file):
    with open(ori_file, "r") as original_file:
        with open(back_file, "w") as backup_file:
            backup_file.write(original_file.read())

    s = 5
    with open(ori_file, "r+") as original_file:
        text = original_file.read()
        encrypted_text = encrypt(text, s)
        original_file.seek(0)
        original_file.write(encrypted_text)
        original_file.truncate()
    print(
        "Os seus dados foram encriptados. Para recupera-los, acesse: 'https://www.dcode.fr/caesar-cipher' e informe o tamanho da chave 's'"
    )
else:
    print(f"File {ori_file} não existe.")
