#! /bin/sh
a=$(ps aux | pgrep python)
 echo "= SENSYNC BASE JABAR - SUKABUMI ="
if screen -list | grep -q "SensyncBase"; then
 echo "Program is running"
else
 #sudo reboot
 echo "Program is not running"
 echo "Restart program.."
 #sudo mount /dev/sda1 /media/fd & mount /dev/sdb1 /media/fd & 
 echo 'makanminggu12' | sudo -S screen -dmS SensyncBase python /home/admin/monitor.py
 echo " "
 screen -ls
 echo " "
 echo "Use 'sudo screen -r SensyncBase' to view active screen"
 #echo "or run script view_prog -> './view_prog.sh'"
fi
