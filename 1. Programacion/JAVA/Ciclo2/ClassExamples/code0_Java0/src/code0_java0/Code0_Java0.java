/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package code0_java0;

import java.util.Scanner;

/**
 *
 * @author aero7
 */
public class Code0_Java0 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        /**
     * @param args the command line arguments
     */
        // TODO code application logic here
        Scanner lector = new Scanner(System.in);
        int dato = lector.nextInt();
        dato++;
        int numero = 1;
        double numero_decimal = 1.5;
        double suma = numero + numero_decimal;
        float punto_flotante = 123.2f;
        String nombre = "Adrian";
        Boolean verified = true;
        /*System.out.println("La suma es: "+ suma); /*sout + tab*/
        
        if(numero < 10){
            System.out.println(punto_flotante); // CTRL + Space...autocompletar
        } else if (numero<20){
            System.out.println("Es mayor a 20");
        }
        for (int i=0; i<10; i++){
            System.out.println(i);
        }
        int i =9;
        while (i>=0){
            System.out.println(i);
            i--;
        }  

    }
    
}
