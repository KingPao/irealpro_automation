import time

from pynput.mouse import Controller, Button
import constants
import csv
import keyboard
import pyaudio
import wave


# import mod_pyaudio.pyaudio as pya


def search_song():
    with open('resources/music.csv') as file:
        reader = csv.reader(file)

        for song_name in reader:
            print(''.join(song_name))
            control_peripherals(''.join(song_name))


def control_peripherals(song_name):
    mouse = Controller()
    mouse.position = constants.SONGS
    mouse.click(Button.left, 1)
    print("Click on Songs")

    mouse.position = constants.SEARCH
    mouse.click(Button.left, 1)
    print("Click on Search")

    keyboard.write(song_name, delay=0.15)
    print("Search for ", song_name)

    mouse.position = constants.FIRST_ENTRY
    mouse.click(Button.left, 1)
    print("Click on First Entry")

    time.sleep(0.5)
    mouse.position = constants.PLAY
    mouse.click(Button.left, 1)
    print("Click on Play Button")

    handle_recording(song_name)

    mouse.position = constants.PLAY
    mouse.click(Button.left, 1)
    print("Click on Play Button")

    time.sleep(0.5)
    mouse.position = constants.EXIT_SEARCH
    mouse.click(Button.left, 1)
    print("Click on Exit Button")


def handle_recording(filename):
    chunk = 1024
    audio_format = pyaudio.paInt16
    channels = 2
    rate = 44100
    record_seconds = 5

    p = pyaudio.PyAudio()
    dev_index = 8

    info = p.get_device_info_by_index(dev_index)
    print(str(info["index"]) + ": \t %s \n \t %s \n" % (
        info["name"], p.get_host_api_info_by_index(info["hostApi"])["name"]))

    stream = p.open(format=audio_format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    input_device_index=dev_index,
                    frames_per_buffer=chunk,
                    as_loopback=True)

    print('-----Now Recording ' + filename + '-----')
    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the Stream and PyAudio
    stream.stop_stream()
    stream.close()
    p.terminate()

    print('-----Finished Recording ' + filename + '-----')

    # Open and Set the data of the WAV file
    file = wave.open("recordings/" + filename + '.wav', 'wb')
    file.setnchannels(channels)
    file.setsampwidth(p.get_sample_size(audio_format))
    file.setframerate(rate)

    # Write and Close the File
    file.writeframes(b''.join(frames))
    file.close()


def list_devices():
    p = pyaudio.PyAudio()
    print("Available devices:\n")

    for i in range(0, p.get_device_count()):
        info = p.get_device_info_by_index(i)
        print(str(info["index"]) + ": \t %s \n \t %s \n" % (
            info["name"], p.get_host_api_info_by_index(info["hostApi"])["name"]))


if __name__ == '__main__':
    search_song()
    # list_devices()
    # handle_recording('test_it.wav')
