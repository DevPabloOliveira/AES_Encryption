from cryptography.fernet import Fernet

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        file_data = file.read()  # Lê os dados do arquivo em formato binário

    fernet = Fernet(key)  # Inicializa uma instância do algoritmo de criptografia com a chave fornecida
    encrypted_data = fernet.encrypt(file_data)  # Criptografa os dados do arquivo

    with open(file_path, 'wb') as file:
        file.write(encrypted_data)  # Escreve os dados criptografados de volta para o arquivo

# Exemplo de uso:
arquivo = 'red.png'  # Arquivo a ser criptografado teste com png
chave = Fernet.generate_key()  # Gera uma nova chave de criptografia
encrypt_file(arquivo, chave)  # Chama a função para criptografar o arquivo com a chave gerada
print(f"Hash AES do arquivo: {chave}")  # Imprime o valor da chave gerada (nesse caso, chamado de "Hash AES")
