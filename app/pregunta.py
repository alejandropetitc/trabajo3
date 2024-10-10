class Preg:
    def __init__(self, txt, tipo, opc=None):
        self.txt = txt
        self.tipo = tipo
        self.opc = opc if opc is not None else []

    def __str__(self):
        return f'Pregunta: {self.txt} (Tipo: {self.tipo})'

    def agregar_opcion(self, opcion):
        if self.tipo in ['opcion', 'multiple']:
            self.opc.append(opcion)
        else:
            print("No se pueden agregar opciones a este tipo de pregunta.")
    
    def mostrar_opciones(self):
        if self.opc:
            print("Opciones disponibles:")
            for idx, opc in enumerate(self.opc, start=1):
                print(f"{idx}. {opc}")
        else:
            print("Esta pregunta no tiene opciones o no es de opción múltiple.")
