traducir el siguiente código a Python:
public class Main {
	public static void main(String[] args) {
	    int b = 23;
	    Fraccion fr = new Fraccion();
	    Fraccion fs = new Fraccion(3, 5);
	    fr.setNum(1); //  fr.num = 1;
	    fr.setDen(0);//  fr.den = 4;
		System.out.println(fr.getNum() + "/" + fr.getDen());
		System.out.println(fs.getNum() + "/" + fs.getDen());
		fs.set(8, 9);
		System.out.println(fs.getNum() + "/" + fs.getDen());
	}
}

class Fraccion {
    private int num;
    private int den;

    Fraccion() {
        // System.out.println("Nuevo objeto Fraccion creado!");
    }
    Fraccion(int num, int den) {
        this.num = num;
        this.den = den;
    }
    void set(int num, int den) {
        this.num = num;
        this.den = den;
    }
    void setNum(int x) {
        num = x;
    }
    void setDen(int x) {
        if (x == 0)
            den = 1;
        else
            den = x;
    }
    int getNum() {
        return num;
    }
    int getDen() {
        return den;
    }
}
