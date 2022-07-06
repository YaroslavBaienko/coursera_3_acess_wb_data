import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

#for line in fhand:
#    print(line.decode().strip())
 
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)




#import socket

#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.connect(('data.pr4e.org', 80))
#cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
#mysock.send(cmd)

#while True:
#    data = mysock.recv(512)
#    print(data)
#    if (len(data) < 1):
#        break
#    print(data.decode())
#mysock.close()

#print(ord('i'))
