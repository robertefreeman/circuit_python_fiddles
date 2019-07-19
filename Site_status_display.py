import board
import time
import busio
from digitalio import DigitalInOut
import terminalio
from adafruit_display_text import label
from adafruit_esp32spi import adafruit_esp32spi
import adafruit_esp32spi.adafruit_esp32spi_requests as requests

TEXT_URL = "https://www.google.com"

# If you are using a board with pre-defined ESP32 Pins:
esp32_cs = DigitalInOut(board.ESP_CS)
esp32_ready = DigitalInOut(board.ESP_BUSY)
esp32_reset = DigitalInOut(board.ESP_RESET)

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)

text_area = label.Label(
    terminalio.FONT,
    text="PyPortal\nRocks",
    max_glyphs=50,  # Optionally allow longer text to be added
    color = 0x00FF00,
    x=20,  # Pixel offsets from (0, 0) the top left
    y=20,
    line_spacing=1,  # Distance between lines
)

def checksite(site):
    r = requests.get(site)
    r.close()
    return str(r.status_code)

requests.set_interface(esp)

while not esp.is_connected:
    try:
        esp.connect_AP('RobRadio2', 'kreative')
    except RuntimeError as e:
        print("could not connect to AP, retrying: ",e)
        continue

while True:
    print('-'*40)
    print("Status code: " + checksite("https://www.google.com"))
    print('-'*40)
    time.sleep(3)
