import network
import socket
from time import sleep
#from picozero import pico_temp_sensor, pico_led
import machine

ssid = 'AshXhome_New'
password = 'Andrew00'

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
        
    print(wlan.ifconfig())
    return(wlan.ifconfig()[0])
    
def open_socket(ip):
    # Open a socket
    address = (ip, 5005)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    print(connection)

    
try:
    connect()
except KeyboardInterrupt:
    machine.reset()