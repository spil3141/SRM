
################################################################################
# Copyright (C) 2012-2013 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################


#For Windows OS
import os, sys, inspect
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../dependencies/lib-win/x64' if sys.maxsize > 2**32 else '../dependencies/lib-win/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
sys.path.insert(1, os.path.abspath(os.path.join(src_dir, "../dependencies/lib-win")))
#For Mac OS
#sys.path.insert(1,'../dependencies/lib-mac')
#sys.path.insert(0,'../dependencies/lib-mac/Leap.py')
import Leap, thread, time, os, pandas, numpy ,ctypes
import matplotlib.pyplot as plt
import numpy as np 
#global variable for image 
image = None 

class SampleListener(Leap.Listener):
    
    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        self.datasets.close()
        print "Exited"
        
    
    def on_frame(self, controller):
        frame = controller.frame()
        right_image = frame.images[0]
        if right_image.is_valid:
            print "Image: "
            global image
            #wrap image data in numpy array
            i_address = int(right_image.data_pointer)
            ctype_array_def = ctypes.c_ubyte * right_image.height * right_image.width
            # as ctypes array
            as_ctype_array = ctype_array_def.from_address(i_address)
            # as numpy array
            as_numpy_array = np.ctypeslib.as_array(as_ctype_array)
            image = np.reshape(as_numpy_array, (right_image.height, right_image.width))
            plt.imshow(image)
            plt.show()
            
        
        
        
def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()
    controller.set_policy_flags(Leap.Controller.POLICY_IMAGES)
    # Have the sample listener receive events from the controller
    controller.add_listener(listener)
    
    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
#        sys.stdin.readline()
        raw_input()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()

