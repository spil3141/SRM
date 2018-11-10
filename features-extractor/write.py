################################################################################
# Copyright (C) 2012-2013 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################
import sys 
sys.path.insert(1,'../dependencies/lib-mac')
sys.path.insert(0,'../dependencies/lib-mac/Leap.py')
import Leap, thread, time


class SampleListener(Leap.Listener):
    datasets = open("../dataset/test.csv", 'wb')
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
        for hand in frame.hands:
            # Get the hand's and direction
            direction = hand.direction
            # Get fingers
            self.datasets.write("0"),
            for finger in hand.fingers:
                # Get bones
                for i in range(0,4):
                    self.datasets.write (",%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f" % (
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
            self.datasets.write ("\n")
        
def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)
    
    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
