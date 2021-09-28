//#include <11ConversorAD.h>
#include <16F877A.h>
#device ADC=10 //10 bits 

#FUSES NOWDT                    //No Watch Dog Timer
#FUSES NOBROWNOUT               //No brownout reset
#FUSES NOLVP                    //No low voltage prgming, B3(PIC16) or B5(PIC18) used for I/O

#use delay(crystal=20000000)

void Mostra_digito(int n) {
   if(n==0) output_d(0b00111111); //0
   if(n==1) output_d(0b00000110);
   if(n==2) output_d(0b01011011);
   if(n==3) output_d(0b01001111); 
   if(n==4) output_d(0b01100110);
   if(n==5) output_d(0b01101101);
   if(n==6) output_d(0b01111101);
   if(n==7) output_d(0b00000111);
   if(n==8) output_d(0b01111111);
   if(n==9) output_d(0b01101111);
}

//Define the default pins before calling the LCD driver
#ifndef lcd_enable 
   #define lcd_enable     pin_e1
   #define lcd_rs         pin_e2
   //#define lcd_rw       pin_e2  
   #define lcd_d4         pin_d4
   #define lcd_d5         pin_d5
   #define lcd_d6         pin_d6
   #define lcd_d7         pin_d7
#endif

#include "E:\University\Microcontrollers\PCW Projects\Driver\mod_lcd.c"

void main()
{
   int n[10];
   int i, tempo;
   unsigned int8 tensao;
   unsigned int16 tensao10;
   float valor_tensao;
   setup_adc_ports(AN0); 
   setup_adc(ADC_CLOCK_DIV_16);
    
   set_adc_channel( 0 );
   delay_us( 50 );
   
   
   //LCD
   lcd_ini();
   delay_ms(50);

   while(TRUE) 
   {
      //tensao = read_adc();
      tensao10 = read_adc();
      valor_tensao = (tensao10*5)/1023.;
      
      
      printf(lcd_escreve, "\f Valor = %Lu",tensao10);
      printf(lcd_escreve, "\r\nTensao (V)= %3.2f",valor_tensao);
      tensao = tensao10/10.23; // 0 to 100
      
      if(tensao > 99)
        tensao = 99;
        
      //tensao = 36;
      
      for(tempo = 0; tempo < 10; tempo++){
      
         i = tensao/10;
         Mostra_digito(i);
         output_high(pin_A4);
         output_low(pin_A5);
         delay_ms(5);

         i = tensao%10;
         Mostra_digito(i);
         output_low(pin_A4);
         output_high(pin_A5);
         delay_ms(5);
         
      
      }
        
      
   }

}
