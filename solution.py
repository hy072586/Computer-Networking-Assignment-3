from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    clientSocket = socket(AF_INET,SOCK_STREAM)
    clientSocket.connect(mailserver, port)

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    connectionSocket, addr = clientSocket.accept()
    # Fill in start
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1) 
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    clientSocket.send('Mail From:<alice@crepes.edu>\r\n')
    recv1=clientSocket.recv(1024)
    print(recv1)
    if recv1[:3] != '250':
        print ('250 reply not received from server.')

    # Send RCPT TO command and handle server response.
    clientSocket.send('RCPT TO:<hy2245@nyu.edu>\r\n')
    recv1 = clientSocket.recv(1024)
    print(recv1)
    if recv1[:3] !='250':
        print('250 reply not received from server.')

    # Send DATA command and handle server response.
    clientSocket.send('DATA\r\n')
    recv1 = clientSocket.recv(1024)
    print (recv1)
    if recv1[:3] !='354':
        print('250 reply not received from server.')

    # Send message data.
    clientSocket.send('\r\n')
    clientSocket.send('something important\r\n')

    # Message ends with a single period, send message end and handle server response.
    clientSocket.send('.\r\n')
    recv1 = clientSocket.recv(1024)
    print (recv1)
    if recv1[:3] !='250':
        print('250 reply not received from server.')

    # Send QUIT command and handle server response.
    clientSocket.send('QUIT\r\n')
    clientSocket.close()
    pass

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
