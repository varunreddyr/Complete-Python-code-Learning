#Garbage Collector:
#The main objective of Garbage collector is to destroy useless objects.
#If an object does not have any reference variable then that object eligible for Garbage collection.
# GC Modules:
# gc.isenabled()
# gc.disabled()
# gc.enabled()
import gc
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())
