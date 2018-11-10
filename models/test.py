import sys 
sys.path.insert(1,'../dependencies/lib-mac')
sys.path.insert(0,'../dependencies/lib-mac/Leap.py')
import Leap, thread, time
#from sklearn.externals import joblib
#import pandas as pd

#model = joblib.load('SRM_1.sav')

class SampleListener(Leap.Listener):
    
    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()
        # Get hands
        for hand in frame.hands:
            # Get the hand's and direction
            direction = hand.direction
            
            for finger in hand.fingers:
                # Get bones
                for i in range(0,4):
<<<<<<< HEAD
                    print (",%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f" % (
                        finger.bone(0).prev_joint.x,
                        finger.bone(0).prev_joint.y,
                        finger.bone(0).prev_joint.z,
                        finger.bone(0).next_joint.x,
                        finger.bone(0).next_joint.y,
                        finger.bone(0).next_joint.z,
                        finger.bone(0).direction.x,
                        finger.bone(0).direction.y,
                        finger.bone(0).direction.z
=======
                    data.write (",%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f" % (
                        finger.bone(i).prev_joint.x,
                        finger.bone(i).prev_joint.y,
                        finger.bone(i).prev_joint.z,
                        finger.bone(i).next_joint.x,
                        finger.bone(i).next_joint.y,
                        finger.bone(i).next_joint.z,
                        finger.bone(i).direction.x,
                        finger.bone(i).direction.y,
                        finger.bone(i).direction.z
>>>>>>> debug
                    )),
        







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
