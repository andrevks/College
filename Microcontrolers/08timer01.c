//#include <08timer01.h>

/*
   -  Aluno:André Geraldo, Eng. da Computação (7º semestre).
   -  Professor Dr. Alberto Willian Mascarenhas.
   
   -  Disciplina: Microcontroladores.
   
   -  Objetivo: Crie um programa para o PIC16F877A para que os 3 LEDs (1, 2 e 3) conectados na porta D (D0, D1
      e D2) respectivamente, liguem e desliguem com frequências iguais Na (50), Nb(280) e Nc(700) Hertz
      
   - Data: 14/09/2021
*/
#include <16F877A.h>
#device ADC=16

#FUSES NOWDT                    //No Watch Dog Timer
#FUSES NOBROWNOUT               //No brownout reset
#FUSES NOLVP                    //No low voltage prgming, B3(PIC16) or B5(PIC18) used for I/O

#use delay(crystal=20000000)

unsigned int16 count[3] = {0, 0, 0}; 


#INT_RTCC
void  RTCC_isr(void) 
{
  /*
      Para chegar aos valores foi preciso pegar as frequências dadas e converter-las 
      em período.
      
      Por exemplo, Na = 50 então Ta = 1/50 => Ta = 20ms
      
      - Depois tem que lembrar que só a metade do período que é mantido ligado.
      - Deve-se considerar que o tempo de overflow de 13.1ms.
      - Overflow = 0.2us * 256 * DIV  | No caso o DIV aqui é 256
      - O count então varia de acordo com o overflow
      - Count = (T/2)*1000/OVF
      
   */

   if( ++count[0] >= 763){
      output_toggle(PIN_D0);
      count[0] = 0;
   }
  
   if( ++count[1] >= 136){
      output_toggle(PIN_D1);
       count[1] = 0;
   } 
   
   if( ++count[2] >= 55){
      output_toggle(PIN_D2);
       count[2] = 0;
   }
   
   
}

void main()
{
   setup_timer_0(RTCC_INTERNAL|RTCC_DIV_256|RTCC_8_bit);      //13.1 ms overflow


   enable_interrupts(INT_RTCC);
   enable_interrupts(GLOBAL);

   while(TRUE)
   {
      
   }

}
