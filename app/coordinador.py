from encuesta import Encu

class Coord:
    def __init__(self, nom, mail):
        self.nom = nom
        self.mail = mail

    def crear_encuesta(self, titulo):
        return Encu(titulo)

    def generar_informe(self, encuesta):
        print(f"\n--- Informe de la Encuesta: {encuesta.tit} ---")
        print(f"Total de Participantes: {len(encuesta.partics)}")
        print("Participantes:")
        for p in encuesta.partics:
            print(f"- {p.nom} ({p.mail})")
        print("\nPreguntas y Respuestas:")
        for preg in encuesta.preguntas:
            print(f"Pregunta: {preg.txt} (Tipo: {preg.tipo})")
            if preg.tipo in ['opcion', 'multiple']:
                print("Opciones:")
                for opc in preg.opc:
                    print(f"  - {opc}")
            else:
                print("Esta pregunta es abierta.")
        print("-------------------------------")
