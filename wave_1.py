import time
import stand

def wave(poppy):
    
    # Rotate the motors back to the initial position
    
    stand.stand(poppy)

    # Move the arm up
    poppy.m2.goto_position(22, 0.5, wait=True)
    #time.sleep(0.5)

    # Move the arm down
    poppy.m2.goto_position(-30, 0.5, wait=True)
    #time.sleep(0.5)

    # Move the arm up again
    poppy.m2.goto_position(22, 0.5, wait=True)
    #time.sleep(0.5)

    # Move the arm down and rotate the motors to wave
    poppy.m2.goto_position(-30, 0.5, wait=True)

    poppy.m1.goto_position(0, 0.5, wait=True)
    poppy.m3.goto_position(0, 0.5, wait=True)
    #time.sleep(0.5)

    # Rotate the motors back to the initial position
    stand.stand(poppy)
