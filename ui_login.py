import tkinter as tk
from tkinter import messagebox, PhotoImage
from ui_admin import AdminApp
from ui_alumno import AlumnoApp
from gestor_json import validar_usuario

class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login - Sistema de Asistencia")
        self.geometry("400x430")
        self.resizable(False, False)
        self.configure(bg="#FFFFFF")

        tk.Label(self, text="Seleccione Rol:", bg="#FFFFFF", font=("Arial", 16, "bold")).pack(pady=30)

        tk.Button(self, text="Administrador", width=20, height=2, font=("Arial", 12),
                  command=self.login_admin).pack(pady=10)
        tk.Button(self, text="Alumno", width=20, height=2, font=("Arial", 12),
                  command=self.login_alumno).pack(pady=10)

    def login_admin(self):
        self.withdraw()
        AdminLogin(self)

    def login_alumno(self):
        self.withdraw()
        AlumnoLogin(self)

class AdminLogin(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Login Administrador")
        self.geometry("400x430")
        self.resizable(False, False)
        self.configure(bg="#d9d9d9")  
        self.master = master

        try:
            self.iconbitmap("sources/user.ico")
        except Exception as e:
            print("No se pudo cargar el ícono:", e)

        frame = tk.Frame(self, bg="#d9d9d9")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text="INICIAR SESIÓN", bg="#d9d9d9", font=("Arial", 16, "bold")).pack(pady=(10, 25))
        
        try:
            self.img_user = PhotoImage(file="sources/profile_key.png").subsample(7, 7)
            tk.Label(frame, image=self.img_user, bg="#d9d9d9").pack(pady=(0, 25))
        except:
            tk.Label(frame, text="PERFIL", bg="#d9d9d9", font=("Arial", 48)).pack(pady=(0, 25))

        tk.Label(frame, text="Usuario:", bg="#d9d9d9", font=("Arial", 12)).pack(anchor="w")
        self.entry_usuario = tk.Entry(frame, font=("Arial", 14), width=30)
        self.entry_usuario.pack(anchor="w", pady=(5, 15))

        tk.Label(frame, text="Contraseña:", bg="#d9d9d9", font=("Arial", 12)).pack(anchor="w")
        self.entry_password = tk.Entry(frame, show="*", font=("Arial", 14), width=30)
        self.entry_password.pack(pady=(5, 25))

        tk.Button(frame, text="Ingresar", font=("Arial", 12, "bold"),
                  bg="#4a90e2", fg="white",
                  activebackground="#357ab8",
                  activeforeground="white",
                  relief="flat", width=30,
                  height=1,
                  command=self.validar).pack(pady=5, fill="x")

    def validar(self):
        usuario = self.entry_usuario.get().strip()
        password = self.entry_password.get().strip()

        usuario_valido = validar_usuario(usuario, password, rol="administrador")

        if usuario_valido:
            nombre_admin = usuario_valido["name"]  
            self.destroy()
            self.master.destroy()
            app = AdminApp(admin_name=nombre_admin)
            app.mainloop()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos", parent=self)

class AlumnoLogin(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Login Alumno")
        self.state('zoomed')
        self.configure(bg="#E6E6E6")
        self.master = master

        frame = tk.Frame(self, bg="#E6E6E6")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text="Código de alumno:", bg="#E6E6E6", font=("Arial", 14)).pack(pady=10)
        self.entry_codigo = tk.Entry(frame, font=("Arial", 14))
        self.entry_codigo.pack(pady=10)

        tk.Button(frame, text="Ingresar", font=("Arial", 14),
                  command=self.validar).pack(pady=15)

    def validar(self):
        from gestor_json import obtener_alumnos
        codigo = self.entry_codigo.get()
        alumnos = obtener_alumnos()
        for alumno in alumnos:
            if alumno["codigo"] == codigo:
                self.destroy()
                self.master.destroy()
                AlumnoApp(codigo)
                return
        messagebox.showerror("Error", "Código incorrecto")
