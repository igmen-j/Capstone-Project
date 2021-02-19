#===========================================================#
# camera.py                                                 #
# File for the camera component                             #
#                                                           #
# **Code reference: PixyCam code- get_blocks_python_demo.py #                                                   
#===========================================================#

from __future__ import print_function
import pixy 
from ctypes import *
from pixy import *

pixy.init ()
pixy.change_prog ("color_connected_components");

#========== Block initialization ===========
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
block_x = 0
block_y = 0
block_width = 0
block_height = 0
#==========================================

#============= Vest Dimensions ============
# Source: https://www.pyimagesearch.com/2015/01/19/find-distance-camera-objectmarker-using-python-opencv/
# Vest dimensions
object_width = 0.56 # meters
object_height = 0.64 # meters
focal_width = 208.2143 # pixels
focal_height = 250.9375 # pixels
#==========================================
    
 
# Function: getCamera
# Description: Determines the block size of the object detected anf returns the distance and position
# Parameters: None
# Returns: distance, position
def getCamera():   
    distance = 100 # default value for distance in meters
    position = "OUT" # default value for position (Out of Bounds)
    ave_count = 0
    count = pixy.ccc_get_blocks (100, blocks) # gets the number of blocks detected by the camera
    
    if count > 0:  #if there are blocks detected
        block_x, block_y, block_width, block_height = getBlockParams(count, blocks)	
        ave_x, ave_y, ave_width, ave_height = getAverageParams(ave_count, block_x, block_y, block_width, block_height)
        distance = getDistance(ave_width, ave_height)
        position = getPosition(ave_x, ave_y)
        
    return distance, position
  

# Function: getBlockParams
# Description: Combines all the blocks detected and takes the average
# Parameters: count, blocks
# Returns: block_x, block_y, block_width, block_height
def getBlockParams(count, blocks):
    block_x = 0
    block_y = 0
    block_width = 0
    block_height = 0
    for index in range (0, count): # add all the blocks together
        block_x += blocks[index].m_x
        block_y += blocks[index].m_y      
        block_width += blocks[index].m_width
        block_height += blocks[index].m_height

    block_x /= count # take the average of x
    block_y /= count # take the average of y

    return block_x, block_y, block_width, block_height


# Function: getAverageParams
# Description: Takes the average of the parameters every 10 frames
# Parameters: block_x, block_y, block_width, block_height
# Returns: ave_x, ave_y, ave_width, ave_height
def getAverageParams(ave_count, block_x, block_y, block_width, block_height):
    if ave_count == 0:
        ave_x = 0
        ave_y = 0
        ave_width = 0
        ave_height = 0
    
    ave_count += 1

    ave_x += float(block_x)
    ave_y += float(block_y)
    ave_width += float(block_width)
    ave_height += float(block_height)
    
    if ave_count == 10:	# if 10 frames has passed, take the average parameters
        ave_count = 0
        ave_x = ave_x / 10
        ave_y = ave_y / 10
        ave_width = ave_width / 10
        ave_height = ave_height / 10

    return ave_x, ave_y, ave_width, ave_height

# Function: getDistance
# Description: Use the formula from https://www.pyimagesearch.com/2015/01/19/find-distance-camera-objectmarker-using-python-opencv/
#            to determine the distance of object to camera
# Parameters: ave_width, ave_height
# Returns: ave_distance
def getDistance(ave_width, ave_height):
    width_distance = focal_width * object_width / ave_width
    height_distance = focal_height * object_height / ave_height
    ave_distance = (width_distance + height_distance) / 2
    
    return ave_distance
    
# Function: getPosition
# Description: Determine the position of the object based on its coordinates and distance
# Parameters: ave_distance, ave_x, ave_y
# Returns: position
def getPosition(ave_x, ave_y):
    # x range: 0 to 315, y range: 0 to 206
    if (ave_x > 0 and ave_x < 105):
        position = "LEFT"
    elif (ave_x >= 105 and ave_x < 210):
        position = "MIDDLE"
    elif (ave_x >= 210 and ave_x < 315):
        position = "RIGHT"
    else:# should never be here but added for safety
        position = "OUT"

    return position
