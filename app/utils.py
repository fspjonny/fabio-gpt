import hashlib

# Função para calcular o hash de uma senha
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()
