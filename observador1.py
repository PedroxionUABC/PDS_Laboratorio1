# FileName: observador1.py
#Clase Observador: Define la interfaz de los observadores, 
# con un metodo actualizar() que sera implementado por los 
# observadores concretos.

#Clase Sujeto: Contiene una lista de observadores y 
# tiene metodos para agregar, eliminar y notificar 
# a los observadores sobre los cambios de estado.

#Clase ObservadorConcreto: Implementa el comportamiento del 
# observador concreto, en este caso, simplemente imprime un 
# mensaje cuando es notificado.

#Clase SujetoConcreto: Es una implementacion especifica de 
# Sujeto que contiene un estado. Cuando su estado cambia, 
# notifica a todos los observadores.

# Definir la clase Observador
class Observador:
    # Metodo que debe ser implementado por los observadores concretos
    # Recibe un mensaje de notificacion del sujeto
    def actualizar(self, mensaje):
        raise NotImplementedError("Debes implementar el metodo actualizar.")

# Definir la clase Sujeto
class Sujeto:
    def __init__(self):
        # Inicializamos la lista de observadores vacia
        self._observadores = []  # Lista para almacenar los observadores

    # Metodo para agregar un observador a la lista
    def agregar_observador(self, observador):
        # Verificamos si el observador ya esta en la lista
        if observador not in self._observadores:
            self._observadores.append(observador)  # Agregamos el observador

    # Metodo para eliminar un observador de la lista
    def eliminar_observador(self, observador):
        # Eliminamos el observador si existe en la lista
        self._observadores.remove(observador)

    # Metodo para notificar a todos los observadores sobre un cambio
    def notificar(self, mensaje):
        # Iteramos sobre todos los observadores registrados
        for observador in self._observadores:
            observador.actualizar(mensaje)  # Llamamos a su metodo de actualizacion

# Implementar un observador concreto que hereda de Observador
class ObservadorConcreto(Observador):
    def __init__(self, nombre):
        # Asignamos un nombre al observador para identificarlo
        self.nombre = nombre

    # Implementacion del metodo actualizar del Observador
    def actualizar(self, mensaje):
        # Simplemente imprimimos el mensaje recibido
        print(f"{self.nombre} ha recibido el mensaje: {mensaje}")

# Implementar un sujeto concreto que hereda de Sujeto
class SujetoConcreto(Sujeto):
    def __init__(self, estado):
        # Inicializamos el sujeto con un estado
        super().__init__()  # Llamamos al constructor de la clase base (Sujeto)
        self._estado = estado  # El estado inicial del sujeto

    # Metodo para obtener el estado actual del sujeto
    def obtener_estado(self):
        return self._estado

    # Metodo para actualizar el estado y notificar a los observadores
    def establecer_estado(self, estado):
        self._estado = estado  # Actualizamos el estado
        # Llamamos a notificar para avisar a los observadores del cambio
        self.notificar(f"Estado actualizado a {estado}")

# Crear instancias y probar el patron
if __name__ == "__main__":
    # Creamos un sujeto concreto con un estado inicial
    sujeto = SujetoConcreto("Inicial")

    # Creamos dos observadores con nombres diferentes
    observador1 = ObservadorConcreto("Observador 1")
    observador2 = ObservadorConcreto("Observador 2")

    # Agregamos ambos observadores al sujeto
    sujeto.agregar_observador(observador1)
    sujeto.agregar_observador(observador2)

    # Cambiamos el estado del sujeto, lo cual desencadenara una notificacion
    sujeto.establecer_estado("Nuevo estado")

    # Esperamos que ambos observadores reciban la notificacion sobre el cambio de estado