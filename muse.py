"""

This program listens to the eeg signal from muse, separates it into its basic components and forwards it to another UDP port via OSC
It was written on python 3.8.0
Needs python-osc library. I used python-osc-1.7.3

"""
import math
import time
import os

from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import osc_message_builder
from pythonosc import udp_client

bind_host = "0.0.0.0"	#listening ip
bind_port = 5005	#listening port

target_host = "127.0.0.1"	#Neuromore host (itself machine)
target_port = 4545	#Neuromore udp port

client = udp_client.SimpleUDPClient(target_host, target_port)

#HANDLERS: It handle original raw signal and split it to forward via OSC

def eeg_handler(address, egg, tp9, af7, af8, tp10, fpz):
	client.send_message("/muse/eeg/tp9", tp9)
	client.send_message("/muse/eeg/af7", af7)
	client.send_message("/muse/eeg/af8", af8)
	client.send_message("/muse/eeg/tp10", tp10)
	client.send_message("/muse/eeg/fpz", fpz)
	
def alpha_handler(address, alpha, tp9, af7, af8, tp10):
	client.send_message("/muse/elements/alpha_absolute/tp9", tp9)
	client.send_message("/muse/elements/alpha_absolute/af7", af7)
	client.send_message("/muse/elements/alpha_absolute/af8", af8)
	client.send_message("/muse/elements/alpha_absolute/tp10", tp10)

def beta_handler(address, beta, tp9, af7, af8, tp10):
	client.send_message("/muse/elements/beta_absolute/tp9", tp9)
	client.send_message("/muse/elements/beta_absolute/af7", af7)
	client.send_message("/muse/elements/beta_absolute/af8", af8)
	client.send_message("/muse/elements/beta_absolute/tp10", tp10)

#You can create anothers def's from several signals
#def theta_handler(address, theta, tp9, af7, af8, tp10):
#	client.send_message("/muse/elements/theta_absolute/tp9", tp9)
#	client.send_message("/muse/elements/theta_absolute/af7", af7)
#	client.send_message("/muse/elements/theta_absolute/af8", af8)
#	client.send_message("/muse/elements/theta_absolute/tp10", tp10)

if __name__ == "__main__":

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/muse/eeg", eeg_handler, "EEG")
    dispatcher.map("/muse/elements/alpha_absolute", alpha_handler, "ALPHA")
    dispatcher.map("/muse/elements/beta_absolute", beta_handler, "BETA")

# 	You can write here other mapping for several signals (remember making def's)
# 	dispatcher.map("/muse/elements/theta_absolute", theta_handler, "THETA")
# 	[...]
# 	[...]
   

    server = osc_server.ThreadingOSCUDPServer( (bind_host, bind_port), dispatcher)
    print("Listening on {}".format(server.server_address) + " and forwarding to ('" + target_host + "', " + str(target_port) + ")")
    server.serve_forever()
