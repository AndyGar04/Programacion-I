/*Determinar a qué signo del zodiaco pertenece una persona, cuando se ingresa separadamente el
“Día” y “Mes” de nacimiento de una persona. Automáticamente, el resultado del signo al que
pertenezca deberá ser mostrado como salida en la terminal de VScode.*/

#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main(){
    string Rta;
    int Dia, Mes;
    float invitados, total_invitados;
    cout << "Dia ";
    cin >> Dia;
    cout << "Mes ";
    cin >> Mes;
   
  if (Mes < 13 && Mes > 0 && Dia>0 && Dia<32){
    if (Mes == 1){
      if (Dia < 21){
        cout << "Eres Capricornio\n";
      }else{
        cout << "Eres Acuario\n";
      }
    }
    //21/01 a 19/02 Acuario
    if (Mes == 2){
     if (Dia > 29){
        cout << "Valor invalido para febrero, reinicie el programa";
        return 0;
     }else{   
      if (Dia < 20){
        cout << "Eres Acuario\n";
      }else{
        cout << "Eres Picis\n";
      }
     } 
    }
    //20/02 a 20/03 Piscis
    if (Mes == 3){
        if (Dia < 21){
        cout << "Eres Picis\n";
      }else{
        cout << "Eres Aries\n";
      }
    }
    //21/03 a 19/04 Aries
    if (Mes == 4){
     if (Dia > 30){
        cout << "Valor invalido para abril, reinicie el programa";
        return 0;
     }else{   
        if (Dia < 20){
        cout << "Eres Aries\n";
      }else{
        cout << "Eres Tauro\n";
      }
     } 
    }
    //20/04 a 20/05 Tauro
    if (Mes == 5){
        if (Dia < 21){
        cout << "Eres Tauro\n";
      }else{
        cout << "Eres Geminis\n";
      }
    }
    //21/05 a 21/06 Géminis
    if (Mes == 6){
      if (Dia > 30){
        cout << "Valor invalido para junio, reinicie el programa";
        return 0;
     }else{  
        if (Dia < 22){
        cout << "Eres Geminis\n";
      }else{
        cout << "Eres Cancer\n";
      }
     } 
    }    
    //22/06 a 22/07 Cáncer
    if (Mes == 7){
        if (Dia < 23){
        cout << "Eres Cancer\n";
      }else{
        cout << "Eres Leo\n";
      }
    }  
    //23/07 a 23/08 Leo
    if (Mes == 8){
        if (Dia < 24){
        cout << "Eres Leo\n";
      }else{
        cout << "Eres Virgo\n";
      }
    }
    //24/08 a 22/09 Virgo
    if (Mes == 9){
      if (Dia > 30){
        cout << "Valor invalido para septiembre, reinicie el programa";
        return 0;
     }else{  
        if (Dia < 25){
        cout << "Eres Virgo\n";
      }else{
        cout << "Eres Libra\n";
      }
     } 
    }
    //23/09 a 22/10 Libra
    if (Mes == 10){
        if (Dia < 23){
        cout << "Eres Libra\n";
      }else{
        cout << "Eres Escorpio\n";
      }
    }
    //23/10 a 22/11 Escorpio    
    if (Mes == 11){
      if (Dia > 30){
        cout << "Valor invalido para noviembre, reinicie el programa";
        return 0;
     }else{  
        if (Dia < 23){
        cout << "Eres Escorpio\n";
      }else{
        cout << "Eres Capricornio\n";
      }
     } 
    }
    //23/11 a 21/12 Sagitario    
    if (Mes == 12){
        if (Dia < 22){
        cout << "Eres Capricornioa\n";
      }else{
        cout << "Eres Acuario\n";
      }
    }
    //22/12 a 20/01 Capricornio
  }else{
    cout << "Valor invalido, reinicie el programa";
    return 0;
  }

   /*Una vez mostrado en terminal el signo del zodiaco, deberán preguntarle al usuario “Si le gusta
    festejar su cumpleaños”, siendo como únicas respuestas permitidas: “Si” o “No” (tengan en cuenta
    las minúsculas y mayúsculas). Automáticamente, como contestación a esta respuesta, se deberá
    mostrar en la terminal de VScode, lo siguiente:
    • Si le gusta festejar su cumpleaños entonces contestarle con un “Que Bueno!”
    • No le gusta festejar su cumpleaños entonces contestarle con un “Que Lastima.”
    • Si ingresa valores erróneos, mostrar un error, que indique que vuelva a intentar ingresando
    los valores correctos. Observación: Si hay error, se muestra el error, pero el programa
    continua con el paso siguiente.*/

    cout << "Te gusta festejar tu cumpleanios? (Responda Si o No)\n";
    cin >> Rta;

    if (Rta == "Si" || Rta == "SI" || Rta == "si" || Rta == "sI"){
        cout << "Que bueno!\n"; 
    }else if(Rta == "NO" || Rta == "no" || Rta == "No" || Rta == "nO"){
        cout << "Que lastima!\n";
    }else{
        cout << "Respuesta invalida, reinicie el programa...\n";
        return 0;
    }

    /*Finalmente, deberán preguntarle al usuario “el número de invitados a su cumpleaños”, el usuario
    deberá contestar con un “número” del tipo float el cual será almacenado en una variable llamada
    “invitados”. Mediante el uso de las funciones correctas, el valor ingresado deberá ser elevado a la
    potencia 4, luego calcularle la raíz cuadrada y redondearlo. Dando como resultado el “total de
    invitados” a su cumpleaños, dicho valor deberá ser mostrado como salida en la terminal de VScode.*/

    cout << "Cual el numero de invitados a tu cumpleanios?\n";
    cin >> invitados;
    
    total_invitados=round(sqrt(pow(invitados,4)));

    cout << "El redondeo de la raiz cuadrada de los invitados ^ 4 es " << total_invitados;

    return 0;
}
