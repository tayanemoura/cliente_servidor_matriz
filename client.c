#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h>

// socket(),connect(), send(), recv(), close()

int main(void) {


	int sock;
	struct sockaddr_in server_addr;
	char recvBuffer[1024];


	//PF_INET = IPv4
	sock = socket(PF_INET, SOCK_STREAM, 0);	

	memset(&server_addr, 0, sizeof(server_addr));
	server_addr.sin_family = AF_INET;
	server_addr.sin_port = htons(3000);
	server_addr.sin_addr.s_addr = inet_addr("127.0.0.1");

	connect(sock, (struct sockaddr *) &server_addr, sizeof(server_addr)); 

	recv(sock, recvBuffer, 1024, 0);

	printf("%s", recvBuffer );
	

	close(sock);
}