import pytest
from unittest.mock import MagicMock
from io import StringIO
import sys

from observador1 import ObservadorConcreto, SujetoConcreto
# Importar las clases desde el modulo donde las definiste

# Prueba para verificar el patron de diseño Observador
def test_notificar_a_observadores():
    # Creamos un sujeto concreto con un estado inicial
    sujeto = SujetoConcreto("Inicial")

    # Creamos dos observadores concretos con nombres diferentes
    observador1 = ObservadorConcreto("Observador 1")
    observador2 = ObservadorConcreto("Observador 2")

    # Usamos MagicMock para verificar que los metodos actualizar son llamados
    observador1_mock = MagicMock()
    observador2_mock = MagicMock()

    # Agregamos los observadores al sujeto
    sujeto.agregar_observador(observador1_mock)
    sujeto.agregar_observador(observador2_mock)

    # Cambiamos el estado del sujeto
    sujeto.establecer_estado("Nuevo estado")

    # Verificamos que el metodo actualizar de ambos observadores ha sido llamado
    observador1_mock.actualizar.assert_called_with("Estado actualizado a Nuevo estado")
    observador2_mock.actualizar.assert_called_with("Estado actualizado a Nuevo estado")


# Prueba para verificar que se eliminan correctamente los observadores
def test_eliminar_observador():
    # Creamos un sujeto concreto
    sujeto = SujetoConcreto("Inicial")

    # Creamos un observador
    observador = ObservadorConcreto("Observador 1")

    # Agregamos el observador al sujeto
    sujeto.agregar_observador(observador)

    # Verificamos que el observador esta en la lista de observadores
    assert observador in sujeto._observadores

    # Eliminamos el observador
    sujeto.eliminar_observador(observador)

    # Verificamos que el observador ha sido eliminado
    assert observador not in sujeto._observadores


# Prueba para verificar que un observador recibe la notificacion correctamente
def test_notificacion_imprime_mensaje():
    # Creamos un sujeto concreto
    sujeto = SujetoConcreto("Inicial")

    # Creamos un observador
    observador = ObservadorConcreto("Observador 1")

    # Capturamos lo que imprime el observador
    captured_output = StringIO()
    sys.stdout = captured_output  # Redirigimos la salida estandar a StringIO

    # Agregamos el observador al sujeto
    sujeto.agregar_observador(observador)

    # Cambiamos el estado del sujeto
    sujeto.establecer_estado("Nuevo estado")

    # Verificamos que el mensaje correcto fue impreso
    assert "Observador 1 ha recibido el mensaje: Estado actualizado a Nuevo estado" in captured_output.getvalue()

    sys.stdout = sys.__stdout__  # Restauramos la salida estandar a la original