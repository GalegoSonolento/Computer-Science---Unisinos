#include <stdio.h>
#include <omp.h>
#include <math.h>
#include <stdlib.h>

int* inicializa(int size);

int* inicializa(int size)
{
    int* vector = malloc(size * sizeof(int));
    for (int i=0; i < size; i++)
    {
        vector[i] = i * 2;
    }

    return vector;
}

int main()
{
    int size = 12;

    int* vector = inicializa(size); //isso será feito sequencial

    #pragma omp parallel num_threads(3)
    {
        #pragma omp for
        for (int i=0; i < size; i++)
        {
            int id = omp_get_thread_num();
            vector[i] = (int)sqrt(vector[i]);
            printf("Thread %d - posicao %i\n", id, i);
        }
    }
    
    free(vector); // Free allocated memory
    return 0;
}