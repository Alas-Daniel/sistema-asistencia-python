import tkinter as tk
from tkinter import scrolledtext, messagebox
from gestor_json import agregar_alumno, obtener_alumnos, obtener_asistencias, registrar_asistencia
from ticketera import imprimir_ticket
from datetime import datetime

class AdminApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Administrador - Sistema de Asistencia")
        self.geometry("700x500")
        self.configure(bg="#F2F2F2")

        tk.Label(self, text="Agregar nuevo alumno:", bg="#F2F2F2", font=("Arial", 12, "bold")).pack(pady=10)
        self.entry_nombre = tk.Entry(self, width=40)
        self.entry_nombre.pack(pady=5)
        tk.Button(self, text="Agregar y generar ticket", command=self.agregar_alumno_func).pack(pady=5)
        tk.Button(self, text="Ver lista de alumnos", command=self.ver_alumnos).pack(pady=5)
        tk.Button(self, text="Ver asistencias", command=self.ver_asistencias).pack(pady=5)

        self.text_log = scrolledtext.ScrolledText(self, width=80, height=20)
        self.text_log.pack(pady=10)

        self.mainloop()

    def agregar_alumno_func(self):
        nombre = self.entry_nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Aviso", "Ingrese un nombre")
            return
        codigo = nombre.upper().replace(" ", "") + "123"
        agregar_alumno(nombre, codigo)
        imprimir_ticket(nombre, codigo)
        self.text_log.insert(tk.END, f"Alumno agregado: {nombre} | Código: {codigo}\n")
        self.entry_nombre.delete(0, tk.END)

    def ver_alumnos(self):
        alumnos = obtener_alumnos()
        self.text_log.insert(tk.END, "\nLista de alumnos:\n")
        for a in alumnos:
            self.text_log.insert(tk.END, f"{a['nombre']} | {a['codigo']}\n")

    def ver_asistencias(self):
        asistencias = obtener_asistencias()
        self.text_log.insert(tk.END, "\nAsistencias:\n")
        for a in asistencias:
            self.text_log.insert(tk.END, f"{a['codigo']} | {a['fecha']}\n")
