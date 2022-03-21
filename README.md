# irealpro_automation
An automation tool for recording songs out of iRealPro running in Bluestacks.

**Attention since this project records the loopback audio it only works on Windows.**

## Get it running

### Create environment
Clone the repository and create a conda environment with:

`conda env create -f environment.yml`


### Set up the forked pyaudio
This project uses a forked version of pyaudio to record the system audio via loopback.
Download and install the .msi from [here](https://github.com/intxcc/pyaudio_portaudio/releases).
Since it's an installer, choose a proper installation directory. 

After the installation 3 files are created:
1. pyaudio.py
2. _portaudio.cp37-win_amd64.pyd
3. PyAudio-0.2.11-py3.7.egg-info

If you are using Anaconda or miniconda navigate to the path 
`\Miniconda\envs\'your_environment'\Lib\site-packages`  
and replace the existing pyaudio files with the new ones.

### Window setup
#### Predefined
Since this script works with strict monitor coordinates a 2 monitor setup is definitely an advantage.  
To get this working you need to set the resolution of your monitor to **1920x1080**.

1. Put Fullscreen Bluestacks with iRealPro open on the right screen
2. Start the script
3. You should see the mouse moving and operating Bluestacks  
4. Do not move your mouse or keyboard and wait for the program to finish.
5. The generated .wav files can be found in the recordings folder

#### Alternative
Run the mouse_position.py script and click on the screen to get coordinates.  
You can then replace them in the constants.py.

## Select loopback audio device
### Recommended way 
The easiest method to find the loopback device is to download Audacity and follow [this guide](https://manual.audacityteam.org/man/tutorial_recording_computer_playback_on_windows.html
).

After finding the loopback device follew these steps:
1. Open main.py
2. Navigate to the main method
3. Only run the list_devices() method
4. This will print all possible devices with index
5. Find your loopback devices index 
6. Set the value of `dev_index =`  to the found index
7. Comment list_devices()
8. Run search_song()

**Be cautious, every new/plugged in device (webcam, microphone) will change the device indices.  
This could result in a new setup of the loopback device.**

### Alternative way
Try to find loopback devices by hand without Audacity.  
1. Set `dev_index =` to every possible index
2. Start a random sound on you PC and let it run the entire time
3. Let the script create one recording
4. Listen if the recording plays the PCs system sound
5. YES -> Loopback found | NO -> Repeat with the next device

If some devices generate an error that is no problem they are probably some virtual devices without input channels.  
Just ignore them and continue searching.
