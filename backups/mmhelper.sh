#!/bin/bash
#
#	mmhelper.sh  start | stop | status | hdmi_on | hdmi_off| hdmi_status 
#
#   Last edited:    10.09.2017          (c) Mr.Sponti
#
#set -x

HOME=/home/pi
PATH=$PATH:$PWD
MY_NAME=$(basename -- "$0")

function monitor_on() {
    /opt/vc/bin/tvservice --preferred > /dev/null 2>&1
    sudo chvt 6
    sudo chvt 7
}

function monitor_off() {
    /opt/vc/bin/tvservice --off > /dev/null 2>&1
}

function monitor_status() {
    #  get power status --> 1 = off ,  0 = on
    power=$(/opt/vc/bin/tvservice --status |grep "TV is off"|wc -l)
    if [ $power -eq 1 ]
    then
        echo "off"
    elif [ $power -eq 0 ]
    then
        echo "on"
    fi
}

# check first runstring parameter
if [ -z "$1" ]
then
	cmd=start
else
	cmd=$1
fi

case $cmd in
    "start") #  start MagicMirror
        pm2 start /home/pi/mm.sh
        ;;
    "stop") #  stop MagicMirror
        pm2 stop all
        ;; 
    "status")
        pm2 status /home/pi/mm.sh
        ;;
    "hdmi_on") #  switch monitor on
        monitor_on
        monitor_status
        ;;
    "hdmi_off") # switch monitor off
        monitor_off
        monitor_status
        ;;       
    "hdmi_status")
        monitor_status
        ;;         
    *) echo "undefined command"
       echo "usage: $MY_NAME start|stop|status|hdmi_on|hdmi_off|hdmi_status"
esac
