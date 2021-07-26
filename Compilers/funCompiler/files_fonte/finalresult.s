.global main 
.func main 
main: 
LDR R1, =backup_lr @Address of the var 
STR LR, [R1]  @Store LinkRegister in var 
@------BEGIN--------

LDR R0, =string0 @Send variable address
BL printf  @Function to receive input from the keyboard

LDR R0, =pattern @int pattern (%d)
LDR R1, =taxas @Send variable address
BL scanf  @Function to receive input from the keyboard

@CONDITION
LDR R1,=taxas @Send address to the R1
LDR R2, [R1] @Move value from R2 to var location
MOV R3, R2  @Send end result to R3
MOV R2, #123 @Move value to the R2
CMP R3, R2  @Compare R3 and R2, changes flags status
@END-CONDITION
BLT _se0  @Jumps if R3 < R1
B _senao1 @Jumps unconditionally (R3 == R1)
_se0: @add symbol after expr
LDR R0, =string1 @Send variable address
BL printf  @Function to receive input from the keyboard

B _fim_se2 @Jumps unconditionally
_senao1: @add symbol after expr
LDR R0, =string2 @Send variable address
BL printf  @Function to receive input from the keyboard

_fim_se2: 
@CONDITION
LDR R1,=taxas @Send address to the R1
LDR R2, [R1] @Move value from R2 to var location
MOV R3, R2  @Send end result to R3
MOV R2, #123 @Move value to the R2
CMP R3, R2  @Compare R3 and R2, changes flags status
@END-CONDITION
BGT _se3  @Jumps if R3 > R1 (Zero is set)
B _senao4 @Jumps unconditionally 
_se3: @add symbol after expr
LDR R0, =string3 @Send variable address
BL printf  @Function to receive input from the keyboard

_senao4: 
@CONDITION
LDR R1,=taxas @Send address to the R1
LDR R2, [R1] @Move value from R2 to var location
MOV R3, R2  @Send end result to R3
MOV R2, #123 @Move value to the R2
CMP R3, R2  @Compare R3 and R2, changes flags status
@END-CONDITION
BEQ _se5  @Jumps if R3 == R1 (Zero is set)
B _senao6 @Jumps unconditionally (R3 <> R1)
_se5: @add symbol after expr
LDR R0, =string4 @Send variable address
BL printf  @Function to receive input from the keyboard

_senao6: 
@CONDITION
LDR R1,=taxas @Send address to the R1
LDR R2, [R1] @Move value from R2 to var location
MOV R3, R2  @Send end result to R3
MOV R2, #123 @Move value to the R2
CMP R3, R2  @Compare R3 and R2, changes flags status
@END-CONDITION
BNE _se7  @Jumps if R3 > R1 (Zero is not set)
B _senao8 @Jumps unconditionally 
_se7: @add symbol after expr
LDR R0, =string5 @Send variable address
BL printf  @Function to receive input from the keyboard

_senao8: 
@------END--------
LDR LR, =backup_lr @Address of the var 
LDR LR, [LR] 
BX LR @Return from the main function

.data @ Data section
.balign 8 @Bytes allocated to each var
pattern: .asciz "%d" @Int format
pattern_print: .asciz "%d\n" 
backup_lr: .word 0
 

.global printf 
.global scanf 
taxas: .word 0 
dinheiro: .word 0 
string0: .asciz "Digite o valor da taxa\n"  
string1: .asciz "EH MENOR \n"  
string2: .asciz "Passou no ELSE \n"  
string3: .asciz "EH MAIOR \n"  
string4: .asciz "EH IGUAL \n"  
string5: .asciz "EH DIFF \n"  
