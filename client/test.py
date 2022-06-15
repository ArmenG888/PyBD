import socket

result = socket.getaddrinfo("https://api6.ipify.org", 80, socket.AF_INET6)
print(result)