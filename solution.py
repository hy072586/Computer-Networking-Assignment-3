from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"
    mailserver = ('127.0.0.1', 1025)

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mailserver)

    recv = clientSocket.recv(1024)

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024)

    # Send MAIL FROM command and handle server response.
    mailfrom = "MAIL FROM:<alice@example.edu>\r\n"
    clientSocket.send(mailfrom.encode())
    recv1 = clientSocket.recv(1024)

    # Send RCPT TO command and handle server response.
    rcptTo = "RCPT TO:<hy2245@nyu.edu>\r\n"
    clientSocket.send(rcptTo.encode())
    recv1 = clientSocket.recv(1024)

    # Send DATA command and handle server response.
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    recv1 = clientSocket.recv(1024)

    # Send message data.
    subject = "Subject: SMTP mail client testing \r\n\r\n"
    clientSocket.send(subject.encode())
    message = "Enter your message: \r\n"
    clientSocket.send(message.encode())
    clientSocket.send(msg.encode())
    recv_msg = clientSocket.recv(1024)

    # Message ends with a single period, send message end and handle server response.
    clientSocket.send(endmsg.encode())
    recv1 = clientSocket.recv(1024)

    # Send QUIT command and handle server response.
    clientSocket.send('QUIT\r\n')
    clientSocket.close()
    pass

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
