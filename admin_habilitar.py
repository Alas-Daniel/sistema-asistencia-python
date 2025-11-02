import tkinter as tk
from tkinter import messagebox

class HabilitarAsistencia(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Habilitar Asistencia")
        self.geometry("400x200")
        self.configure(bg="#FFFFFF")

        tk.Label(self, text="Habilitar asistencia de alumnos", bg="#9E9E9E",
                 font=("Arial", 14, "bold")).pack(pady=20)

        tk.Button(self, text="Habilitar", bg="#000000", fg="white",
                  font=("Arial", 12, "bold"),
                  command=self.habilitar).pack(pady=20)

    def habilitar(self):
        messagebox.showinfo("Aqui vamos a poner la interfaz para marcar asistencia")
        self.destroy()
