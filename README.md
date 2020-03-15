# My Raspberry pi mirror app
## Requirements
1) Need to have both a mm.sh and mmhelper.sh file located in `/home/pi/`
Can almost directly from https://forum.magicmirror.builders/topic/5831/quit-mm-with-script/2
but may need to change file mm.sh to full path
2) Change button/led pin #'s accordinly in rasp.py

## To run in background
Run `nohup /home/pi/Documents/code/rasp.py &`
## To kill
Find PID by running `ps ax | grep rasp.py`
Then run `kill <PID>`

