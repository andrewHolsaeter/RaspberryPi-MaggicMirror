# My Raspberry pi mirror app
## Requirements
1) Need to have both a mm.sh and mmhelper.sh file located in `/home/pi/`
Can almost directly from https://forum.magicmirror.builders/topic/5831/quit-mm-with-script/2
but may need to change file mm.sh to full path
2) Change button/led pin #'s accordinly in rasp.py

## To run in background
TODO / Problem: When this is called more than once, things get thrown off when one of them is killed 
Run `nohup /home/pi/Documents/code/rasp.py &`
## To kill
1) Find PID by running `ps ax | grep rasp.py`
2) Then run `kill <PID>`

