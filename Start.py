from enum import Enum, auto
from work import Work
import time
class states(Enum):
    idle = auto() 
    wander = auto()
    work = auto() 
   
state = states.idle
for i in range(5):
    if(state == states.idle):
        state = states.wander
        print(state)
        

    elif(state == state.wander):
        state = state.work
        print(state)
        time.sleep(3)
        

    elif(state == states.work):
        for i in range(50000):
            state = state.idle
            coc = Work('1.png')
            coc.work_start()
            coc = Work('2.png')
            coc.work_start()
            coc = Work('3.png')
            coc.work_start()
            coc = Work('4.png')
            coc.work_start()
            coc = Work('5.png')
            coc.work_start()
            coc = Work('6.png')
            coc.work_start()
            coc = Work('7.png')
            coc.work_start()
            coc = Work('8.png')
            coc.work_start()
            coc = Work('9.png')
            coc.work_start()
            coc = Work('10.png')
            coc.work_start()
            coc = Work('11.png')
            coc.work_start()
            coc = Work('12.png')
            coc.work_start()
            coc = Work('13.png')
            coc.work_start()
            coc = Work('14.png')
            coc.work_start()
            coc = Work('15.png')
            coc.work_start()
            coc = Work('16.png')
            coc.work_start()
            coc = Work('17.png')
            coc.work_start()
            coc = Work('18.png')
            coc.work_start()
            coc = Work('19.png')
            coc.work_start()
            coc = Work('20.png')
            coc.work_start()
        coc4.work_start()
        print(state)
        time.sleep(3)
    


