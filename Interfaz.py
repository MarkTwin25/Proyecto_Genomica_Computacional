import subprocess
import tkinter as tk
from tkinter import messagebox, filedialog
from threading import Thread

def leer_salida(proceso):
    while True:
        salida = proceso.stdout.readline()
        if salida == '' and proceso.poll() is not None:
            break
        if salida:
            texto.insert(tk.END, salida)
            texto.see(tk.END)
            window.update_idletasks()

def leer_error(proceso):
    while True:
        error = proceso.stderr.readline()
        if error == '' and proceso.poll() is not None:
            break
        if error:
            texto.insert(tk.END, error)
            texto.see(tk.END)
            window.update_idletasks()

def buscar_fagos():
    ruta_archivo = filedialog.askopenfilename(filetypes=(("Archivos GenBank", "*.gb"),("Todos los archivos", "*.*")))
    if ruta_archivo:
        try:
            texto.delete('1.0', tk.END)
            # Ejecuta PhiSpy.py con el archivo seleccionado
            proceso = subprocess.Popen(["PhiSpy.py", "-o", "Streptococcus.phages", ruta_archivo], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            Thread(target=leer_salida, args=(proceso,)).start()
            Thread(target=leer_error, args=(proceso,)).start()
        except Exception as e:
            messagebox.showinfo("Error", f"Error al buscar fagos: {e}")

def buscar_fagos_metricas():
    # Elimina los botones actuales
    boton_buscar.grid_forget()
    boton_secundario.grid_forget()
    boton_terciario.grid_forget()

    texto.delete('1.0', tk.END)

    def metrica_at_skew():   
        metrica = "at_skew"
        ruta_archivo = filedialog.askopenfilename(filetypes=(("Archivos GenBank", "*.gb"),("Todos los archivos", "*.*")))
        if ruta_archivo:
            try:
                # Ejecuta PhiSpy.py con el archivo seleccionado
                proceso = subprocess.Popen(["PhiSpy.py", "-o", "Streptococcus.phages", ruta_archivo, "--metrics", metrica], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                Thread(target=leer_salida, args=(proceso,)).start()
                Thread(target=leer_error, args=(proceso,)).start()
            except Exception as e:
                messagebox.showinfo("Error", f"Error al buscar fagos: {e}")

    def metrica_gc_skew():
        metrica = "gc_skew"
        ruta_archivo = filedialog.askopenfilename(filetypes=(("Archivos GenBank", "*.gb"),("Todos los archivos", "*.*")))
        if ruta_archivo:
            try:
                # Ejecuta PhiSpy.py con el archivo seleccionado
                proceso = subprocess.Popen(["PhiSpy.py", "-o", "Streptococcus.phages", ruta_archivo, "--metrics", metrica], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                Thread(target=leer_salida, args=(proceso,)).start()
                Thread(target=leer_error, args=(proceso,)).start()
            except Exception as e:
                messagebox.showinfo("Error", f"Error al buscar fagos: {e}")

    def metrica_shannon_slope():
        metrica = "shannon_slope"
        ruta_archivo = filedialog.askopenfilename(filetypes=(("Archivos GenBank", "*.gb"),("Todos los archivos", "*.*")))
        if ruta_archivo:
            try:
                # Ejecuta PhiSpy.py con el archivo seleccionado
                proceso = subprocess.Popen(["PhiSpy.py", "-o", "Streptococcus.phages", ruta_archivo, "--metrics", metrica], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                Thread(target=leer_salida, args=(proceso,)).start()
                Thread(target=leer_error, args=(proceso,)).start()
            except Exception as e:
                messagebox.showinfo("Error", f"Error al buscar fagos: {e}")

    def metrica_max_direction():
        metrica = "max_direction"
        ruta_archivo = filedialog.askopenfilename(filetypes=(("Archivos GenBank", "*.gb"),("Todos los archivos", "*.*")))
        if ruta_archivo:
            try:
                # Ejecuta PhiSpy.py con el archivo seleccionado
                proceso = subprocess.Popen(["PhiSpy.py", "-o", "Streptococcus.phages", ruta_archivo, "--metrics", metrica], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                Thread(target=leer_salida, args=(proceso,)).start()
                Thread(target=leer_error, args=(proceso,)).start()
            except Exception as e:
                messagebox.showinfo("Error", f"Error al buscar fagos: {e}")

    def metrica_orf_length_med():
        metrica = "orf_length_med"
        ruta_archivo = filedialog.askopenfilename(filetypes=(("Archivos GenBank", "*.gb"),("Todos los archivos", "*.*")))
        if ruta_archivo:
            try:
                # Ejecuta PhiSpy.py con el archivo seleccionado
                proceso = subprocess.Popen(["PhiSpy.py", "-o", "Streptococcus.phages", ruta_archivo, "--metrics", metrica], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                Thread(target=leer_salida, args=(proceso,)).start()
                Thread(target=leer_error, args=(proceso,)).start()
            except Exception as e:
                messagebox.showinfo("Error", f"Error al buscar fagos: {e}")

    # Crea los nuevos botones
    boton_at_skew = tk.Button(window, text="at_skew", command=metrica_at_skew, bg="#fc03fc", fg="white")
    boton_at_skew.grid(row=1, column=0, padx=10, pady=10)
    boton_gc_skew = tk.Button(window, text="gc_skew", command=metrica_gc_skew, bg="#fc03fc", fg="white")
    boton_gc_skew.grid(row=1, column=1, padx=5, pady=5)
    boton_shannon_slope = tk.Button(window, text="shannon_slope", command=metrica_shannon_slope, bg="#fc03fc", fg="white")
    boton_shannon_slope.grid(row=1, column=2, padx=5, pady=5)
    boton_max_direction = tk.Button(window, text="max_direction", command=metrica_max_direction, bg="#fc03fc", fg="white")
    boton_max_direction.grid(row=2, column=0, padx=5, pady=5)
    boton_orf_length_med = tk.Button(window, text="orf_length_med", command=metrica_orf_length_med, bg="#fc03fc", fg="white")
    boton_orf_length_med.grid(row=2, column=1, padx=5, pady=5)



def buscar_fagos_numero():
    # Elimina los botones actuales
    boton_buscar.grid_forget()
    boton_secundario.grid_forget()
    boton_terciario.grid_forget()

    texto.delete('1.0', tk.END)

    def numero1():

        ruta_archivo = filedialog.askopenfilename(filetypes=(("Archivos GenBank", "*.gb"),("Todos los archivos", "*.*")))
        if ruta_archivo:
            try:
                # Ejecuta PhiSpy.py con el archivo seleccionado
                proceso = subprocess.Popen(["PhiSpy.py", "-o", "Streptococcus.phages/", ruta_archivo, "--phage_genes", "1"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                Thread(target=leer_salida, args=(proceso,)).start()
                Thread(target=leer_error, args=(proceso,)).start()
            except Exception as e:
                messagebox.showinfo("Error", f"Error al buscar fagos: {e}")

    def numero2():
        ruta_archivo = filedialog.askopenfilename(filetypes=(("Archivos GenBank", "*.gb"),("Todos los archivos", "*.*")))
        if ruta_archivo:
            try:
                # Ejecuta PhiSpy.py con el archivo seleccionado
                proceso = subprocess.Popen(["PhiSpy.py", "-o", "Streptococcus.phages", ruta_archivo, "--phage_genes", "2"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                Thread(target=leer_salida, args=(proceso,)).start()
                Thread(target=leer_error, args=(proceso,)).start()
            except Exception as e:
                messagebox.showinfo("Error", f"Error al buscar fagos: {e}")

    # Crea los nuevos botones
    boton1 = tk.Button(window, text="1", command=numero1, bg="#fc03fc", fg="white")
    boton1.grid(row=1, column=0, padx=10, pady=10)
    boton2 = tk.Button(window, text="2", command=numero2, bg="#fc03fc", fg="white")
    boton2.grid(row=1, column=1, padx=5, pady=5)

window = tk.Tk()
window.title("Buscador de Fagos")
window.geometry("700x570")
window.configure(bg = '#1071e0')
texto = tk.Text(window, bg="grey", fg="yellow")
texto.grid(row=0, column=0, columnspan=3)  # Cambia esto a grid
texto.insert(tk.END, "¡Bienvenido al buscador de fagos! \n Por favor, seleccione un archivo GenBank para buscar fagos. \n"
             "También puede seleccionar una métrica para buscar fagos. \n" 
             """ ------------------------
  < Selecciona una opcion >
 -------------------------
 \                             .       .
  \                           / `.   .' " 
   \                  .---.  <    > <    >  .---.
    \                 |    \  \ - ~ ~ - /  /    |
         _____          ..-~             ~-..-~
        |     |   \~~~\.'                    `./~~~/
       ---------   \__/                        \__/
      .'  O    \     /               /       \  " 
     (_____,    `._.'               |         }  \/~~~/
      `----.          /       }     |        /    \__/
            `-.      |       /      |       /      `. ,~~|
                ~-.__|      /_ - ~ ^|      /- _      `..-'   
                     |     /        |     /     ~-.     `-. _  _  _
                     |_____|        |_____|         ~ - . _ _ _ _ _>
""")
boton_buscar = tk.Button(window, text="Busqueda predeterminada", command=buscar_fagos, bg="#e81c1c", fg="white")
boton_buscar.grid(row=1, column=0)  # Cambia esto a grid
boton_secundario = tk.Button(window, text="Buscador por metricas", command=buscar_fagos_metricas, bg="#e81c1c", fg="white")
boton_secundario.grid(row=1, column=1)  # Cambia esto a grid
boton_terciario = tk.Button(window, text="Buscador por numero", command=buscar_fagos_numero, bg="#e81c1c", fg="white")
boton_terciario.grid(row=1, column=2)  # Cambia esto a grid
window.mainloop()