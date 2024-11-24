class Asignatura:

    def __init__(self, nombre, salon="remoto"):
        self._nombre = nombre
        self._salon = salon

    def __str__(self): #Se crea para poder imprimir las caracterísitcas del objeto cuando se llame
        cadena = self._nombre +" "+ self._salon
        return cadena
