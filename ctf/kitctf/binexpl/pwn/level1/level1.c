#include <stdio.h>
#include <stdlib.h>

// gcc -no-pie -fno-stack-protector -o level1 level1.c

void win() {
	execve("/bin/sh", NULL, NULL);
}


int main() {
	char buf[0xff];
	gets(buf);
	puts(buf);
	return 0;
}
