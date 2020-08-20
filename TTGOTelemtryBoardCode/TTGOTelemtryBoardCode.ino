// -!- C++ -!- //////////////////////////////////////////////////////////////
//
//  System        : 
//  Module        : 
//  Object Name   : $RCSfile$
//  Revision      : $Revision$
//  Date          : $Date$
//  Author        : $Author$
//  Created By    : Robert Heller
//  Created       : Sun Aug 9 10:54:30 2020
//  Last Modified : <200809.1512>
//
//  Description	
//
//  Notes
//
//  History
//	
/////////////////////////////////////////////////////////////////////////////
//
//    Copyright (C) 2020  Robert Heller D/B/A Deepwoods Software
//			51 Locke Hill Road
//			Wendell, MA 01379-9728
//
//    This program is free software; you can redistribute it and/or modify
//    it under the terms of the GNU General Public License as published by
//    the Free Software Foundation; either version 2 of the License, or
//    (at your option) any later version.
//
//    This program is distributed in the hope that it will be useful,
//    but WITHOUT ANY WARRANTY; without even the implied warranty of
//    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//    GNU General Public License for more details.
//
//    You should have received a copy of the GNU General Public License
//    along with this program; if not, write to the Free Software
//    Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
//
// 
//
//////////////////////////////////////////////////////////////////////////////

#include <Arduino.h>
#include <Adafruit_ADXL345_U.h>
#include <Adafruit_MPL3115A2.h>
#include <uEEPROMLib.h>
#include <uRTCLib.h>
#include <sd_diskio.h>
#include <sd_defines.h>
#include <SD.h>
#include "SerialCLI.h"

static const char rcsid[] = "@(#) : $Id$";

SerialCLI Command;
Adafruit_ADXL345_Unified accel = Adafruit_ADXL345_Unified(1);
Adafruit_MPL3115A2 baro = Adafruit_MPL3115A2();

void setup() {
    // put your setup code here, to run once:
    Serial.begin(115200);
    if(!SD.begin()) {
        Serial.println("Card Mount Failed");
        return;
    }
    uint8_t cardType = SD.cardType();
    if(cardType == CARD_NONE) {
        Serial.println("No SD card attached");
        return;
    }
    Serial.print("SD Card Type: ");
    if(cardType == CARD_MMC) {
        Serial.println("MMC");
    } else if(cardType == CARD_SD) {
        Serial.println("SDSC");
    } else if(cardType == CARD_SDHC) {
        Serial.println("SDHC");
    } else {
        Serial.println("UNKNOWN");
    }
    
    uint64_t cardSize = SD.cardSize() / (1024 * 1024);
    Serial.printf("SD Card Size: %lluMB\n", cardSize);
    
    if (!accel.begin()) {
        Serial.println("Ooops, no ADXL345 detected ... Check your wiring!");
        return;
    }
    
    accel.setRange(ADXL345_RANGE_16_G); // +/- 16gs
    
    if (! baro.begin()) {
        Serial.println("Couldnt find sensor");
        return;
    }
    
    Serial.println("TTGO Telemtry Board 0.0");
    Serial.print(">>");
    Serial.flush();
        
}
                
void loop() {
    sensors_event_t accelevent;
    // put your main code here, to run repeatedly:
    Command.ProcessCommandLine();
    
    accel.getEvent(&accelevent);
    
    float pascals = baro.getPressure();
    float altm = baro.getAltitude();
    float tempC = baro.getTemperature();
    
    Command.LogData(accelevent.acceleration.x,accelevent.acceleration.y,\
                    accelevent.acceleration.z,pascals,altm,tempC);
    delay(1000);
}    
