#include<xc.h>           // processor SFR definitions
#include<sys/attribs.h>  // __ISR macro
#include<math.h>
#include<string.h>
#include<stdio.h>
#include<stdlib.h>
#include "spi.h"

// DEVCFG0
#pragma config DEBUG = OFF // disable debugging
#pragma config JTAGEN = OFF // disable jtag
#pragma config ICESEL = ICS_PGx1 // use PGED1 and PGEC1
#pragma config PWP = OFF // disable flash write protect
#pragma config BWP = OFF // disable boot write protect
#pragma config CP = OFF // disable code protect

// DEVCFG1
#pragma config FNOSC = PRIPLL // use primary oscillator with pll
#pragma config FSOSCEN = OFF // disable secondary oscillator
#pragma config IESO = OFF // disable switching clocks
#pragma config POSCMOD = HS // high speed crystal mode
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

void setVoltage(char, unsigned short);

int main() {

    __builtin_disable_interrupts();

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
    LATAbits.LATA4 = 1;

    __builtin_enable_interrupts();
    
    init_spi();
    int i = 0, x = 0, slope = 0;
    float m = 10.23;
    
    while(1) {
        _CP0_SET_COUNT(0);      // Setting Core Timer count to 0
        float triangle = slope*m*x;
        x++;
        setVoltage(1, triangle);
        if(x<=100) {
            slope = 1;
        }
        else if(x<=200) {
            slope = -1;
        }
        else {
            x = 0;
        }
        
        float sine = 512 + 512 * sin(i*2*3.1415/1000*10);
        i++;
        setVoltage(0, sine);
        while(_CP0_GET_COUNT() < 24000) {}  // wait 1000 times a second
    }
    return 0;
}

void setVoltage(char a, unsigned short v) {
	unsigned short t = 0;
	t= a << 15; //a is at the very end of the data transfer
	t = t | 0b0111000000000000;
	t = t | ((v&0b1111111111) <<2); //rejecting excessive bits (above 10)
	
	CS = 0;
	spi_io(t>>8);
	spi_io(t);
    CS = 1;
}
