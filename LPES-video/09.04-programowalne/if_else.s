	.file	"a.c"
	.text
	.section	.rodata
.LC0:
	.string	"A"
.LC1:
	.string	"B"
.LC2:
	.string	"C"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movl	%edi, -4(%rbp)

# operacja porównania
	cmpl	$1, -4(%rbp)
# skok jeżeli nie równe do bloku else
	jne	.L2
# odłożenie argumentu "A" na stos i wywołanie funkcji puts
	leaq	.LC0(%rip), %rdi
	call	puts@PLT
# skok bezwarunkowy za blok if - else
	jmp	.L3
.L2:
# blok else, odłożenie argumentu "B" na stos i wywołanie funkcji puts
	leaq	.LC1(%rip), %rdi
	call	puts@PLT
.L3:
# kod po if - else, odłożenie argumentu "C" na stos i wywołanie funkcji puts
	leaq	.LC2(%rip), %rdi
	call	puts@PLT

	movl	$0, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Debian 8.3.0-6) 8.3.0"
	.section	.note.GNU-stack,"",@progbits
