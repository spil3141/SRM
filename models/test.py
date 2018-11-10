import sys 
sys.path.insert(1,'../dependencies/lib-mac')
sys.path.insert(0,'../dependencies/lib-mac/Leap.py')
import Leap, thread, time
#from sklearn.externals import joblib
import pandas as pd

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
        data = open("r-time.csv", 'wb')
        # Get hands
        for hand in frame.hands:
            # Get the hand's and direction
            direction = hand.direction
            # Get fingers
            data.write("4,34.95,107.01,145.27,34.95,107.01,145.27,0.00,0.00,0.00,34.95,107.01,145.27,34.95,107.01,145.27,0.00,0.00,0.00,34.95,107.01,145.27,34.95,107.01,145.27,0.00,0.00,0.00,34.95,107.01,145.27,34.95,107.01,145.27,0.00,0.00,0.00,45.54,123.21,134.89,10.77,133.05,77.12,0.51,-0.14,0.85,45.54,123.21,134.89,10.77,133.05,77.12,0.51,-0.14,0.85,45.54,123.21,134.89,10.77,133.05,77.12,0.51,-0.14,0.85,45.54,123.21,134.89,10.77,133.05,77.12,0.51,-0.14,0.85,54.74,121.39,128.40,29.07,127.89,69.46,0.40,-0.10,0.91,54.74,121.39,128.40,29.07,127.89,69.46,0.40,-0.10,0.91,54.74,121.39,128.40,29.07,127.89,69.46,0.40,-0.10,0.91,54.74,121.39,128.40,29.07,127.89,69.46,0.40,-0.10,0.91,63.74,116.83,123.14,48.34,119.58,67.27,0.27,-0.05,0.96,63.74,116.83,123.14,48.34,119.58,67.27,0.27,-0.05,0.96,63.74,116.83,123.14,48.34,119.58,67.27,0.27,-0.05,0.96,63.74,116.83,123.14,48.34,119.58,67.27,0.27,-0.05,0.96,71.09,106.25,120.35,64.49,108.06,67.08,0.12,-0.03,0.99,71.09,106.25,120.35,64.49,108.06,67.08,0.12,-0.03,0.99,71.09,106.25,120.35,64.49,108.06,67.08,0.12,-0.03,0.99,71.09,106.25,120.35,64.49,108.06,67.08,0.12,-0.03,0.99\n")
            data.write("4"),
            for finger in hand.fingers:
                # Get bones
                for i in range(0,4):
                    data.write (",%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f" % (
                        finger.bone(0).prev_joint.x,
                        finger.bone(0).prev_joint.y,
                        finger.bone(0).prev_joint.z,
                        finger.bone(0).next_joint.x,
                        finger.bone(0).next_joint.y,
                        finger.bone(0).next_joint.z,
                        finger.bone(0).direction.x,
                        finger.bone(0).direction.y,
                        finger.bone(0).direction.z
                    )),
            data.write ("\n")
        data.close()
        """data = pd.read_csv('r-time.csv')
        if data != NULL:
            print (data.values.shape)"""






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
