# /usr/bin/env python3

class Vehiculo:

    def __init__(self, matricula, modelo):

        self.matricula = matricula
        self.modelo = modelo
        self.disponible = True

    def alquilar(self):

        if self.disponible:
            self.disponible = False
            return

        print(
            f"\n[!] El vehículo con matrícula {self.matricula} no está disponible")

    def devolver(self):

        if not self.disponible:
            self.disponible = True
            return

        print(
            f"\n[!] El vehículo con matrícula {self.matricula} no está alquilado")

    def __str__(self):

        return f"    Vehículo(mat={self.matricula}, mod={self.modelo}, disp={'Sí' if self.disponible else 'No'})"


class Flota:

    def __init__(self):

        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):

        self.vehiculos.append(vehiculo)

    def mostrar_vehiculos(self):

        for vehiculo in self.vehiculos:
            print(vehiculo)

    def alquilar_vehiculo(self, matricula):

        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.alquilar()

    def devolver_vehiculo(self, matricula):

        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.devolver()

    def __str__(self):

        return "\n".join([str(vehiculo) for vehiculo in self.vehiculos])


if __name__ == '__main__':

    flota = Flota()

    flota.agregar_vehiculo(Vehiculo('1234ABC', 'Ford Fiesta'))
    flota.agregar_vehiculo(Vehiculo('5678DEF', 'Renault Clio'))

    print(f"\n[+] Flota inicial:\n{flota}")

    flota.alquilar_vehiculo('1234ABC')

    print(f"\n[+] Flota después de alquilar el Ford Fiesta:\n{flota}")

    flota.devolver_vehiculo('1234ABC')

    print(f"\n[+] Flota después de devolver el Ford Fiesta:\n{flota}")
