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

 
