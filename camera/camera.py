from __future__ import print_function
import pixy 
from ctypes import *
from pixy import *
import RPi.GPIO as GPIO

# Code used if from the sample pixycam code GetBlocks

pixy.init ()
pixy.change_prog ("color_connected_components");

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)

class Blocks (Structure):
  _fields_ = [ ("m_signature", c_uint),
    ("m_x", c_uint),
    ("m_y", c_uint),
    ("m_width", c_uint),
    ("m_height", c_uint),
    ("m_angle", c_uint),
    ("m_index", c_uint),
    ("m_age", c_uint) ]

blocks = BlockArray(100)
frame = 0

ave_x = 0
ave_y = 0
ave_width = 0
ave_height = 0
ave_count = 0

object_width = 0.56 #m
object_height = 0.64 #m
focal_width = 208.2143
focal_height = 250.9375

while 1:
  count = pixy.ccc_get_blocks (100, blocks)

  if count > 0:
    print('frame %3d:' % (frame))
    frame = frame + 1
    for index in range (0, count):
      #print('[BLOCK: SIG=%d X=%3d Y=%3d WIDTH=%3d HEIGHT=%3d]' % (blocks[index].m_signature, blocks[index].m_x, blocks[index].m_y, blocks[index].m_width, blocks[index].m_height))

    ave_count += 1
    
    ave_x += blocks[0].m_x
    ave_y += blocks[0].m_y
    ave_width += blocks[0].m_width
    ave_height += blocks[0].m_height
    
    if ave_count == 10:
      ave_count = 0
      ave_x = ave_x / 10
      ave_y = ave_y / 10
      ave_width = ave_width / 10
      ave_height = ave_height / 10
      
      width_distance = focal_width * object_width / ave_width
      height_distance = focal_height * object_height / ave_height
      
      ave_distance = (width_distance + height_distance) /2
      print("Distance: %3d\n" % ave_distance)
      if (ave_x < 105.333333):
        print("You are in the LEFT SIDE\n")
      elsif (ave_x >= 105.333333 and ave < 210.666666):
        print("You are in the MIDDLE SIDE\n")
      elsif (ave_x >= 210.666666 and ave_X < 316):
        print("You are in the RIGHT SIDE\n")
      else
        print("ERROR\n")
      
    
    GPIO.output(16, GPIO.HIGH)
  else:    
    GPIO.output(16, GPIO.LOW)

