// -!- c++ -!- //////////////////////////////////////////////////////////////
//
//  System        : 
//  Module        : 
//  Object Name   : $RCSfile$
//  Revision      : $Revision$
//  Date          : $Date$
//  Author        : $Author$
//  Created By    : Robert Heller
//  Created       : Sun Aug 9 12:05:00 2020
//  Last Modified : <200809.1532>
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

#ifndef __SERIALCLI_H
#define __SERIALCLI_H

#include <uRTCLib.h>
#include <FS.h>
#include <SD.h>

class SerialCLI : public uRTCLib {
private:
    typedef enum {SET='S', OPENNEW='O', CLOSE='C', HELP='H'} Commands;
    static const char *HelpText[];
public:
    SerialCLI();
    ~SerialCLI();
    void ProcessCommandLine();
    void LogData(float accel_x,float accel_y,float accel_z,float pascals,
                 float altm,float tempC);
private:
    File _dataLog;
};

#endif // __SERIALCLI_H

