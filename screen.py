class screen:
    def __init__(self):
        #Uint16 sdata[13];
        #sdata[0] = "40";       //display start line at 0
        #sdata[1] = "A1";       //set SEG to bottom view
        #sdata[2] = "C0";       //set normal direction com0-com63
        #sdata[3] = "A4";       //set all pixels off
        #sdata[4] = "A6";       //set inverse display off
        #sdata[5] = "A2";       //set bias 1/9 (duty 1/65)
        #sdata[6] = "2F";       //set power control, booster, regulator and follower on
        #sdata[7] = "27";       //set contrast
        #sdata[8] = "81";
        #sdata[9] = "10";
        #sdata[10] = "FA";       //set temperature compensation curve to -0.11 %/C
        #sdata[11] = "90";
        #sdata[12] = "AF";       //set display on
        
        # for(i = 0; i < 13; i++)
        #{
        #   // Transmit data
        #   spi_xmit(sdata[i]);
        #   // Wait until data is received
        #   while(SpiaRegs.SPIFFRX.bit.RXFFST !=1) { }
        #   // Check against sent data
        #   rdata = SpiaRegs.SPIRXBUF;
        #   if(rdata != sdata[i]) error();
        #}
        pass
    
    