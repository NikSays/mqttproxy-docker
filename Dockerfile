FROM alpine:latest
RUN apk add openssh py3-pip
RUN pip install pyotp
RUN adduser -HDs /bin/false user
ADD sshd_config /etc/ssh/
ADD entrypoint.sh /usr/local/bin/
ADD otp.py /opt/
ENTRYPOINT /usr/local/bin/entrypoint.sh
