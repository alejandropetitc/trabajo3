import csv

class Partic:
    def __init__(self, nom, mail, tel, edad=None, gen=None, dir=None, ciu=None, emp=None, car=None, sal=None):
        self.nom = nom
        self.mail = mail
        self.tel = tel
        self.edad = edad
        self.gen = gen
        self.dir = dir
        self.ciu = ciu
        self.emp = emp
        self.car = car
        self.sal = sal

    def __str__(self):
        return f'Participante: {self.nom}, Mail: {self.mail}, Tel: {self.tel}'

    @staticmethod
    def cargar_desde_csv(ruta_archivo):
        partics = []
        with open(ruta_archivo, newline='', encoding='utf-8') as archivo_csv:
            lector = csv.DictReader(archivo_csv)
            for fila in lector:
                partic = Partic(
                    nom=fila.get('nombre'),
                    mail=fila.get('correo'),
                    tel=fila.get('telefono'),
                    edad=fila.get('edad'),
                    gen=fila.get('genero'),
                    dir=fila.get('direccion'),
                    ciu=fila.get('ciudad'),
                    emp=fila.get('empresa'),
                    car=fila.get('cargo'),
                    sal=fila.get('salario')
                )
                partics.append(partic)
        return partics
