/*Determinar a qué signo del zodiaco pertenece una persona, cuando se ingresa separadamente el
“Día” y “Mes” de nacimiento de una persona. El resultado del signo al que pertenezca deberá ser
mostrado en la salida del terminal.*/

#include <iostream>
using namespace std;

int main(){
    int Dia, Mes;
    cout << "Dia ";
    cin >> Dia;
    cout << "Mes ";
    cin >> Mes;
   
  switch(Mes){
   case 1:
    if (Dia < 21){
         cout << "Eres Capricornio\n";
       }else{
         cout << "Eres Acuario\n";
       }
   break;
   case 2:
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
   break;
   case 3:
    if (Dia < 21){
        cout << "Eres Picis\n";
      }else{
        cout << "Eres Aries\n";
      }
   break;   
   case 4:
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
   break;
   case 5:
    if (Dia < 21){
        cout << "Eres Tauro\n";
      }else{
        cout << "Eres Geminis\n";
      }  
   break;
   case 6:
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
   break;
   case 7:
   if (Dia < 23){
        cout << "Eres Cancer\n";
      }else{
        cout << "Eres Leo\n";
      }
   break;
   case 8:
    if (Dia < 24){
        cout << "Eres Leo\n";
      }else{
        cout << "Eres Virgo\n";
      }
   break;
   case 9:
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
   break;
   case 10:
    if (Dia < 23){
        cout << "Eres Libra\n";
      }else{
        cout << "Eres Escorpio\n";
      }
   break;   
   case 11:
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
   break;
   case 12:
    if (Dia < 22){
        cout << "Eres Capricornioa\n";
      }else{
        cout << "Eres Acuario\n";
      }
   break;
   default:
    cout << "Valor invalido, reinicie el programa";
    return 0;
  }
}