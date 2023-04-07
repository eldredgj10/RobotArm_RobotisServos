import wave_1
import smile
import rest
import time
import pypot
import stand
from poppy_ergo_jr import PoppyErgoJr
poppy = PoppyErgoJr(camera='dummy')


#Awake Motors and strengthen them so they can't be turned by hand
for m in poppy.motors:
		m.compliant = False
        
stand.stand(poppy)


while True:
    inString = input("Enter a command: ")
    if inString == ':)':
        smile.smile(poppy)
    elif inString == "wave":
        wave_1.wave(poppy)
    elif inString == 'rest':
        rest.rest(poppy)
    elif inString == 'esc':
        break
    else:
        for m in poppy.motors:
            m.led = 'red'
            time.sleep(0.2)
            m.led = 'off'
