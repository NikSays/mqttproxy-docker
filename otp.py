import subprocess, requests, random, os
from time import sleep
try:
  interval = int(os.environ.get('INTERVAL'))  #Interval is an int 5..120
  assert interval >= 5 and interval <= 120
except:
  print('INTERVAL isn\'t an int between 5 and 120 seconds, defaulting to 30')
  interval = 30
  
print(posData := requests.get('http://ip-api.com/json/?fields=status,country,city,lat,lon,query').json()) #get positional data
assert posData.pop('status') == 'success', 'ERROR: unable to get positional data'

ip = posData.pop("query")

payload = {
  'interval': interval,
  **posData
} 

while True:
  randint = random.SystemRandom().randint(0, 999999) # /dev/urandom int 0~999999
  otp = str(randint).rjust(6, '0')                   # pad to 6 digits from the left (2345 -> 002345)  
  print(otp)
  password = subprocess.Popen(f"echo user:{otp} | chpasswd", shell=True)
 
  requests.post(f"http://end2end.network/api/otp/{ip}", json={**payload, 'otp':otp})
  sleep(interval)
