#!/usr/bin/python
import random
import re
from phue import Bridge
import random

b = Bridge('10.0.1.3') # Enter bridge IP here.

WORDS = ["ON", "OFF", "OF", "TOGGLE", "KITCHEN", "BEDROOM"]

lights = b.get_light_objects()

def handle(text, mic, profile):

	if re.search(r'\bkitchen\b', text, re.IGNORECASE):

		if re.search(r'\bon\b', text, re.IGNORECASE):
			mic.say("Turning on the kitchen lights.")
			
			b.set_group('Kitchen', 'on', True)

		elif re.search(r'\boff\b', text, re.IGNORECASE) or re.search(r'\bof\b', text, re.IGNORECASE):
			mic.say("Turning off the kitchen lights.")
			
			b.set_group('Kitchen', 'on', False)

		else:
			mic.say("Sorry, I didn't understand that.")

	elif re.search(r'\bbedroom\b', text, re.IGNORECASE):

		if re.search(r'\bon\b', text, re.IGNORECASE):
			mic.say("Turning on the bedroom lights.")

			b.set_group('Bedroom', 'on', True)

		elif re.search(r'\boff\b', text, re.IGNORECASE) or re.search(r'\bof\b', text, re.IGNORECASE):
			mic.say("Turning off the bedroom lights.")

			b.set_group('Bedroom', 'on', False)

		else:
			mic.say("Sorry, I didn't understand that.")

	elif re.search(r'\bon\b', text, re.IGNORECASE):
		mic.say("Turning all lights on.")

		for light in lights:
			light.on = True

	elif re.search(r'\boff\b', text, re.IGNORECASE) or re.search(r'\bof\b', text, re.IGNORECASE):

		mic.say("Turning lights off.")

		for light in lights:
			light.on = False

	else:
		mic.say("I didn't understand that.")
	
def isValid(text):
	if re.search(r'\bon\b', text, re.IGNORECASE):
		return True
	elif re.search(r'\boff\b', text, re.IGNORECASE):
		return True
	elif re.search(r'\btoggle\b', text, re.IGNORECASE):
		return True
	elif re.search(r'\bkitchen\b', text, re.IGNORECASE):
		return True
	elif re.search(r'\bbedroom\b', text, re.IGNORECASE):
		return True
	else:
		return False
