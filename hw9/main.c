#include<xc.h>           // processor SFR definitions
#include<sys/attribs.h>  // __ISR macro

#include <stdio.h>

#include "spi.h"
#include "uart.h"
#include "font.h"
#include "ST7789.h"

// DEVCFG0
#pragma config DEBUG = OFF // disable debugging
#pragma config JTAGEN = OFF // disable jtag
#pragma config ICESEL = ICS_PGx1 // use PGED1 and PGEC1
#pragma config PWP = OFF // disable flash write protect
#pragma config BWP = OFF // disable boot write protect
#pragma config CP = OFF // disable code protect

// DEVCFG1

// no crystal:
// FNOSC = FRCPLL
// POSCMOD = OFF

#pragma config FNOSC = FRCPLL // use internal oscillator with pll
#pragma config FSOSCEN = OFF // disable secondary oscillator
#pragma config IESO = OFF // disable switching clocks
#pragma config POSCMOD = OFF // internal RC
#pragma config OSCIOFNC = OFF // disable clock output
#pragma config FPBDIV = DIV_1 // divide sysclk freq by 1 for peripheral bus clock
#pragma config FCKSM = CSDCMD // disable clock switch and FSCM
#pragma config WDTPS = PS1048576 // use largest wdt
#pragma config WINDIS = OFF // use non-window mode wdt
#pragma config FWDTEN = OFF // wdt disabled
#pragma config FWDTWINSZ = WINSZ_25 // wdt window at 25%

// DEVCFG2 - get the sysclk clock to 48MHz from the 8MHz crystal
#pragma config FPLLIDIV = DIV_2 // divide input clock to be in range 4-5MHz
#pragma config FPLLMUL = MUL_24 // multiply clock after FPLLIDIV
#pragma config FPLLODIV = DIV_2 // divide clock after FPLLMUL to get 48MHz

// DEVCFG3
#pragma config USERID = 0 // some 16bit userid, doesn't matter what
#pragma config PMDL1WAY = OFF // allow multiple reconfigurations
#pragma config IOL1WAY = OFF // allow multiple reconfigurations

int main() {

    __builtin_disable_interrupts(); // disable interrupts while initializing things

    // set the CP0 CONFIG register to indicate that kseg0 is cacheable (0x3)
    __builtin_mtc0(_CP0_CONFIG, _CP0_CONFIG_SELECT, 0xa4210583);

    // 0 data RAM access wait states
    BMXCONbits.BMXWSDRM = 0x0;

    // enable multi vector interrupts
    INTCONbits.MVEC = 0x1;

    // disable JTAG to get pins back
    DDPCONbits.JTAGEN = 0;

    // do your TRIS and LAT commands here
    TRISBbits.TRISB4 = 1;
    TRISAbits.TRISA4 = 0;
    LATAbits.LATA4 = 0;
    
    initUART();
  
  initSPI();
  LCD_init();
  LCD_clearScreen(BLACK);
  
  int x = 10, y = 10,z=0;

    __builtin_enable_interrupts();
    
    char m[100];

    while (1) {
        /*
        LATAbits.LATA4 = 1;
        _CP0_SET_COUNT(0);
        while (_CP0_GET_COUNT() < 48000000/2/2) {}
        LCD_clearScreen(BLUE);
        
        LATAbits.LATA4 = 0;
        _CP0_SET_COUNT(0);
        while (_CP0_GET_COUNT() < 48000000/2/2) {}
        LCD_clearScreen(RED);
         * */
        
        _CP0_SET_COUNT(0);
        z++;
        if(z==100){
            z = 0;
        }
        char message[100];
        sprintf(message,"hello world %d   ", z);
        drawString(28,32,message);
        
        
        for(x=10;x<10+z;x++){
            for(y=44;y<49;y++){
                LCD_drawPixel(x,y,BLUE);
            }
        }
        for(x=10+z;x<110;x++){
            for(y=44;y<49;y++){
                LCD_drawPixel(x,y,YELLOW);
            }
        }
        int time = _CP0_GET_COUNT();
        while(_CP0_GET_COUNT()<24000000/30){}
        
        sprintf(message,"FPS = %5.2f   ",1.0/((float)time/24000000.0));
        drawString(10,100,message);
    }
}
