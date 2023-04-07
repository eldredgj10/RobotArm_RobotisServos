import time

def rest(poppy):
    
    poppy.m1.goto_position(0, 1.5, wait=True)
    poppy.m2.goto_position(-90, 1.5, wait=True)
    poppy.m3.goto_position(90, 1.5, wait=True)
    poppy.m4.goto_position(0, 1.5, wait=True)
    poppy.m5.goto_position(0, 1.5, wait=True)
    poppy.m6.goto_position(0, 1.5, wait=True)
