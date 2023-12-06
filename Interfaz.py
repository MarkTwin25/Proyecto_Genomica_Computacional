import tkinter as tk
from tkinter import messagebox, filedialog, messagebox
import PhiSpyModules
import subprocess


def buscar_fagos():
    ruta_archivo = filedialog.askopenfilename(filetypes=(("Archivos GenBank", "*.gb"),("Todos los archivos", "*.*")))
    if ruta_archivo:
        try:
            # Ejecuta PhiSpy.py con el archivo seleccionado
            resultado = subprocess.run(["PhiSpy.py", "-o","Streptococcus.phages", ruta_archivo], capture_output=True, text=True)
            print("proceso terminado")
            texto.insert(tk.END, resultado.stdout) # Imprime el resultado en la consola
            if resultado.stderr:
                texto.insert(tk.END, resultado.stderr)
        except Exception as e:
            messagebox.showinfo("Error", f"Error al buscar fagos: {e}")
window = tk.Tk()
window.title("Buscador de Fagos")
#window.iconbitmap("icono.ico")
window.geometry("700x500")

texto = tk.Text(window)
texto.pack()

boton_buscar = tk.Button(window, text="Buscar fagos", command=buscar_fagos)
boton_buscar.pack()

window.mainloop()