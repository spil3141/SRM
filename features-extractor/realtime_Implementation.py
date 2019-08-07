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
import Leap, thread, time, os, numpy 

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
        # Get the most recent frame and report some basic information
        frame = controller.frame()
        # Get hands
        self.X = list()
        for hand in frame.hands:
            # Get the hand's Bones and direction
            # Get fingers
#            print "unknow",
            self.X.append("unknow"),
            for finger in hand.fingers:
                # Get bones
                for i in range(0,4):
#                    print ",%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f" % (
#                        finger.bone(i).prev_joint.x,
#                        finger.bone(i).prev_joint.y,
#                        finger.bone(i).prev_joint.z,
#                        finger.bone(i).next_joint.x,
#                        finger.bone(i).next_joint.y,
#                        finger.bone(i).next_joint.z,
#                        finger.bone(i).direction.x,
#                        finger.bone(i).direction.y,
#                        finger.bone(i).direction.z
#                    ),
                    self.X.append(",%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f" % (
                        finger.bone(i).prev_joint.x,
                        finger.bone(i).prev_joint.y,
                        finger.bone(i).prev_joint.z,
                        finger.bone(i).next_joint.x,
                        finger.bone(i).next_joint.y,
                        finger.bone(i).next_joint.z,
                        finger.bone(i).direction.x,
                        finger.bone(i).direction.y,
                        finger.bone(i).direction.z
                    )),
#        print "\n"
        self.X.append("\n")
        
        temp = numpy.asarray(self.X)
        
        self.X = self.into_a_line(temp)
        
        if len(temp) > 1:
            self.detected_hand()
        else:
            self.did_not_detect_hand()
#        print temp
        self.X= []
        
    def into_a_line(self,a):
        
        return a
    
    def detected_hand(self):
        print self.X
    
    def did_not_detect_hand(self):
        print "No Hand Detected"
        
        
def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

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
