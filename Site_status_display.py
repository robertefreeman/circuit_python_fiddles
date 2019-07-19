import board
import audioio
import neopixel
import time
import busio
import terminalio
from adafruit_display_text import label


text_area = label.Label(
    terminalio.FONT,
    text="",
    max_glyphs=50,  # Optionally allow longer text to be added
    color = 0x00FF00,
    x=20,  # Pixel offsets from (0, 0) the top left
    y=20,
    line_spacing=1,  # Distance between lines
)



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
    pixels[0] = (0, 255, 0)  # Red, green, blue
    time.sleep(1)
    # with audioio.AudioOut(board.AUDIO_OUT) as audio:  # or board.A0
    #    play_sound_file("super_cool.wav")
    text_area.text = str('Site is up')
    board.DISPLAY.show(text_area)
