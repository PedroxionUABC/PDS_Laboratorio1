"""
Sistema de Notificación de Estado de Servidores usando el Patrón Observador

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

# Importamos las clases base desde el código existente
"""
import customtkinter as ctk
from observador1 import *

class ServidorCentral(SujetoConcreto):
    def __init__(self):
        super().__init__("Operativo")

    def reportar_falla(self, mensaje):
        self.establecer_estado(f"¡Alerta! {mensaje}")

class AdministradorSistema(ObservadorConcreto):

    def __init__(self, nombre):
        super().__init__(nombre)

    def reportar_falla(self, mensaje):
        servidor.reportar_falla("Ha habido una falla")
        app.textbox.insert("0.0", 'C:Usuarios/Administrador: echo "Ha habido una falla"\n')

    
if __name__ == "__main__":
    servidor = ServidorCentral()
    admin1 = AdministradorSistema("Administrador Pedro")
    servidor.agregar_observador(admin1)
    # Configuracion de pantalla
    app = ctk.CTk()
    app.geometry("600x500")
    app.title("CTk example")
    app.grid_rowconfigure(0, weight=2)  # configure grid system
    app.grid_columnconfigure(0, weight=2)
    # Widgets
    app.textbox = ctk.CTkTextbox(master=app, width=400, corner_radius=0)
    app.textbox.grid(row=0, column=0, sticky="nsew")
    app.button = ctk.CTkButton(app, text="Reportar falla en el servidor", command=lambda:admin1.reportar_falla("Ha habido una falla"))
    app.button.grid(row=2, column=0, sticky="nsew")

app.mainloop()