class Encu:
    def __init__(self, tit):
        self.tit = tit
        self.preguntas = []
        self.partics = []

    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)

    def agregar_participante(self, participante):
        self.partics.append(participante)

    def mostrar_preguntas(self):
        print(f"Encuesta: {self.tit}")
        for idx, preg in enumerate(self.preguntas, start=1):
            print(f"{idx}. {preg.txt}")

    def mostrar_participantes(self):
        print("Participantes:")
        for p in self.partics:
            print(p)
