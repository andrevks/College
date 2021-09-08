//#include <04display7seg03.h>

/*

   -  Aluno:André Geraldo, Eng. da Computação (7º semestre).

   -  Professor Dr. Alberto Willian Mascarenhas.
   
   -  Disciplina: Microcontroladores.
   
   -  Objetivo: construir um contador decimal com PICSimLab configurado com a placa McLab1-PIC16F628A. 
      O contador vai de 0 a 99 com um delay de 390ms.
      
   - Data: 08/09/2021


*/
#include <16F628.h>

#FUSES NOWDT                    //No Watch Dog Timer
#FUSES NOBROWNOUT               //No brownout reset
#FUSES NOLVP                    //No low voltage prgming, B3(PIC16) or B5(PIC18) used for I/O

#use delay(crystal=4000000)

#define DELAY 5

byte const unidade[11]={
    0b11111110,  //0
    0b00111000,  //1
    0b11011101, //2
    0b01111101, //3
    0b00111011, //4
    0b01110111, //5
    0b11110111, //6
    0b00111100, //7
    0b11111111, //8
    0b00111111, //9
    
};

byte const dezena[11]={
    0b11101110,  //0
    0b00101000,  //1
    0b11001101, //2
    0b01101101, //3
    0b00101011, //4
    0b01100111, //5
    0b11100111, //6
    0b00101100, //7
    0b11101111, //8
    0b00101111, //9
};


void main()
{
   int count_num = 0;
   int8 d = 0;
   int8 u = 0;
   
   while(true)
   {
      if(count_num > 100){
         count_num = 0;
      }
      d = count_num / 10;
      u = count_num % 10;
      
      //A 390ms Delay
      for(int i=0; i < 39; i++){
         //Each loop takes 10ms
         //The change needs to 
         //happen after a delay of 390,
         //that's why it repeats 39 times.
         output_b(dezena[d]);
         delay_ms(DELAY);//5ms
         output_b(unidade[u]);
         delay_ms(DELAY);//5ms
      }
      
      count_num++;
 
   }

}
