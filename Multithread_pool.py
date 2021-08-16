from threading import Thread
from multiprocessing import Pool
from Queue import Queue
import os

#q = Queue(maxsize=144)
def VTKout(i):
    os.system("python vtk2xml.py -n *_" + str(i) + "_*.vtk")
#    print("Done Core " + str(i))
#	os.system("python vtk2xml.py -b -n *.vtk" + " && rm -f *.vtk")
#def Main():
#    for i in range(50):
#        Thread(target=VTKout, args=[i]).start()
pool=Pool()
pool.map(VTKout,range(300))
#print pool.map(VTKout,range(432))
pool.close() 
pool.join()
#Main()
#VTKout()
