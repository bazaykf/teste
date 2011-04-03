import socket
 
# Set the socket parameters
host = "127.0.0.1"
port = 5000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
nome=raw_input('introduza nome:\t')
addr = (host,port)
tcp.connect(addr)
 
 
def_msg = "===introduza o texto===";
print "\n",def_msg
 
# Send messages
data = raw_input(nome+'>> ')
while data <> '\x18':
    data=nome+' diz:\t'+data
    tcp.send(data)
    data = raw_input(nome+'>> ')
tcp.close()
