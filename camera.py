from __future__ import print_function
import pixy 
from ctypes import *
from pixy import *
import RPi.GPIO as GPIO
import time
from time import sleep

# Code used if from the sample pixycam code GetBlocks

pixy.init ()
pixy.change_prog ("color_connected_components");

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

block_x = 0
block_y = 0
block_width = 0
block_height = 0

object_width = 0.56 #m
object_height = 0.64 #m
focal_width = 208.2143
focal_height = 250.9375
    
def getCamera():
    ave_x = 0
    ave_y = 0
    ave_width = 0
    ave_height = 0
    ave_count = 0
    

    ave_distance = 100
    position = "OUT"
    
    count = pixy.ccc_get_blocks (100, blocks)

    if count > 0:
        block_x = 0
        block_y = 0
        block_width = 0
        block_height = 0
        for index in range (0, count):
            block_x += blocks[index].m_x
            block_y += blocks[index].m_y      
            block_width += blocks[index].m_width
            block_height += blocks[index].m_height

        block_x /= count
        block_y /= count
        ave_count += 1
    
        ave_x += float(block_x)
        ave_y += float(block_y)
        ave_width += float(block_width)
        ave_height += float(block_height)
    
        if ave_count == 10:
            ave_count = 0
            ave_x = ave_x / 10
            ave_y = ave_y / 10
            ave_width = ave_width / 10
            ave_height = ave_height / 10
      
        width_distance = focal_width * object_width / ave_width
        height_distance = focal_height * object_height / ave_height

        ave_distance = (width_distance + height_distance) / 2
        #print('[width=%f height=%f\n]' % (ave_width, ave_height))
        #print('[X=%f Y=%f\n]' % (ave_x, ave_y))
      
        #print("Distance: %f" % ave_distance)
        if ave_distance > 1 and ave_distance < 2:
            if (ave_x > 0 and ave_x < 105):
         #       print("LEFT\n")
                position = "LEFT"
            elif (ave_x >= 105 and ave_x < 210):
          #      print("MIDDLE\n")
                position = "MIDDLE"
            elif (ave_x >= 210 and ave_x < 315):
           #     print("RIGHT\n")
                position = "RIGHT"
            else:
            #    print("ERROR: x = %f\n" % ave_x)
                position = "OUT"
        else:
           # print("Out of Bounds\n")
            position = "OUT"
        
    return ave_distance, position

  