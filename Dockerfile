FROM alpine:3.12.1
RUN apk add --no-cache openssh python3 py3-requests fail2ban
RUN adduser -HDs /bin/false user
ADD sshd_config /etc/ssh/
ADD entrypoint.sh /usr/local/bin/
ADD otp.py /opt/
ENTRYPOINT /usr/local/bin/entrypoint.sh
