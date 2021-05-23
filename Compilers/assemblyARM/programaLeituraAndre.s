.global _start  

_start:
    MOV R0, #0               @Input from the keyboard
    MOV R7, #3               @Syscall to read  
    LDR R1, =user_input      @Load string to register 1
    LDR R2, =len_user_input  @Load the number of caracter to be read
    SWI 0                    @Soft. interruption 0 
_print_msg:
    MOV R0, #1               @Output to the monitor
    MOV R7, #4               @Syscall to write  
    LDR R1, =msg             @Load string to register 1
    LDR R2, =len_msg         @Load the caracter length to be printed 
    SWI 0
_print_user_input:
    MOV R0, #1               @Output to the monitor
    MOV R7, #4               @Syscall to write  
    LDR R1, =user_input      @Load string to register 1
    LDR R2, =len_user_input  @Load the caracter length to be printed 
    SWI 0
_end:
    MOV R7, #1               @Terminate the current process
    SWI 0
.data
  user_input: .ascii "                           "
  len_user_input = .-user_input
  msg: .ascii "\nSeja bem vindo a corretora MicoLeaoDourado, "
  len_msg = .-msg