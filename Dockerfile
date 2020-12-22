FROM adguard/adguardhome:latest
RUN apk add --no-cache openssh python3 py3-requests fail2ban tor
RUN chmod 700 /var/lib/tor
RUN adduser -HDs /bin/false user
ADD torrc /etc/tor/
ADD sshd_config /etc/ssh/
ADD entrypoint.sh /usr/local/bin/
ADD otp.py /opt/
ENTRYPOINT /usr/local/bin/entrypoint.sh
