#include <stdio.h>
#include <omp.h>

int main()
{
    printf("--Fora da regiao paralela--\n");

    omp_set_num_threads(3);
    #pragma omp parallel
    {
        int id = omp_get_thread_num();
        int nt = omp_get_num_threads();
        printf("Regiao Paralela - Hello, World da thread %d - %d threads disponiveis\n", id, nt);
    }

    printf("--Fora da regiao paralela--\n");
    return 0;
}