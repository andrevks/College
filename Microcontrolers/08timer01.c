//#include <08timer01.h>

#include <16F877A.h>
#device ADC=16

#FUSES NOWDT                    //No Watch Dog Timer
#FUSES NOBROWNOUT               //No brownout reset
#FUSES NOLVP                    //No low voltage prgming, B3(PIC16) or B5(PIC18) used for I/O

#use delay(crystal=20000000)

unsigned int8 count[3] = {0, 0, 0}; 


#INT_RTCC
void  RTCC_isr(void) 
{

   if( ++count[0] >= 195){
      output_toggle(PIN_D0);
      count[0] = 0;
   }
  
   if( ++count[1] >= 35){
      output_toggle(PIN_D1);
       count[1] = 0;
   } 
   
   if( ++count[2] >= 14){
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
