import tkinter as tk
from gestor_json import obtener_asistencias

class HistorialAsistencias(tk.Toplevel):
    def __init__(self, master, log_widget=None):
        super().__init__(master)
        self.title("Historial de Asistencias")
        self.geometry("500x400")
        self.configure(bg="#FFFFFF")
        self.log_widget = log_widget

        tk.Label(self, text="Historial de asistencias", bg="#D3D3D3",
                 font=("Arial", 14, "bold")).pack(pady=15)

        self.text = tk.Text(self, width=60, height=20)
        self.text.pack(pady=10)

        self.mostrar_asistencias()

    def mostrar_asistencias(self):
        asistencias = obtener_asistencias()
        self.text.delete("1.0", tk.END)
        for a in asistencias:
            self.text.insert(tk.END, f"{a['codigo']} | {a['fecha']}\n")
        if self.log_widget:
            self.log_widget.insert(tk.END, f"Se visualizó el historial de {len(asistencias)} asistencias.\n")
