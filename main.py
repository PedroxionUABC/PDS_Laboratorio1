"""
Sistema de Notificacion de Estado de Servidores usando el Patron Observador

# Problema
Se necesita un sistema para monitorear el estado de los servidores en un centro de datos. Cuando un servidor 
presenta una falla o queda fuera de servicio, los administradores deben recibir una notificación inmediata 
para tomar acciones correctivas.

# Contexto
En un entorno de TI, los servidores pueden fallar debido a problemas de hardware, software o red. Para 
garantizar la continuidad del servicio, es crucial detectar y notificar estos eventos a los administradores 
de manera eficiente y automatizada.

# Solución
Implementamos el Patrón Observador, donde el **Servidor Central** actúa como el **Sujeto**, y los **Administradores** 
actúan como los **Observadores**. Cada administrador recibe una alerta cuando un servidor reporta una falla.

# Estructura
- **Sujeto (SujetoConcreto - Servidor Central)**: Mantiene una lista de administradores y los notifica ante cambios.
- **Observador (ObservadorConcreto - Administrador de Sistemas)**: Implementa la reacción a la notificación de fallos en servidores.
"""
import customtkinter as ctk
from observador1 import *

class ServidorCentral(SujetoConcreto):
    def __init__(self):
        super().__init__("Operativo")

    def reportar_falla(self, mensaje):
        self.establecer_estado(f"{mensaje}")

class AdministradorSistema(ObservadorConcreto):

    def __init__(self, nombre):
        super().__init__(nombre)

    def reportar_falla(self, mensaje):
        servidor.reportar_falla(mensaje)
        app.textbox.insert("0.0", 'C:Usuarios/Administrador_' + self.getNombre() + ': echo "Ha habido una falla"\n')

    def getNombre(self):
        return self.nombre

    
if __name__ == "__main__":
    servidor = ServidorCentral()
    admin1 = AdministradorSistema("Pedro")
    admin2 = AdministradorSistema("David")
    servidor.agregar_observador(admin1)
    servidor.agregar_observador(admin2)
    # Configuracion de pantalla
    app = ctk.CTk()
    app.geometry("600x500")
    app.title("CTk example")
    app.grid_rowconfigure(0, weight=2)
    app.grid_columnconfigure(0, weight=2)
    # Widgets
    app.textbox = ctk.CTkTextbox(master=app, width=400, corner_radius=0)
    app.textbox.grid(row=0, column=0, sticky="nsew")
    app.button = ctk.CTkButton(app, 
                               text="Reportar falla en el servidor", 
                               command=lambda:admin1.reportar_falla("No operativo"))
    app.button.grid(row=1, column=0, sticky="nsew")
    app.button = ctk.CTkButton(app,
                               fg_color='#e93100', 
                               text="Reportar falla en el servidor", 
                               command=lambda:admin2.reportar_falla("No operativo"))
    app.button.grid(row=2, column=0, sticky="nsew")

app.mainloop()