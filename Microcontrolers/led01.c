//#include <01led.h>

#include <16F877A.h>
#device ADC=8

                   //No Watch Dog Timer
#FUSES HS                       //High speed OSC (>4mhz for PCM/PCH) (>10mhz for PCD)
#FUSES NOPUT                    //No Power Up Timer
#FUSES NOPROTECT                //Code not Protected from reading
#FUSES NODEBUG                  //No Debug mode for ICD
#FUSES BROWNOUT                 //Reset when brownout  detected
#FUSES NOLVP                    //No low voltage prgming, B3(PIC16) or B5(PIC18) used for I/O
#FUSES NOCPD                    //No EE protection
#FUSES NOWRT                    //Program memory not write protected

#use delay(crystal=20000000)



void main()
{

   setup_adc_ports(NO_ANALOGS);
   setup_adc(ADC_OFF);
   setup_psp(PSP_DISABLED);
   setup_spi(SPI_SS_DISABLED);
   setup_timer_0(RTCC_INTERNAL|RTCC_DIV_1);
   setup_timer_1(T1_DISABLED);
   setup_timer_2(T2_DISABLED,0,1);
   setup_comparator(NC_NC_NC_NC);
   setup_vref(FALSE);
   
  //  void turn_on_off_led(int timeMs, int pinNum, char pinLetter){

  //     char pinName[15];
  //     strcpy(pinName, "Pin_");
  //     strcat(pinName, pinLetter);

  //     strcat(pinName, pinNum);

  //    output_high(pinName );
  //    delay_ms( timeMs );
  //    output_low( pinName );
  //    delay_ms( timeMs );
  //  }
   
    while(true){
    //Reset LEDs to LOW
     output_low(PIN_D0);
     output_low(PIN_D1);
     output_low(PIN_D2);
     output_low(PIN_D3);
     output_low(PIN_D4);
     output_low(PIN_D5);
     output_low(PIN_D6);
     output_low(PIN_D7);
    //----------------



     output_high(PIN_D0);
     delay_ms( 1000 );//1 sec (1000 milsec)
     output_low(PIN_D0);
     delay_ms( 1000 );//1 sec (1000 milsec)

     output_high(PIN_D4);
     delay_ms( 1000 );//1 sec (1000 milsec)
     output_low(PIN_D4);
     delay_ms( 1000 );//1 sec (1000 milsec)

     output_high(PIN_D7);
     delay_ms( 1000 );//1 sec (1000 milsec)
     output_low(PIN_D7);
     delay_ms( 1000 );//1 sec (1000 milsec)

    //----------------
     output_high(PIN_D0);
     delay_ms( 600 );//1 sec (1000 milsec)
     output_low(PIN_D0);
     delay_ms( 600 );//1 sec (1000 milsec)

     output_high(PIN_D1);
     delay_ms( 600 );//1 sec (1000 milsec)
     output_low(PIN_D1);
     delay_ms( 600 );//1 sec (1000 milsec)

     output_high(PIN_D2);
     delay_ms( 600 );//1 sec (1000 milsec)
     output_low(PIN_D2);
     delay_ms( 600 );//1 sec (1000 milsec)

     output_high(PIN_D3);
     delay_ms( 600 );//1 sec (1000 milsec)
     output_low(PIN_D3);
     delay_ms( 600 );//1 sec (1000 milsec)

     output_high(PIN_D6);
     delay_ms( 650 );//1 sec (1000 milsec)
     output_low(PIN_D6);
     delay_ms( 300 );//1 sec (1000 milsec)

     output_high(PIN_D6);
     delay_ms( 200 );//1 sec (1000 milsec)
     output_low(PIN_D6);
     delay_ms( 650 );//1 sec (1000 milsec)

    //----------------
     output_high(PIN_D7);
     delay_ms( 547 );
     output_low(PIN_D7);
     delay_ms( 123 );

     output_high(PIN_D6);
     delay_ms( 750 );
     output_low(PIN_D6);
     delay_ms( 750 );
     
     output_high(PIN_D4);
     delay_ms( 750 );
     output_low(PIN_D4);
     delay_ms( 750 );

    //----------------

     output_high(PIN_D4);
     delay_ms( 500 );
     output_low(PIN_D4);
     delay_ms( 500 );

     output_high(PIN_D6);
     delay_ms( 800 );
     output_low(PIN_D6);
     delay_ms( 800 );

     output_high(PIN_D4);
     delay_ms( 500 );
     output_low(PIN_D4);
     delay_ms( 500 );

     output_high(PIN_D1);
     delay_ms( 800 );
     output_low(PIN_D1);
     delay_ms( 800 );

     output_high(PIN_D2);
     delay_ms( 800 );
     output_low(PIN_D2);
     delay_ms( 800 );
     
     output_high(PIN_D5);
     delay_ms( 800 );
     output_low(PIN_D5);
     delay_ms( 800 );
    //----------------
     output_high(PIN_D0);
     delay_ms( 300 );
     output_high(PIN_D1);
     delay_ms( 300 );
     output_high(PIN_D2);
     delay_ms( 300 );
     output_high(PIN_D3);
     delay_ms( 300 );
     output_high(PIN_D4);
     delay_ms( 300 );
     output_high(PIN_D5);
     delay_ms( 300 );
     output_high(PIN_D6);
     delay_ms( 300 );
     output_high(PIN_D7);
     delay_ms( 300 );
    //----------------

     output_low(PIN_D0);
     delay_ms( 300 );
     output_low(PIN_D1);
     delay_ms( 300 );
     output_low(PIN_D2);
     delay_ms( 300 );
     output_low(PIN_D3);
     delay_ms( 300 );
     output_low(PIN_D4);
     delay_ms( 300 );
     output_low(PIN_D5);
     delay_ms( 300 );
     output_low(PIN_D6);
     delay_ms( 300 );
     output_low(PIN_D7);
     delay_ms( 300 );


   }


}