package application_1;

import java.util.Scanner;
//import java.util.*;
public class Application_1 {

    public static void main(String[] args) {
        /*int var1= 10, var2= 10, var3 = 10;
        float fvar1 = 12.5f, fvar2 = 15f;
        double dvar1 = 12.3564598878554565654;
        String nombre = "aDRIAN";
        char c ='f';
        System.out.println(dvar1+" "+fvar1);
        System.out.println(var1+"  "+ var2 + " " + var3);
        System.out.println("El numero es "+fvar2);
        System.out.println("Su nombre es: "+nombre);
        System.out.println(nombre.equals("pepe"));
        System.out.println(nombre.equalsIgnoreCase("adrian"));*/
        
//SUMAR DOS NUMEROS
        Scanner n1 = new Scanner(System.in);
        int i1, i2, r;
        String nombre;
        System.out.println("Digite su nombre: ");
        nombre = n1.next();
        System.out.println("Digita un numero: ");
        i1 = n1.nextInt();
        System.out.println("Digite otro numero: ");
        i2 = n1.nextInt();
        r = i1+i2;
        System.out.println("\nEl resultado es: "+r);
        System.out.println("Su nombre es: "+nombre);
    }
    
}
