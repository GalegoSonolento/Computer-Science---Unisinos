#include <stdio.h>
#include <omp.h>

int main()
{
    #pragma omp parallel sections nowait
    {
        int id = omp_get_thread_num();

        #pragma omp section
        printf("Section 1 - Thread %d\n", id);

        #pragma omp section
        printf("Section 2 - Thread %d\n", id);

        #pragma omp section
        printf("Section 3 - Thread %d\n", id);
    }
    return 0;
}