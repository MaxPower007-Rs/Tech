
package code2_edades;

import java.util.Scanner;


public class Code2_Edades {
    //************* Declaracion de funciones *************
    public static int gen(String genero){
        int msg;
        if(genero.equalsIgnoreCase("H")){
           msg = 1; 
        }
        else if(genero.equalsIgnoreCase("M")){
            msg = 2;
        }else{
            msg = 3;
        }  
        return msg;
    }
    //*********************************************
    //************* Funcion principal *************
    public static void main(String[] args) {
    /*
        0 a 5 Niños pequeños
        6 a 12 Niños grandes
        13 a 17 Adolecentes
        18 a 65 Adultos
        66 a 100 Adulto mayor
    */
        Scanner opc=new Scanner(System.in);
        float edad;
        String genero;
        System.out.println("Digite la edad: ");
        edad = opc.nextFloat();
        
        // Inicia la comprobacion de la edad
        if(edad<0 || edad>100){
            System.out.println("Edad erronea, verificar. ");
        //Si la edad es correcta sigue solicitando el genero
        }else{
            System.out.println("Digite M si es mujer o H si es hombre");
            genero = opc.next();
            
            //Llama la funcion para genero
            int person = gen(genero); //1 = hombre, 2 = mujer y 3 = no definido
            
            if (person==3){
                System.out.println("Genero no binario...VERIFICAR");
            }           
            else {
                if(edad>=0){
                    if(edad <= 5){
                        if(person==1){
                            System.out.println("Es un nino pequeno");
                        }
                        else if(person==2){
                            System.out.println("Es una nina pequena");
                        }
                    }
                    else if(edad<=12){
                        if(person==1){
                            System.out.println("Es un nino grande");
                        }
                        else if(person==2){
                            System.out.println("Es una nina grande");
                        }
                    }
                    else if(edad<=17){
                        if(person==1){
                            System.out.println("Es un hombre Adolescente");
                        }
                        else if(person==2){
                            System.out.println("Es una mujer Adolescente");
                        }
                    }
                    else if(edad<=65){
                        if(person==1){
                            System.out.println("Es un hombre Adulto");
                        }
                        else if(person==2){
                            System.out.println("Es una mujer Adulta");
                        }
                    }
                    else if(edad<=100){
                        if(person==1){
                            System.out.println("Es un adulto mayor hombre");
                        }
                        else if(person==2){
                            System.out.println("Es una adulto mayor mujer");
                        }
                    }
                    
                }
            }
        }
    }
    
}
