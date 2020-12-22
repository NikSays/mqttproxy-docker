#!/bin/sh
if [[ ! -f /opt/keys/ssh_host_rsa_key  ]]; then
  ssh-keygen -q -t rsa -f /opt/keys/ssh_host_rsa_key -N ""
  ssh-keygen -q -t ecdsa -f /opt/keys/ssh_host_ecdsa_key -N ""
  ssh-keygen -q -t ed25519 -f /opt/keys/ssh_host_ed25519_key -N ""
fi
/sbin/syslogd
/usr/sbin/sshd
/usr/bin/fail2ban-server 1> /dev/null
/usr/bin/fail2ban-client set sshd bantime ${BAN_TIME-12h} 1> /dev/null
/usr/bin/fail2ban-client set sshd maxretry ${BAN_ATTEMPTS-5} 1> /dev/null
/usr/bin/fail2ban-client set sshd findtime ${BAN_FIND_INTERVAL-10m} 1> /dev/null
/usr/bin/tor -f /etc/tor/torrc & \
/opt/adguardhome/AdGuardHome -h 0.0.0.0 -c /opt/adguardhome/conf/AdGuardHome.yaml -w /opt/adguardhome/work --no-check-update &\
python3 -u /opt/otp.py 
