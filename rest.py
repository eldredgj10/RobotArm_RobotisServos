from poppy_ergo_jr import PoppyErgoJr
import time



def rest(poppy):


	poppy.m1.compliant = False
	poppy.m2.compliant = False
	poppy.m3.compliant = False
	poppy.m4.compliant = False
	poppy.m5.compliant = False
	poppy.m6.compliant = False


	#for m in poppy.motors:
	#	poppy.m.goto_position(0, 0.5, wait=True)

	poppy.m1.goto_position(0, 0.5, wait=True)
	poppy.m2.goto_position(-90, 0.5, wait=True)
	poppy.m3.goto_position(90, 0.5, wait=True)
	poppy.m4.goto_position(0, 0.5, wait=True)
	poppy.m5.goto_position(0, 0.5, wait=True)
	poppy.m6.goto_position(0, 0.5, wait=True)
