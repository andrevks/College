/* 
  Author: André Geraldo | github:@Andrevks

  Disciplina: Compiladores

  Objetivo:Implemente um programa, na linguagem Assembly,
  que contenha estrutura de repetição e interação 
  (leitura e escrita) com o usuário. 


  Linguagem: Assembly Arquitetura ARM no Raspberry PI 3

  Data: 18/06/2021

  print("Digite a duas notas de cada aluno")
  R0 = 4 

  if RO > 0
    nota1 <- entradaUsuario
    nota2 <- entradaUsuario
    media <- nota1/nota2
    RO = RO - 1
  }
*/
.global _start

_start:
  MOV R1, #0
  MOV R2, #1

_print_msg:
    MOV R0, #1               @Output to the monitor
    MOV R7, #4               @Syscall to write  
    LDR R1, =msg             @Load string to register 1
    LDR R2, =len_msg         @Load the caracter length to be printed 
    SWI 0

_while:
  CMP R2, #5
  BGT _endwhile
  _input
  _backinput
  _print_user_input
  _backprint
  ADD R2, R2, #1
  B _while

_input:
  MOV R0, #0               @Input from the keyboard
  MOV R7, #3               @Syscall to read  
  LDR R1, =user_input      @Load string to register 1
  LDR R2, =len_user_input  @Load the number of caracter to be read
  SWI 0                    @Soft. interruption 0 
  B _backinput

_print_user_input:
    MOV R0, #1               @Output to the monitor
    MOV R7, #4               @Syscall to write  
    LDR R1, =user_input      @Load string to register 1
    LDR R2, =len_user_input  @Load the caracter length to be printed 
    SWI 0
  B _backprint

_endwhile:
  MOV R7, #1               @Terminate the current process
  SWI 0

.data
  user_input: .ascii "                  \n"
  len_user_input = .-user_input
  msg: .ascii "\nDigite o nome dos alunos"
  len_msg = .-msg