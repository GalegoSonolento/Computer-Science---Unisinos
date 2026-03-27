#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

const int N = 100;
int V1[N], V2[N], V3[N];
int nt = 4;

void * exec( void *arg )
{
    int desloc = *(int*)arg;
    int i;

    for (i = desloc * (N/nt); i < (desloc + 1) * (N/nt); i++)
        V3[i] = V1[i] + V2[i];
    return 0;
}

int main()
{
    pthread_t p[nt];
    int i;

    for (i = 0; i < nt; i++)
        pthread_create(&p[i], NULL, exec, &i);

    for (i = 0; i < nt; i++)
        pthread_join(p[i], NULL);
    
    for (i = 0; i < N; i++)
        printf("%d ", V3[i]);
    printf("\n");

    return 0;
}