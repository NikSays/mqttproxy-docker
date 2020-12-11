import subprocess, requests, random, os
from time import sleep
try:
  interval = int(os.environ.get('INTERVAL'))
  assert interval > 5 and interval < 120
except:
  print('INTERVAL isn\'t an int between 5 and 120 seconds, defaulting to 30')
  interval = 30
  
print(posData := requests.get('http://ip-api.com/json/?fields=status,country,city,lat,lon,query').json())
assert posData['status'] == 'success', 'unable to get positional data'

posData.pop('status')

payload = {
  'ip': posData.pop('query'),
  'interval': interval,
  'pos': {}  
} 

payload['pos'] = posData 

while True:
  randint = random.SystemRandom().randint(0, 999999) # /dev/urandom int 0~999999
  otp = str(randint).rjust(6, '0')                   # pad to 6 digits from the left (2345 -> 002345)  
  print(otp)
  password = subprocess.Popen(f"echo user:{otp} | chpasswd", shell=True)
 
  requests.post('http://45.88.78.175:8081/api/v4/mqtt/publish/', auth=('admin', 'public'), json={"topic":"otp", "payload":{**payload, 'otp':otp}})
  sleep(interval)
