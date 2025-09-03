import board
import busio
import digitalio
import adafruit_sdcard
import storage
import json

def mount_filesystem():
    if board.board_id == "grandcentral_m4_express":
        # Connect to the card and mount the filesystem.
        spi = busio.SPI(board.SD_SCK, board.SD_MOSI, board.SD_MISO)
        cs = digitalio.DigitalInOut(board.SD_CS)
        sdcard = adafruit_sdcard.SDCard(spi, cs)
        vfs = storage.VfsFat(sdcard)
        storage.mount(vfs, "/sd")
        return None
    else:
        print("SD Card Not Supported")

def load_dict(filename):
    try:
        with open(("/sd/"+filename), 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"An error occurred while loading the dictionary: {e}")
        return None
    
def save_dict(dictionary, filename):
    try:
        with open(("/sd/"+filename), 'w') as file:
            json.dump(dictionary, file, indent=4)
        print(f"Dictionary saved to '{filename}'.")
    except Exception as e:
        print(f"An error occurred while saving the dictionary: {e}")
