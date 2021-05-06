.global _start

_start:
    MOV R7, #4
    MOV R0, #1
    LDR R1, =string
    MOV R2, =len_string
    SWI 0

_end:
    MOV R7, #1
    SWI 0

_data
  string: .ascii "Voce esta sendo vigiado(a) !\n"
  len_string = .-string