#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <stdio.h>

#define PORT 5842
#define IP 176.9.9.172

int main() {
	int sock, run;
	struct hostent *host;
	sock = socket(AF_INET, SOCK_STREAM, 0);
	host = gethostbyname("vortex.labs.overthewire.org");
	printf(host);

	return 0;
}
