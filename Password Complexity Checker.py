import tkinter as tk
import re

def calculate_strength(password):
    common_passwords = [
        '123456', 'password', '123456789', '12345678', '12345',
        '1234567', '1234567890', 'qwerty', 'abc123', 'password1',
        '111111', '123123', 'admin', 'letmein', 'welcome'
    ]

    strength = 0

    if password in common_passwords:
        return 0

    if len(password) > 8:
        strength += 1
    if len(password) >= 12:
        strength += 1

    if re.search(r'[A-Z]', password):
        strength += 1

    if re.search(r'[a-z]', password):
        strength += 1

    if re.search(r'[0-9]', password):
        strength += 1

    if re.search(r'[^A-Za-z0-9]', password):
        strength += 1

    return strength

def update_strength_meter(event):
    password = password_entry.get()

    strength = calculate_strength(password)
    strength_meter_label.config(text="")  # Clear the previous strength meter

    if strength <= 2:
        container.config(bg="red")
        strength_meter_label.config(text="Weak", fg="red")
    elif 2 < strength <= 4:
        container.config(bg="yellow")
        strength_meter_label.config(text="Moderate", fg="yellow")
    else:
        container.config(bg="green")
        strength_meter_label.config(text="Strong", fg="green")

def toggle_password():
    if password_entry.cget('show') == '*':
        password_entry.config(show='')
        show_button.config(text="Hide password")
    else:
        password_entry.config(show='*')
        show_button.config(text="Show password")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("400x300")
root.configure(bg="#282828")

# Crear contenedor
container = tk.Frame(root, bg="#383838", bd=5)
container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Crear entrada para contraseña
password_entry = tk.Entry(container, show="*", width=40, font=("Arial", 14), insertbackground="#ffffff", bg="#606060", fg="#ffffff")
password_entry.pack(pady=10)
password_entry.bind("<KeyRelease>", update_strength_meter)

# Botón para mostrar u ocultar contraseña
show_button = tk.Button(container, text="Show password", command=toggle_password, bg="#00bfff", fg="#ffffff", font=("Arial", 12), padx=10, pady=5)
show_button.pack(pady=10)

# Indicador de fortaleza
strength_meter_label = tk.Label(container, justify=tk.LEFT, font=("Arial", 14), bg="#383838", fg="#ffffff")
strength_meter_label.pack(pady=10)

# Iniciar bucle principal
root.mainloop()