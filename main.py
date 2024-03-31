from socket import *

serverPort=9977 #Server port number to 7788
serverSocket=socket(AF_INET, SOCK_STREAM) #creating a TCP socket for incoming request
serverSocket.bind(("", serverPort)) #associate the server port number "serverPort" with this socket
serverSocket.listen(1) #The server listen for TCP connection requests from the client with 1 queued connections.
print("The web server is ready to receive!") #Print a message to tell the client that the server is ready to receive.
while True:
    connectionSocket, addr = serverSocket.accept()  # When a client sends a TCP connection request create "connectionSocket" dedicated to this client
    sentence = connectionSocket.recv(1024).decode()
    if not sentence:
        # Handle the case of an empty request
        continue  # Skip the remaining code and wait for the next request

    print(addr)
    print(sentence)
    ip = addr[0]
    port = addr[1]
    request = sentence.split()[1] if len(sentence.split()) > 1 else '/'
    print(f"The HTTP request is: {request}")  # print the HTTP request on the terminal window

    if (request == '/' or request == '/index.html' or request == '/main_en.html' or request == '/en'): # The if statement checks whether the requested object is one of several specific values
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        fileminen=open("main_en.html", "rb")
        connectionSocket.send(fileminen.read()) #read the file that was open  when it called



    elif (request == '/ar'):
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        filemainar=open("main_ar.html", "rb")
        connectionSocket.send(filemainar.read())

    elif (request.endswith('.html')):
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        filelink=open("Link.html", "rb")
        connectionSocket.send(filelink.read())

    elif (request.endswith('.css')):
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: text/css \r\n".encode())
        connectionSocket.send("\r\n".encode())
        filecss = open("cssFile.css", "rb")
        connectionSocket.send(filecss.read())


    elif (request.endswith('.png')): # files with the extensions '.png' and '.jpg'.

        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: image/png \r\n".encode())
        connectionSocket.send("\r\n".encode())
        filepngimg = open("pngImage.png", "rb")
        connectionSocket.send(filepngimg.read())

    elif (request.endswith('.jpg')):#The same process occurs for '.jpg' files,

        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Content-Type: image/jpeg \r\n".encode())
        connectionSocket.send("\r\n".encode())
        filejpgimg = open("jpgImage.jpg", "rb") #open the image with jpg extension.
        connectionSocket.send(filejpgimg.read())

    elif (request == '/yt'):

        connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("Location: https://www.youtube.com/watch?v=IAlRyJjTBIk&list=RDIAlRyJjTBIk&start_radio=1 \r\n".encode())
        connectionSocket.send("\r\n".encode())

    elif (request == '/so'):

        connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("Location: https://stackoverflow.com \r\n".encode())
        connectionSocket.send("\r\n".encode())

    elif (request == '/rt'):
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode()) #HTTP response to the client with a "307 Temporary Redirect" status code
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("Location: https://www.birzeit.edu/en \r\n".encode())
        connectionSocket.send("\r\n".encode())



    else: #scenario where a requested resource is not found by a client.
        connectionSocket.send("HTTP/1.1 404 Not Found \r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        notFoundHtmlString = "<html>" \
                             "<head>" \
                             "<title>ERROR 404 </title>" \
                             "</head>" \
                             "<div>" \
                             "Error HTTP/1.1 404 the requested resource is not found<hr>" \
                             "<p style ='font-size: 45px; text-align:center; color:Red'>" \
                             "<strong>" \
                             "<strong>"\
                                "The file is not found </strong> </p>"\
                               "<pre style ='font-size: 25px; text-align:center; color:Black'> <br>"\
                               "<b> Jenin Mansour 1200540 <br/>"\
                             " Christina Saba 1201255 <br/>" \
                             "pierre Backleh 12001296 <br/><br/><br/>" \
                             "</b>" \
                             "</pre>" \
                             "<pre style='font-size: 25px; text-align:center;'>" \
                             f"The IP is: {ip}     " \
                             f"The port is: {port}" \
                             "</pre>" \
                             "</div>" \
                             "</body>" \
                             "</html>"
        notFoundHtmlBytes = bytes(notFoundHtmlString, "UTF-8")
        connectionSocket.send(notFoundHtmlBytes)

    connectionSocket.close()  # close the connection


