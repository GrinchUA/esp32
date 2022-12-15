import urequests
import time
from esp import ESP

import st7789py as st7789
import tft_config
import vga1_8x16 as font

tft = tft_config.config()
tft.fill(0) #clears after previous display

step = 15

def log(text):
    global step
    x = chr(32)
    #uses endSpace to clear the end of the line each time the line gets overwritten
    endSpace = str(x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x)
    tft.text(
        font,
        text+endSpace,
        15,
        step,
        st7789.GREEN,
        st7789.BLACK
    )    

    step += 15

uart_id=1
tx_pin=8
rx_pin=9
baud_rate=115200
tx_buffer=2048
rx_buffer=2048

class Monitoring:
    def __init__(self, debug=False):
        self.esp = ESP(uart_id, tx_pin, rx_pin, baud_rate, tx_buffer, rx_buffer, debug=debug)
        self.secrets = {
            "ssid":"la-la-la",
            "password":"uagshfn12"
        }

        self.wi_fi_conect()
        while True:
            self.mon()
            time.sleep(30)
        
    def wi_fi_conect(self):
        log('SSID: '+self.secrets['ssid'])
        log('Password: '+self.secrets['password'])

        self.esp.soft_reset()
        self.esp.set_mode(3)

        try:
            self.esp.connect(self.secrets)
            log(f'Wifi connected {self.esp.is_connected} : {self.esp.local_ip}')
            return self.esp.is_connected
        except Exception as e:
            print(e)
            return False


    def mon(self):
        if not self.esp.is_connected:
            self.wi_fi_conect()

        if self.esp.is_connected:
            self.check()

    def check(self):
        if self.esp.ping('192.168.1.150'):
            #tft.fill_rect(0, 0, 240, 135, st7789.GREEN)
            tft.sleep_mode(True)
        else:
            tft.sleep_mode(False)
            tft.fill_rect(0, 0, 240, 135, st7789.RED)


if __name__=='__main__':
    Monitoring()
