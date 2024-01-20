# rtTranslator

Simple overlay for Windows, that listens for background sound and translates it to text thats displayed on the screen.

![](images/screenshot.png)

## Installation

0. Set your loopback device as default device
1. Clone the repository
2. Change `config.py` to your liking
3. Install the requirements
4. Run `python -m app`

For now it's only working on windows, but I'm planning to make it cross-platform.
> You need a loopback device to make it work. Check out [Loopback device setup](#loopback-device-setup) for more info.

### Loopback device setup

1. Install [VB-CABLE](https://vb-audio.com/Cable/) and [Voicemeeter](https://vb-audio.com/Voicemeeter/index.htm)
2. Set your default playback device to `CABLE Input (VB-Audio Virtual Cable)` and default recording device to `VoiceMeeter Output` or `CABLE output`
3. Run Voicemeeter and set your **Hardware input** device to `CABLE Output (VB-Audio Virtual Cable)`

## Usage

Just run app and it will start listening for sound and translating it to text.