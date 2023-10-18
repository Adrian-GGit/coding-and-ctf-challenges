#include <stdio.h>
#include <stdlib.h>

// gcc -no-pie -fno-stack-protector -o level3 level3.c

char BINSH[8] = "/bin/sh";

void win() {
	execve(&BINSH, NULL, NULL);
}

int main() {
	char buf[0xff];
	fgets(buf, 0xff, stdin);

	BINSH[0] = 0;
	printf(buf);
	
	fgets(buf, 0x110, stdin);
	return 0;
}
