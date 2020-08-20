EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:special
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:esp32_devboards
LIBS:adafruitboards
EELAYER 27 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date "29 apr 2019"
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L TTGO-T1 U101
U 1 1 5CC7417F
P 3400 1700
F 0 "U101" H 3400 1700 60  0000 C CNN
F 1 "TTGO-T1" H 3400 2250 60  0000 C CNN
F 2 "~" H 3400 1700 60  0000 C CNN
F 3 "~" H 3400 1700 60  0000 C CNN
	1    3400 1700
	1    0    0    -1  
$EndComp
$Comp
L ADAFRUIT_ADXL345 BO101
U 1 1 5CC74193
P 1750 3150
F 0 "BO101" H 1750 3307 60  0000 C CNN
F 1 "ADAFRUIT_ADXL345" H 1700 3450 60  0000 C CNN
F 2 "~" H 1750 3150 60  0000 C CNN
F 3 "~" H 1750 3150 60  0000 C CNN
	1    1750 3150
	0    -1   -1   0   
$EndComp
$Comp
L ADAFRUIT_DS3231_RTC BO103
U 1 1 5CC741AB
P 4800 3250
F 0 "BO103" H 4800 3250 60  0000 C CNN
F 1 "ADAFRUIT_DS3231_RTC" H 4850 3400 60  0000 C CNN
F 2 "~" H 4800 3250 60  0000 C CNN
F 3 "~" H 4800 3250 60  0000 C CNN
	1    4800 3250
	0    1    1    0   
$EndComp
$Comp
L ADAFRUIT_MPL3115A2_BO BO102
U 1 1 5CC741BA
P 3100 4600
F 0 "BO102" H 3000 4650 60  0000 C CNN
F 1 "ADAFRUIT_MPL3115A2_BO" H 3100 4800 60  0000 C CNN
F 2 "~" H 3100 4600 60  0000 C CNN
F 3 "~" H 3100 4600 60  0000 C CNN
	1    3100 4600
	-1   0    0    1   
$EndComp
$Comp
L 3V3 #PWR01
U 1 1 5CC741DD
P 2950 1100
F 0 "#PWR01" H 2950 1200 40  0001 C CNN
F 1 "3V3" H 2950 1225 40  0000 C CNN
F 2 "" H 2950 1100 60  0000 C CNN
F 3 "" H 2950 1100 60  0000 C CNN
	1    2950 1100
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR02
U 1 1 5CC741EC
P 3850 1050
F 0 "#PWR02" H 3850 1050 30  0001 C CNN
F 1 "GND" H 3850 980 30  0001 C CNN
F 2 "" H 3850 1050 60  0000 C CNN
F 3 "" H 3850 1050 60  0000 C CNN
	1    3850 1050
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR03
U 1 1 5CC741FB
P 2700 1900
F 0 "#PWR03" H 2700 1900 30  0001 C CNN
F 1 "GND" H 2700 1830 30  0001 C CNN
F 2 "" H 2700 1900 60  0000 C CNN
F 3 "" H 2700 1900 60  0000 C CNN
	1    2700 1900
	0    1    1    0   
$EndComp
Wire Wire Line
	2950 1250 2950 1100
Wire Wire Line
	3850 1250 3850 1050
Wire Wire Line
	2950 1900 2700 1900
Text Label 3850 1350 0    25   ~ 0
SCL
Text Label 3850 1500 0    25   ~ 0
SDA
Wire Wire Line
	2150 2800 4050 2800
Wire Wire Line
	4050 1350 4050 3000
Wire Wire Line
	4050 1350 3850 1350
Wire Wire Line
	2150 2900 4000 2900
Wire Wire Line
	4000 1500 4000 3100
Wire Wire Line
	4000 1500 3850 1500
Wire Wire Line
	4050 3000 4250 3000
Connection ~ 4050 2800
Wire Wire Line
	4000 3100 4250 3100
Connection ~ 4000 2900
Wire Wire Line
	2850 4100 2850 2800
Connection ~ 2850 2800
Wire Wire Line
	2700 4100 2700 2900
Connection ~ 2700 2900
$Comp
L 3V3 #PWR04
U 1 1 5CC742D3
P 3600 3800
F 0 "#PWR04" H 3600 3900 40  0001 C CNN
F 1 "3V3" H 3600 3925 40  0000 C CNN
F 2 "" H 3600 3800 60  0000 C CNN
F 3 "" H 3600 3800 60  0000 C CNN
	1    3600 3800
	1    0    0    -1  
$EndComp
Wire Wire Line
	3600 3800 3600 4100
Wire Wire Line
	2150 3600 2150 3900
Wire Wire Line
	2150 3900 3600 3900
Connection ~ 3600 3900
Wire Wire Line
	4250 2800 4150 2800
Wire Wire Line
	4150 2800 4150 3950
Wire Wire Line
	4150 3950 3600 3950
Connection ~ 3600 3950
$Comp
L GND #PWR05
U 1 1 5CC74331
P 4200 4350
F 0 "#PWR05" H 4200 4350 30  0001 C CNN
F 1 "GND" H 4200 4280 30  0001 C CNN
F 2 "" H 4200 4350 60  0000 C CNN
F 3 "" H 4200 4350 60  0000 C CNN
	1    4200 4350
	1    0    0    -1  
$EndComp
Wire Wire Line
	4250 2900 4100 2900
Wire Wire Line
	4100 2900 4100 4200
Wire Wire Line
	4100 4000 3450 4000
Wire Wire Line
	3450 4000 3450 4100
Wire Wire Line
	4100 4200 4200 4200
Wire Wire Line
	4200 4200 4200 4350
Connection ~ 4100 4000
Wire Wire Line
	2150 3400 4100 3400
Connection ~ 4100 3400
$EndSCHEMATC
