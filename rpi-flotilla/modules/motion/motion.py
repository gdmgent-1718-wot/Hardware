import time

import flotilla

dock = flotilla.Client()
motion = dock.first(flotilla.Motion)

MOTION_INFO = "x={x}, y={y}, z={z}"

try:
    while True:
        print(MOTION_INFO.format(
            x=motion.x,
            y=motion.y,
            z=motion.z))
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping Flotilla...")
    dock.stop()
