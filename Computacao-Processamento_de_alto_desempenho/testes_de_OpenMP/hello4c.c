#include <stdio.h>
#include <omp.h>

int main()
{
    #pragma omp parallel num_threads(5)
    {
        int id = omp_get_thread_num();
        int nt = omp_get_num_threads();
        printf("Regiao paralela 1 - thread %d - %d threads disponiveis\n", id, nt);
    }

    #pragma omp parallel
    {
        int id = omp_get_thread_num();
        int nt = omp_get_num_threads();
        printf("Regiao Paralela 2 - Thread %d - %d threads disponiveis\n", id, nt);
    }

    return 0;
}