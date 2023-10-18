#include <stdio.h>
#include <stdlib.h>

// gcc -no-pie -fno-stack-protector -o level2 level2.c

void win(long long int arg1) {
	if (arg1 == 0xdeadbeefd3adc0de) {
		execve("/bin/sh", NULL, NULL);
	} else {
		exit(0);
	}
}


int main() {
	char buf[0xff];
	gets(buf);
	puts(buf);
	return 0;
}
