import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet

# Generar o cargar una clave
def load_key():
    return open("secret.key", "rb").read()

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        original = file.read()
    
    encrypted = fernet.encrypt(original)

    with open(filename, "wb") as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as encrypted_file:
        encrypted = encrypted_file.read()
    
    decrypted = fernet.decrypt(encrypted)

    with open(filename, "wb") as decrypted_file:
        decrypted_file.write(decrypted)

# Funciones de GUI
def select_file():
    filename = filedialog.askopenfilename()
    if filename:
        file_label.config(text=filename)

def encrypt_action():
    filename = file_label.cget("text")
    if filename:
        encrypt_file(filename)
        messagebox.showinfo("Éxito", "Archivo cifrado exitosamente")

def decrypt_action():
    filename = file_label.cget("text")
    if filename:
        decrypt_file(filename)
        messagebox.showinfo("Éxito", "Archivo descifrado exitosamente")

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Cifrado de Archivos")

frame = tk.Frame(root)
frame.pack(pady=20)

file_label = tk.Label(frame, text="Selecciona un archivo", width=80)
file_label.pack(pady=10)

select_button = tk.Button(frame, text="Seleccionar Archivo", command=select_file)
select_button.pack(pady=10)

encrypt_button = tk.Button(frame, text="Cifrar Archivo", command=encrypt_action)
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(frame, text="Descifrar Archivo", command=decrypt_action)
decrypt_button.pack(pady=5)

# Generar una clave si no existe
try:
    load_key()
except FileNotFoundError:
    generate_key()

root.mainloop()
