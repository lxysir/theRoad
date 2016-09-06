#!usr/bin/sh
# test remote host port is open or not for mobileiron core and sentry

#TCP port
nc -w 1 mobileironcore.cn.ab-inbev.com 443 && echo true || echo false
nc -w 1 mobileironsentry.cn.ab-inbev.com 443 && echo true || echo false
nc -w 1 58.247.12.146 443 && echo true || echo false
#core
58.247.12.146
116.236.250.155
#sentry
58.247.12.145
116.236.250.154
#UDP port
nc -w 1 -u mobileironsentry.cn.ab-inbev.com 8080 && echo true || echo false
nc -w 1 -u mobileironsentry.cn.ab-inbev.com 9997 && echo true || echo false