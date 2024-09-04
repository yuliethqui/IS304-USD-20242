'''
Tarea para antes de la  próxima clase:
Crear un programa en Python que cree una clase denominada CuentaBancaria. Agregar encapsulamiento y sobrecarga del constructor de clase, asi como los métodos get y set requeridos para gestionar los atributos de dicha clase.
Los atributos de la clase debern ser: __numeroCta, __nombreCliente, __fechaApertura, __saldo.
Agregar metodos para aperturar cuentas, realizar consignaciones y retiros controlados (es decir, no permitir consignaciones negativas, ni retiros superiores al saldo, las aperturas deben exigir un valor inicial mínimo de 100 mil pesos).
Crear un menú para crear objetos y realizar las diversas operaciones referidas.

'''
import java.util.Scanner;



public class CuentaBancaria {

 // public static void main (String [] args){
// Atributos
private int NumeroCta;
private String NombreCliente;
private String FechaApertura;
private double saldo; 

       public CuentaBancaria(){
        
        this.NumeroCta = "";
        this.NumeroCliente = "";
        this.FechaApertura = "";
        this.saldo = 0.0;
        
        public CuentaBancaria (String NumeroCta, String NumeroCliente, String FechaApertura, double saldo){
            
            this.NumeroCta = NumeroCta;
            this.NumeroCliente = NumeroCliente;
            this.FechaApertura = FechaApertura;
            setsaldo(saldo); 

}
        public String getNumeroCta(){
            return NumeroCta;
            
        }
        
        public String getNumeroCliente(){
            return NumeroCliente;
            
        }
        public String getFechaApertura(){
            return FechaApertura;
        }
        public double getsaldo(){
            return saldo;
            
        }
        
        public void setNumeroCta (String NumeroCta){
            this.NumeroCta = NumeroCta;
            
        }public void setNumeroCliente (String NumeroCliente){
            this.NumeroCliente = NumeroCliente;
            
        }
        public void setFechaApertura(String FechaApertura){
            this.FechaApertura = FechaApertura;
            
        } 
        public void setsaldo (double saldo){
            this.saldo = saldo;
            
        }
        
        public void setsaldo (double saldo){
            if (saldo >= 100000){
                this.saldo = saldo;
            }else {
                System.out.println ()


 // }
}


