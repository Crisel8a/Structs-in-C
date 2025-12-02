/*
Restaurante super exclusivo que solo atienden a 5 perosnas a la vez
1.- Crear pointer para saber que hay en front y rear
2.- Colocar estos valores en -1 al inicializar
3.- Incrementar en 1 el valor de rear cuando agreguemos un elemento
4.- Retornar el valor de front al quitar un elemento e incrementa en 1 el valor de front al usar dequeue
5.- Antes de agregar un elemento revosar si hay espacio
6.- Antes de remover un elemento revisar que existan elementos
7.- Asegurarnos de que al remover todos los elementos resetear nuestro front y rear a 1- y agregaar el valor de 0 a frony y hacer nuestro primer queue
 */
#include <stdio.h> //para imprimir
#define SIZE 5

int values[SIZE], front = -1, rear = -1;

void enQueue(int value)
{
    if (rear == SIZE - 1)
        printf("Nuestro Queue esta lleno\n");
    else {
        if (front == -1)
            front = 0;

        rear++;
        values[rear] = value;
        printf("Se incerto el valor %d correctamente\n", value);
    }
}

void deQueue()
{
    if (front == -1) //tiene que estar en cero para que exosta algo, de lo contrario esta vacia
        printf("Nuestro Queue esta vacio\n");
    else {
        printf("Se elimino el valor %d correctamente\n", values[front]);
        front++;

        if (front > rear)
            front = rear = -1; //eliminamos todo y regresamos a -1 para vaciar
    }
}

main(int argc, char const *argv[])
{
    enQueue(1);
    enQueue(2);
    enQueue(3);
    enQueue(4);
    enQueue(5);
    deQueue();
    enQueue(6);
    return 0;
}
