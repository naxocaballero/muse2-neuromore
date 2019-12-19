# muse2-neuromore
A small script that split differents signals from muse vía OSC

Necessary elements:

1.- Mind Monitor (Old Muse Monitor)

2.- Python (I use python 3.8.0) with python-osc-1.7.3 library ( To install type "pip install python-osc" ).

3.- Muse Headband 1 or 2

4.- Neuromore installed and working


Instructions:

1.- Open Mind Monitor (former Muse Monitor), and set the IP of the computer that will run muse.py and the listening port (in my case 192.168.1.199 and 5005).

2.- Place muse2 and observe on the mobile phone (or tablet) that signals are received in Mind Monitor. Start transiting via OSC.

3.- Run muse_average.py if you have the OSC Stream brainwaves setting in Mind monitor set to average values.
  - Run muse_absolute.py if you have the OSC Stream brainwaves setting in Mind monitor set to all values.

4.- Open Neuromore and configure the necessary input sources (have the correct OSC input parameters configured in neuromore; in my case 0.0.0.0 and 4545).


