import time
import os


class StopWatchApp:

    def stopWatch(self):
        minutes = 0
        sec = 0
        hours = 0
        while (True):
            print("Stopwatch project by (Tushar Nitin Bhansali)")
            print("r:Resume,R:Reset,P:Pause,C:Close")
            print("\n")
            print("-------------")
            print("%d:%d:%d" % (hours, minutes, sec))
            print("--------------")
            time.sleep(1)
            sec += 1
            if (sec == 60):
                sec = 0
                minutes += 1
            if (minutes == 60):
                minutes = 0
                hours += 1
            os.system('cls')

    def reset(self):
        self.t.set('0:0:0')

    def resume(self):
        self.stopWatch()

    def pause(self):
        self.stopWatch()

    def close(self):
        self.root.display()


a = StopWatchApp
a.stopWatch()
