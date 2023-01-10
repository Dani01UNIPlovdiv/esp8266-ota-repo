import network
import time
from machine import Pin
import senko


def connect():
    ssid = 'AtD'
    password = '12345678'
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)
    accesspoint = network.WLAN(network.AP_IF)
    accesspoint.active(True)
    accesspoint.config(essid='ESP8266', authmode=network.AUTH_WPA_WPA2_PSK, password='12345678')


def ota():
    GITHUB_URL = "https://github.com/Dani01UNIPlovdiv/esp8266-ota-repo"
    OTA = senko.Senko(url=GITHUB_URL, files=["main.py"])