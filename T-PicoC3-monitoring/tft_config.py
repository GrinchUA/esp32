from machine import Pin, SoftSPI, SPI
import st7789py as st7789

def config():
    Pin(22, Pin.OUT, value=1) 

    spi = SoftSPI(
        baudrate=20000000,
        polarity=1,
        phase=0,
        sck=Pin(2),
        mosi=Pin(3),
        miso=Pin(13)
    )

    return st7789.ST7789(
        spi,
        135,
        240,
        reset=Pin(0, Pin.OUT),
        cs=Pin(5, Pin.OUT),
        dc=Pin(1, Pin.OUT),
        backlight=Pin(4, Pin.OUT),
        rotation=1
    )