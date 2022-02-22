# irealpro_automation
An automation tool for recording songs out of iRealPro

**Attention -> This only works on Windows**

## Setup

Create an python environment with python 3.8 or lower

This project uses a forked version of pyaudio to record the system audio via loopback.
Download and install the .msi from https://github.com/intxcc/pyaudio_portaudio/releases

If you are using Anaconda or miniconda go to *\Miniconda\envs\'your_environment'\Lib\site-packages* and replace/add 
1. pyaudio.py
2. _portaudio.cp37-win_amd64.pyd
3. PyAudio-0.2.11-py3.7.egg-info

## Select loopback audio device
In the script there is a method called list_devices() which lists all possible audio devices.

You need to find the loopback device to record the PC audio.

Tip: to find that open Audacity and play a sound on your PC and try recording.
https://manual.audacityteam.org/man/tutorial_recording_computer_playback_on_windows.html

Then you need to replace dev_index with the index of the found device.
