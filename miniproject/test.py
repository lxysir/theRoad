import time
import webbrowser

total_breaks = 3
break_count = 0

while(break_count < total_breaks):
    print("It's break time on:", time.ctime())
    time.sleep(5)
    webbrowser.open("http://www.baidu.com")
    break_count += 1
