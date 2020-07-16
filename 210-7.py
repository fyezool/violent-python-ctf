import socket
s = socket.socket()
s.settimeout(2)



target = 'bowneconsultingcontent.com'

s.connect((target, 80))

req = '''GET /A2.5/index.php HTTP/1.1\r
Host: bowneconsultingcontent.com\r
Connection: close\r
Cache-Control: max-age=0\r
Authorization: Basic §YWRtaW46YWRtaW4xMjMy§\r
DNT: 1\r
Upgrade-Insecure-Requests: 1\r
User-Agent: python\r
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r
Sec-Fetch-Site: none\r
Sec-Fetch-Mode: navigate\r
Sec-Fetch-User: ?1\r
Sec-Fetch-Dest: document\r
Accept-Encoding: gzip, deflate\r
Accept-Language: en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,ms;q=0.6\r
\r
'''

s.send(req.encode())
print(s.recv(1024).decode())
s.close()
