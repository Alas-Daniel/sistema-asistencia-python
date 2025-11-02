# admin_registro.py
import tkinter as tk
from tkinter import messagebox
import json
import os

ALUMNOS_FILE = os.path.join("data", "alumnos.json")

class RegistroAlumno(tk.Toplevel):
    def __init__(self, master, log_widget=None):
        super().__init__(master)
        self.title("Registrar Alumno")
        self.geometry("400x300")
        self.configure(bg="#D1D1D1")
        self.log_widget = log_widget

        tk.Label(self, text="REGISTRAR ALUMNO", bg="#D1D1D1",
                 font=("Arial", 14, "bold")).pack(pady=15)

        tk.Label(self, text="NIE:", bg="#D1D1D1", font=("Arial", 12)).pack()
        self.entry_nie = tk.Entry(self, width=30)
        self.entry_nie.pack(pady=5)

        tk.Label(self, text="Nombres:", bg="#D1D1D1", font=("Arial", 12)).pack()
        self.entry_nombres = tk.Entry(self, width=30)
        self.entry_nombres.pack(pady=5)

        tk.Label(self, text="Apellidos:", bg="#D1D1D1", font=("Arial", 12)).pack()
        self.entry_apellidos = tk.Entry(self, width=30)
        self.entry_apellidos.pack(pady=5)

        btn_frame = tk.Frame(self, bg="#D1D1D1")
        btn_frame.pack(pady=15)

        tk.Button(btn_frame, text="Agregar", bg="#2DCA35", fg="black",
            width=10, relief="flat", activebackground="#28A230", activeforeground="white",
            command=self.agregar_alumno).grid(row=0, column=0, padx=5)

        tk.Button(btn_frame, text="Limpiar", bg="#F0E113", fg="black",
                width=10, relief="flat", activebackground="#E5D611", activeforeground="white",
                command=self.limpiar_campos).grid(row=0, column=1, padx=5)

        tk.Button(btn_frame, text="Regresar", bg="#DB1714", fg="black",
                width=10, relief="flat", activebackground="#C21210", activeforeground="white",
                command=self.destroy).grid(row=0, column=2, padx=5)


    def agregar_alumno(self):
        nie = self.entry_nie.get().strip()
        nombres = self.entry_nombres.get().strip()
        apellidos = self.entry_apellidos.get().strip()

        if not nie or not nombres or not apellidos:
            messagebox.showwarning("Aviso", "Todos los campos son obligatorios.")
            return

        if os.path.exists(ALUMNOS_FILE):
            with open(ALUMNOS_FILE, "r", encoding="utf-8") as f:
                try:
                    alumnos = json.load(f)
                except json.JSONDecodeError:
                    alumnos = []
        else:
            alumnos = []

        alumno = {
            "nie": nie,
            "nombres": nombres,
            "apellidos": apellidos
        }
        alumnos.append(alumno)

        with open(ALUMNOS_FILE, "w", encoding="utf-8") as f:
            json.dump(alumnos, f, indent=4, ensure_ascii=False)

        messagebox.showinfo("Éxito", f"Alumno {nombres} {apellidos} agregado correctamente.")
        if self.log_widget:
            self.log_widget.insert(tk.END, f"Alumno agregado: {nie} | {nombres} {apellidos}\n")

        self.limpiar_campos()

    def limpiar_campos(self):
        self.entry_nie.delete(0, tk.END)
        self.entry_nombres.delete(0, tk.END)
        self.entry_apellidos.delete(0, tk.END)
