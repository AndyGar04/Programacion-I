#include <iostream>
#include <string>
using namespace std;

struct Libro {
    string titulo, autor;
    int FechaPublicacion;
};

Libro listaLibros[3];

//• agregarLibro: Esta función recibe por parámetro los datos de un libro (título, autor y
//año de publicación) y agrega un nuevo libro a la lista de libros.

void agregarLibro(string tit, string au, int publicacion, int nLibro) {
    listaLibros[nLibro].titulo = tit;
    listaLibros[nLibro].autor = au;
    listaLibros[nLibro].FechaPublicacion = publicacion;
}

//• buscarLibroPorAutor: Esta función recibe por parámetro el nombre de un autor y busca
//todos los libros de la lista que coincidan con ese autor. Devuelve una lista de libros que
//cumplen con la condición.

void buscarLibroPorAutor(Libro arr[], int cant, string nombre){
    for(int i=0; i<cant; i++){
        if (nombre==arr[i].autor){
            cout<<arr[i].titulo;
        }
    }
}

//• mostrarLibros: Esta función muestra en pantalla todos los libros de la lista, uno por línea.
//Utiliza una estructura llamada Libro para representar los datos de cada libro.

void mostrarLibros() {
    for (int i = 0; i < 3; i++) {
        cout << "Libro numero " << i + 1 << ", su autor es " << listaLibros[i].autor << ", su titulo es " << listaLibros[i].titulo << ", salio a la venta en " << listaLibros[i].FechaPublicacion << endl;
    }
}

int main() {
    string titulo, autor;
    int aSalida;
    cout << "Preparece para cargar libros" << endl;
    for (int i = 0; i < 3; i++) {
        cout << "Cual es el titulo del libro " << i + 1 << endl;
        cin >> titulo;
        cout << "Cual es el autor del libro " << i + 1 << endl;
        cin >> autor;
        cout << "En que anio salio el libro " << i + 1 << endl;
        cin >> aSalida;
        agregarLibro(titulo, autor, aSalida, i);
    }
    mostrarLibros();

    string UnAutor;
    
    cout << "Introduzca un autor"<<endl;
    cin >> UnAutor;
    buscarLibroPorAutor(listaLibros, 3, UnAutor);

}
