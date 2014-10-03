nasm -f elf sh.asm
dd if=sh.o of=s.o bs=1 skip=272 count=73
