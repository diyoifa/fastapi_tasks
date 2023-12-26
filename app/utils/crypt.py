#funcion para encriptar una contraseña con bcrypt
import bcrypt

def encrypt_password(password):
    try:
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return password_hash
    except Exception as e:
        print(f"Error encrypting password: {e}")

#funcion para comparar una contraseña con bcrypt
def check_password(password:str, hashed:str):
    try:
        return bcrypt.checkpw(password.encode('utf-8'), hashed)
    except Exception as e:
        print(f"Error checking password: {e}")

