import board
import audioio
import neopixel
import time
import adafruit_adt7410
import busio
import terminalio
from adafruit_display_text import label


text_area = label.Label(
    terminalio.FONT,
    text="PyPortal\nRocks",
    max_glyphs=50,  # Optionally allow longer text to be added
    color = 0x00FF00,
    x=20,  # Pixel offsets from (0, 0) the top left
    y=20,
    line_spacing=1,  # Distance between lines
)

temp_sensor = adafruit_adt7410.ADT7410(
    busio.I2C(board.SCL, board.SDA),
    address=0x48,  # Specific device address for ADT7410
)
temp_sensor.high_resolution = True


# Connect to the NeoPixel (there is only one so it is index 0)
# auto_write means we don't have to call pixels.show() each time
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1, auto_write=True)

def play_sound_file(file_path):
    try:
        with open(file_path, "rb") as f:
            wave = audioio.WaveFile(f)
            audio.play(wave)
            while audio.playing:
                time.sleep(0.005)
    except OSError as e:
        print('Error opening file: %s' % e)

while True:
    pixels[0] = (255, 0, 0)  # Red, green, blue
    time.sleep(1)
    pixels[0] = (0, 255, 0)
    time.sleep(1)
    pixels[0] = (0, 0, 255)
    time.sleep(1)
    # with audioio.AudioOut(board.AUDIO_OUT) as audio:  # or board.A0
    #    play_sound_file("super_cool.wav")
    degrees_f = (temp_sensor.temperature) * 9/5 + 32
    print('Temperature: %s F' % degrees_f)
    text_area.text = str(degrees_f)
    board.DISPLAY.show(text_area)
