#from module import method1, method2...
#from module import *
import time as z                            # Module 'time' is imposted as 'z'
print(z.strftime('%Y-%m-%d  %H:%M:%S'))

#from time import *
from time import strftime                   # 'strftime' can be Method/Class defined in 'time' Module
print(strftime('%D'))

#import time.strftime as z                  # Gives error as time is not package
from time import strftime as z
print(z('%D'))
