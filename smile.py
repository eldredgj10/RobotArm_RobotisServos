import time
import numpy
import stand
def smile(poppy):
    #markers = detect_markers(image)
    #for m in markers:
        #m.draw_contour(image)
        
    stand.stand(poppy)
    for m in poppy.motors:
            m.led = 'green'
            time.sleep(0.2)
            m.led = 'off'
    
    #time.sleep(3)
    poppy.dance.start()
    time.sleep(10)
    poppy.dance.stop()
    
    stand.stand(poppy)

