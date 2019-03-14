"""
An example that shows how to use the motorized tilt
"""

import time
from pykinect import nui

WAIT_INTERVAL = 1.35

if __name__ == '__main__':
    with nui.Runtime() as kinect:
        cam = nui.Camera(kinect)

        while True:
            angle =input('Set an angle from -27 to 27: ')

            if angle == 'exit':
                break
            else:
                if angle.isdigit() or (angle.startswith('-') and angle[1:].isdigit()):

                    # check the angle value
                    angle = int(angle)
                    if angle > cam.ElevationMaximum:
                        angle = cam.ElevationMaximum
                    elif angle < cam.ElevationMinimum:
                        angle = cam.ElevationMinimum
                                                    
                    # move the tilt
                    cam.set_elevation_angle(angle)

                    # print immediately after elevation changed
                    print ('New elevation angle: ' + str(cam.elevation_angle))

                    # wait before moving tilt again
                    time.sleep(WAIT_INTERVAL)
