from blessed import Terminal
from httplib import HTTPConnection
import urllib
import time
import multicast_receiver
import multicast_sender
import random
import screen_color

term = Terminal()
height, width = term.height, term.width
params = {'token' : 0, 'starting': 0, 'total': 0}
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

def compute_primes(starting=0, _total=0):
	print("Hasn't been defined!")

primes = compute_primes

def set_primes():
	val = primes(params['starting'], params['total'])
	params['starting'] = val[0]
	params['total'] = val[1]


def connect():
	while len(multicast_receiver.ips) < 1:
		pass
	try:
		multicast_receiver.lock.acquire()
		connection = HTTPConnection(random.choice(list(multicast_receiver.ips.keys())), 5000, timeout=10)
		multicast_receiver.lock.release()
		connection.request("POST", "/", urllib.urlencode(params), headers)
		response = connection.getresponse()
		return True
	except multicast_receiver.socket.error:
		return connect()


def send_token():
	set_primes()
	if connect() == False:
		print("Something went wrong")
	else:
		params['token'] = 0
		#screen_color.color("red")
	return 1