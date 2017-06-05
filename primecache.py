import webbrowser
import threading
import sys


f = open(sys.argv[1], "r")
xs = f.readlines()
f.close()

def openstuff(i):
    webbrowser.open(xs[i])

i = 0

webbrowser.open(xs[0])

for x in range(len(xs)-1):
    i += 1
    a = threading.Lock()
    with a:
        while a.acquire(True, 5.0):
            a.wait()
        webbrowser.open(xs[i], 0, False)





