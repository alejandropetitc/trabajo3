from participante import Partic
from pregunta import Preg
from encuesta import Encu
from coordinador import Coord

if __name__ == "__main__":
    # Crear un coordinador
    coord = Coord("Yelena", "yelena@example.com")

    # Crear una nueva encuesta
    encuesta = coord.crear_encuesta("Encuesta de Satisfacción")

    # Crear preguntas
    preg1 = Preg("¿Cuál es tu comida favorita?", "opcion")
    preg1.agregar_opcion("Pizza")
    preg1.agregar_opcion("Sushi")
    preg1.agregar_opcion("Ensalada")

    preg2 = Preg("¿Cuál es tu hobby?", "abierta")

    # Agregar preguntas a la encuesta
    encuesta.agregar_pregunta(preg1)
    encuesta.agregar_pregunta(preg2)

    # Crear participantes
    part1 = Partic("Juan Perez", "juan.perez@example.com", "1234567890")
    part2 = Partic("Maria Lopez", "maria.lopez@example.com", "0987654321")

    # Agregar participantes a la encuesta
    encuesta.agregar_participante(part1)
    encuesta.agregar_participante(part2)

    # Mostrar preguntas y participantes
    encuesta.mostrar_preguntas()
    encuesta.mostrar_participantes()

    # Generar informe de la encuesta
    coord.generar_informe(encuesta)
