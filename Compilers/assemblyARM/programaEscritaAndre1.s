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

.data
  string: .ascii "O caminho para o conhecimento eh a liberdade. - Hacker Pyron !\n"
  len_string = .-string
