import tkinter as tk
from gestor_json import obtener_alumnos

class ListaAlumnos(tk.Toplevel):
    def __init__(self, master, log_widget=None):
        super().__init__(master)
        self.title("Lista de Alumnos")
        self.geometry("500x400")
        self.configure(bg="#5F5F5F")
        self.log_widget = log_widget

        tk.Label(self, text="Lista de alumnos", bg="#FFFFFF",
                 font=("Arial", 14, "bold")).pack(pady=15)

        self.text = tk.Text(self, width=60, height=20)
        self.text.pack(pady=10)

        self.mostrar_alumnos()

    def mostrar_alumnos(self):
        alumnos = obtener_alumnos()
        self.text.delete("1.0", tk.END)
        for a in alumnos:
            nie = a.get("nie", "N/A")
            nombres = a.get("nombres", "")
            apellidos = a.get("apellidos", "")
            self.text.insert(tk.END, f"{nie} | {nombres} {apellidos}\n")
        
        if self.log_widget:
            self.log_widget.insert(tk.END, f"Se visualizó la lista de {len(alumnos)} alumnos.\n")
