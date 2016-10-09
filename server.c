#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h>

// socket(), bind(), listen(), accept(), recv(), send(), close(), close()

int main(void) {


	int sock;
	int connection;
	struct sockaddr_in server_addr;
	struct sockaddr_in client_addr;
	char buffer[1024];


	//PF_INET = IPv4
	sock = socket(PF_INET, SOCK_STREAM, 0);	

	memset(&server_addr, 0, sizeof(server_addr));
	server_addr.sin_family = AF_INET;
	server_addr.sin_port = htons(3000);
	server_addr.sin_addr.s_addr = inet_addr("127.0.0.1");

	bind(sock, (struct sockaddr *) &server_addr, sizeof(server_addr)); 

	listen(sock, 10); 

	while (1){

		connection = accept(sock, (struct sockaddr *) &client_addr, sizeof(client_addr));
		strcpy(buffer, "Hello World\n");
		//int send(int sockfd, const void *msg, int len, int flags); 
		send(connection, buffer, 13, 0);
		close(connection);
	}

	close(sock);
}