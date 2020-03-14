import subprocess

initial = 0

print("<Any key to toggle>")

while (True):
 input()

 if initial == 0:
  initial = 1
  print("Start")
  subprocess.run(['/home/pi/mmhelper.sh', 'start'],
                         stdout=subprocess.PIPE,
                         universal_newlines=True)
  print("Done")
 else:
  initial = 0
  print("Stop")
  subprocess.run(['/home/pi/mmhelper.sh', 'stop'])
  print("Done")
