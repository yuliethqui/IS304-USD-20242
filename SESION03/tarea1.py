'''
Tarea para antes de la  próxima clase:
Crear un programa en Python que cree una clase denominada CuentaBancaria. Agregar encapsulamiento y sobrecarga del constructor de clase, asi como los métodos get y set requeridos para gestionar los atributos de dicha clase.
Los atributos de la clase debern ser: __numeroCta, __nombreCliente, __fechaApertura, __saldo.
Agregar metodos para aperturar cuentas, realizar consignaciones y retiros controlados (es decir, no permitir consignaciones negativas, ni retiros superiores al saldo, las aperturas deben exigir un valor inicial mínimo de 100 mil pesos).
Crear un menú para crear objetos y realizar las diversas operaciones referidas.

'''

class CuentaBancaria:
    def __init__(self, numero_cta=None, nombre_cliente=None, fecha_apertura=None, saldo=0):
        self.__numeroCta = numero_cta
        self.__nombreCliente = nombre_cliente
        self.__fechaApertura = fecha_apertura
        self.__saldo = saldo
    def get_numeroCta(self):
        return self.__numeroCta

    def set_numeroCta(self, numero_cta):
        self.__numeroCta = numero_cta

    def get_nombreCliente(self):
        return self.__nombreCliente

    def set_nombreCliente(self, nombre_cliente):
        self.__nombreCliente = nombre_cliente

    def get_fechaApertura(self):
        return self.__fechaApertura

    def set_fechaApertura(self, fecha_apertura):
        self.__fechaApertura = fecha_apertura

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        if saldo >= 100000:
            self.__saldo = saldo
        else:
            print("El saldo inicial debe ser de al menos 100,000 pesos.")

def aperturar_cuenta(self, numero_cta, nombre_cliente, fecha_apertura, saldo_inicial):
        if saldo_inicial < 100000:
            print("El saldo inicial debe ser de al menos 100,000 pesos.")
        else:
            self.__numeroCta = numero_cta
            self.__nombreCliente = nombre_cliente
            self.__fechaApertura = fecha_apertura
            self.__saldo = saldo_inicial
            print(f"Cuenta {self.__numeroCta} a nombre de {self.__nombreCliente} creada exitosamente con saldo de {self.__saldo}.")
 
def consignar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Consignación exitosa. Nuevo saldo: {self.__saldo}.")
        else:
            print("No se puede consignar un valor negativo o nulo.")

 def retirar(self, valor):
        if valor > self.__saldo:
            print("Fondos insuficientes para realizar el retiro.")
        elif valor <= 0:
            print("El valor a retirar debe ser mayor a 0.")
        else:
            self.__saldo -= valor
            print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}.")

 def menu():
    cuenta = None

    while True:
        print(" Menú Cuenta Bancaria ")
        print("1. Aperturar cuenta")
        print("2. Consignar")
        print("3. Retirar")
        print("4. Consultar saldo")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero_cta = input("Ingrese el número de cuenta: ")
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            fecha_apertura = input("Ingrese la fecha de apertura (dd/mm/aaaa): ")
            saldo_inicial = float(input("Ingrese el saldo inicial (mínimo 100,000): "))
            cuenta = CuentaBancaria()
            cuenta.aperturar_cuenta(numero_cta, nombre_cliente, fecha_apertura, saldo_inicial)

        elif opcion == "2":
            if cuenta is None:
                print("Primero debe aperturar una cuenta.")
            else:
                valor = float(input("Ingrese el valor a consignar: "))
                cuenta.consignar(valor)

        elif opcion == "3":
            if cuenta is None:
                print("Primero debe aperturar una cuenta.")
            else:
                valor = float(input("Ingrese el valor a retirar: "))
                cuenta.retirar(valor)

        elif opcion == "4":
            if cuenta is None:
                print("Primero debe aperturar una cuenta.")
            else:
                print(f"Saldo actual: {cuenta.get_saldo()}")

        elif opcion == "5":
            print("Gracias por usar el sistema bancario. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")   

if __name__ == "__main__":
    menu()
