import time
import sys
import os
from easygui import multenterbox

cwd = os.getcwd()
sys.path.append(cwd+'/src')

from image_handler import Image_handler
from mouse_automate_black import Mouseomate as Mouseomate_black
from mouse_automate_color import Mouseomate as Mouseomate_color

mode = "black" # "color", "black" //Color mode is buggy and should be avoided.
app = "paint" # Name of application that you're drawing with.

os.chdir("images")


lsleep = 0.005 #adujust this to change pause time at end of line (recommend .002)
rsleep = 0.025 #adujust this to change pause time at end of row (recommend .025)
imagename = Image_handler.get_image()
handler = Image_handler(imagename)
message = "Resize value: What is the approximate pixel size you would like to output?\nOffset: What is the approximate brush size in pixels? (1 for one to one drawing)"
resizevalue, offset = multenterbox(message,"Cursor Draw", ["Resize value","Offset"])
resizevalue = int(resizevalue) if resizevalue else 100
offset = int(offset) if offset else 1
resizevalue = resizevalue / offset
handler.convert_bandw(mode)
handler.resize(resizevalue)
	
handler.im.show()
returnkey = None
while returnkey == None:
	print("Preview image loaded. ENTER to begin 3 seconds countdown, N to abort.")
	print("Once drawing has started, pulling mouse quickly to any corner will abort the program.")
	returnkey = input()
	returnkey = returnkey.lower()
	if returnkey == 'n':
		exit()
	if returnkey == 'i':
		handler.invert(imagename)
		handler.convert_bandw(mode)
		resizevalue = resizevalue / offset
		handler.resize(resizevalue)
		handler.im.show()
		returnkey = None

time.sleep(3)
array = handler.update_array()
if mode == "color":
	Mouseomate_color.image_to_lines(array, offset, rsleep, lsleep, app)
elif mode == "black":
	Mouseomate_black.image_to_lines(array, offset, rsleep, lsleep)
		
repeat = 'y'
while repeat == 'y':
	repeat = input("Press Y to draw again, or ENTER to exit.")
	repeat = repeat.lower()
	if repeat == 'y':
		print("3")
		time.sleep(1)
		print("2")
		time.sleep(1)
		print("1")
		time.sleep(1)
		if mode == "color":
			Mouseomate_color.image_to_lines(array, offset, rsleep, lsleep, app)
		elif mode == "black":
			Mouseomate_black.image_to_lines(array, offset, rsleep, lsleep)
	else:
		exit()

