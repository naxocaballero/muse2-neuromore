# muse2-neuromore
A small script that split differents signals from muse vía OSC

Necessary elements:
1.- Mind Monitor (Old Muse Monitor)
2.- Python (I use python 3.8.0)
3.- Muse Headband 2
4.- Neuromore installed and working


Instructions:

1.- Open Mind Monitor (former Muse Monitor), and set the IP of the computer that will run muse.py and the listening port (in my case 192.168.1.199 and 5005).

2.- Place muse2 and observe on the mobile phone (or tablet) that signals are received in Mind Monitor. Start transiting via OSC.

3.- Run muse.py

4.- Open Neuromore and configure the necessary input sources (have the correct OSC input parameters configured in neuromore; in my case 0.0.0.0 and 4545).


