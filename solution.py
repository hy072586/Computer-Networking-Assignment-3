from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"
    mailserver = (1025, '127.0.0.1')

    clientSocket = socket(AF_INET,SOCK_STREAM)
    clientSocket.connect(mailserver)

    recv = clientSocket.recv(1024).decode()
   
    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    
    # Send MAIL FROM command and handle server response.
    clientSocket.send('Mail From:<alice@example.edu>\r\n')
    recv1=clientSocket.recv(1024)
    
    # Send RCPT TO command and handle server response.
    clientSocket.send('RCPT TO:<hy2245@nyu.edu>\r\n')
    recv1 = clientSocket.recv(1024)
   
    # Send DATA command and handle server response.
    clientSocket.send('DATA\r\n')
    recv1 = clientSocket.recv(1024)
    
    # Send message data.
    clientSocket.send('\r\n')
    clientSocket.send('something important\r\n')

    # Message ends with a single period, send message end and handle server response.
    clientSocket.send('.\r\n')
    recv1 = clientSocket.recv(1024)
    
    # Send QUIT command and handle server response.
    clientSocket.send('QUIT\r\n')
    clientSocket.close()
    pass

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
