#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h>
#include <pthread.h> 
#include <stdio.h>

#include <unistd.h>
#include <stdlib.h>
#include <errno.h>
#include <fcntl.h>

 #include <sys/types.h>
 #include <sys/socket.h>
 #include <sys/uio.h>

// socket(), bind(), listen(), accept(), recv(), send(), close(), close()

void* read_client(void* arg){
	char buffer[1024];
	int connection = *(int *) arg;
	while(1){
		recv(connection, buffer, 1024, 0);
		//int send(int sockfd, const void *msg, int len, int flags); 
		printf("%s", buffer );
		if(strcmp(buffer,"EOF\n") != 0){
			break;
		}
	}
	close(connection);
}

int main(void) {


	int sock;
	struct sockaddr_in server_addr;
	


	//PF_INET = IPv4
	sock = socket(PF_INET, SOCK_STREAM, 0);	

	if(sock<0){
		perror("Erro na criação do socket");
	}

	memset(&server_addr, 0, sizeof(server_addr));
	server_addr.sin_family = AF_INET;
	server_addr.sin_port = htons(3000);
	server_addr.sin_addr.s_addr = inet_addr("127.0.0.1");
	
	

	if(bind(sock, (struct sockaddr *) &server_addr, sizeof(server_addr))<0){
		perror("bind - error");
		exit(1);
	} 

	if(listen(sock, 10) != 0){
		perror("listen - error");
		exit(2);
	}

	printf("%s\n","Esperando conexões...");

	while (1){
		int connection;
		struct sockaddr_in client_addr;
		socklen_t client_size = sizeof(client_addr);

		pthread_t thread;
		connection = accept(sock, (struct sockaddr *) &client_addr, &client_size);
		if(connection == -1){
			perror("Server - erro de conexão ");
		}
		pthread_create(&thread, NULL, read_client, &connection );

	}

	close(sock);
}