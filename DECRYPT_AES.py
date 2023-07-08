from cryptography.fernet import Fernet

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()  # Lê os dados criptografados do arquivo em formato binário

    fernet = Fernet(key)  # Inicializa uma instância do algoritmo de criptografia com a chave fornecida
    decrypted_data = fernet.decrypt(encrypted_data)  # Descriptografa os dados do arquivo

    with open(file_path, 'wb') as file:
        file.write(decrypted_data)  # Escreve os dados descriptografados de volta para o arquivo

# Exemplo de uso:
arquivo = 'red.png'  # Arquivo a ser descriptografado teste com png
chave = b't1C9F8ZzPb6xm0CDLYc7MSpZq7wMR8RCinxZ09GLBrA='  # Substitua pela chave usada para criptografar o arquivo essa chave de red.png
decrypt_file(arquivo, chave)  # Chama a função para descriptografar o arquivo com a chave fornecida
