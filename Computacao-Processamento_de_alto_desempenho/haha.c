#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

void * helloworld( void *str )
{
	printf("thread %d\n", (int) pthread_self());
}

void * contagem( void *str )
{
	int aux = 0;
	while (aux < 100)
	{
		printf("cout %d\n", (int) aux);
		aux++;
	}
}

int main()
{
	pthread_t thid;
	pthread_t thid2;

	pthread_create (&thid, NULL, helloworld, NULL);
	printf("Criada thread %d\n", (int) thid);

	/*pthread_create (&thid2, NULL, contagem, NULL);
	printf("Criada a contagem da thread %d\n", (int) thid2);*/

	/*pthread_join(thid, NULL);*/
	printf("A thread %d já terminou\n", (int) thid);

	/*pthread_join(thid2, NULL);
	printf("Acabou a contagem da thread %d\n", (int) thid2);*/

	return 0;
}
