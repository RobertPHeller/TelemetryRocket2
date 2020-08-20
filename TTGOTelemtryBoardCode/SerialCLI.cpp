// -!- C++ -!- //////////////////////////////////////////////////////////////
//
//  System        : 
//  Module        : 
//  Object Name   : $RCSfile$
//  Revision      : $Revision$
//  Date          : $Date$
//  Author        : $Author$
//  Created By    : Robert Heller
//  Created       : Sun Aug 9 12:05:15 2020
//  Last Modified : <200809.1540>
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

static const char rcsid[] = "@(#) : $Id$";

#include <Arduino.h>
#include <uEEPROMLib.h>
#include <uRTCLib.h>
#include <sd_diskio.h>
#include <sd_defines.h>
#include <SD.h>
#include <FS.h>

#include "SerialCLI.h"

SerialCLI::SerialCLI() 
      : uRTCLib(URTCLIB_ADDRESS, URTCLIB_MODEL_DS3231)
{
}

SerialCLI::~SerialCLI()
{
}

const char *SerialCLI::HelpText[] = {
    "TTGO Telemtry Board 0.0",
    "",
    "Commands:",
    "S m/d/y h:m:s",
    "  Set clock",
    "O filename",
    "  Open new file, start collecting data",
    "C",
    "  Close file, stop collecting data",
    "H",
    "  Print this help",
    "",
    NULL
};

void SerialCLI::ProcessCommandLine()
{
    char buffer[256];
    int len;
    
    if (Serial.available() > 0) {
        len = Serial.readBytesUntil('\r',buffer,sizeof(buffer)-1);
        if (len == 0) return;
        buffer[len] = '\0';
        switch ((Commands) (toupper(buffer[0]))) {
        case SET:
            char unused;
            int month, date, year, hours, minutes, seconds;
            if (sscanf(buffer,"%c %d/%d/%d %d:%d:%d",&unused,&month,&date,
                       &year,&hours,&minutes,&seconds) != 7) {
                Serial.println("Syntax error!");
            } else {
                set(seconds,minutes,hours,URTCLIB_WEEKDAY_SUNDAY,date,month,year%100);
                Serial.println("");
                Serial.println("Clock set.");
            }
            break;
        case OPENNEW:
            {
                if (_dataLog) {_dataLog.close();}
                char *p = buffer;
                while (*p && !isspace(*p)) p++;
                while (*p && isspace(*p)) p++;
                char *filename = p;
                while (*p && !isspace(*p)) p++;
                *p = '\0';
                _dataLog = SD.open(filename,FILE_WRITE);
                Serial.println("");
                if (_dataLog) {
                    Serial.println("File opened.");
                }
            }
            break;
            case CLOSE:
                if (_dataLog) {
                    _dataLog.close();
                }
                Serial.println("");
                Serial.println("File Closed.");
            break;
        case HELP:
            {
                int i, n = sizeof(HelpText) / sizeof(HelpText[0]);
                for (i = 0; i < n && HelpText[i]; i++) {
                    Serial.println(HelpText[i]);
                }
                break;
            }
            default:
                Serial.println("");
                Serial.println("Unknown Command.");
        }
        refresh();
        uint16_t yr = year()+2000;
        byte month  = this->month();
        byte date   = day();
        byte hr     = hour();
        byte min    = minute();
        byte sec    = second();
        sprintf(buffer,"%d/%d/%d %02d:%02d:%02d",month,date,yr,hr,min,sec);
        Serial.println(buffer);
        Serial.print(">>");
        Serial.flush();
    }
}

void SerialCLI::LogData(float accel_x,float accel_y,float accel_z,
                        float pascals,float altm,float tempC)
{
    char buffer[256];
    
    if (!_dataLog) return;
    refresh();
    uint16_t yr = year()+2000;
    byte month  = this->month();
    byte date   = day();
    byte hr     = hour();
    byte min    = minute();
    byte sec    = second();
    sprintf(buffer,"%d/%d/%d %02d:%02d:%02d: ",month,date,yr,hr,min,sec);
    _dataLog.print(buffer);
    sprintf(buffer,"Acceleration: %10.3g, %10.3g, %10.3g m/s^2",accel_x,accel_y,accel_z);
    _dataLog.print(buffer);
    sprintf(buffer,"; Barometric Pressure: %10.3g Inches (Hg)",pascals/3377.0);
    _dataLog.print(buffer);
    sprintf(buffer,"; Altitude: %10.3g meters",altm);
    _dataLog.print(buffer);
    sprintf(buffer,"; Temperature: %10.3g *C",tempC);
    _dataLog.print(buffer);
    _dataLog.println();
}
          
