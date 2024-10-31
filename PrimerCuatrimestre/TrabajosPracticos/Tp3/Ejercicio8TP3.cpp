/* Hacer un programa en C++, que solicite al usuario que ingrese una fecha y calcule el
día correspondiente del año. Ejemplo, si se ingresa la fecha 31 12, el número que se
visualizará será 365. (la fecha se debe ingresar en dos variables diferentes: dia y mes).*/

#include <iostream>
using namespace std;

int main(){
    int Total, Dia, Mes, Biciesto, Enero, Febrero, Marzo, Abril, Mayo, Junio, Julio, Agosto, Septiembre, Octubre, Noviembre;
    Enero=31;
    Febrero=28;
    Marzo=30;
    Abril=31;
    Mayo=31;
    Junio=30;
    Julio=31;
    Agosto=31;
    Septiembre=30;
    Octubre=31;
    Noviembre=30;
    

    cout << "¿Cuantos dias tiene febrero?\n";
    cin >> Biciesto;
    cout << "Dame un dia\n";
    cin >> Dia;
    cout << "Dame un mes\n";
    cin >> Mes;

    if (Mes == 1){
        Total = Dia;
    }else{
        if (Mes == 2){
            Total = Enero + Dia; 
        }else{
            if (Mes == 3){
                Total = Enero + Febrero + Dia;
            }else{
                if (Mes == 4){
                    Total = Enero + Febrero + Marzo + Dia;
                }else{
                    if (Mes == 5){
                        Total = Enero + Febrero + Abril + Marzo + Dia;
                    }else{
                        if (Mes == 6){
                            Total = Enero + Febrero + Marzo + Abril + Mayo + Dia;
                        }else{
                            if (Mes == 7){
                                Total = Enero + Febrero + Marzo + Abril + Mayo + Junio + Dia;
                            }else{
                                if (Mes == 8){
                                    Total = Enero + Febrero + Marzo + Abril + Mayo + Junio + Julio + Dia;
                                }else{
                                    if (Mes == 9){
                                        Total = Enero + Febrero + Marzo + Abril + Mayo + Junio + Julio + Agosto + Dia;
                                    }else{
                                    if (Mes == 10){
                                        Total = Enero + Febrero + Marzo + Abril + Mayo + Junio + Julio + Agosto + Septiembre + Dia;
                                    }else{
                                        if (Mes == 11){
                                          Total = Enero + Febrero + Marzo + Abril + Mayo + Junio + Julio + Agosto + Septiembre + Octubre + Dia;
                                        }else{
                                            Total = Enero + Febrero + Marzo + Abril + Mayo + Junio + Julio + Agosto + Septiembre + Octubre + Noviembre + Dia;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            } 
        }
    }
}
 

 if (Biciesto==29 && Mes>2){
    Total = Total + 1;
    cout << "La cantidad de dias es " << Total;
 }else{
    cout << "La cantidad de dias es " << Total;
 }

}