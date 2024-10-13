import socket

class GDTSender:
    def __init__(self, host, port):
        """
        Initialize the GDTConnection with the specified host and port.

        Parameters:
        host (str): The hostname or IP address of the medical device.
        port (int): The port number to connect to.
        """
        self.host = host
        self.port = port
        self.socket = None
        self.connected = False

    def connect(self):
        """Establish a connection to the medical device."""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            self.connected = True
            print(f"Connected to {self.host}:{self.port}")
        except Exception as e:
            print(f"Failed to connect: {e}")

    def sendMessage(self, message):
        """
        Send a GDT message to the connected device.

        Parameters:
        message (str): The GDT message to send.
        """
        if not self.connected:
            print("Connection is not established.")
            return
        
        try:
            self.socket.sendall(message.encode('utf-8'))
            print("Message sent successfully.")
        except Exception as e:
            print(f"Failed to send message: {e}")

    def receiveMessage(self, buffer_size=16000):
        """
        Receive a GDT message from the connected device.

        Parameters:
        buffer_size (int): The size of the buffer to use for receiving data.

        Returns:
        str: The received message.
        """
        if not self.connected:
            print("Connection is not established.")
            return None
        
        try:
            data = self.socket.recv(buffer_size)
            message = data.decode('utf-8')
            print("Message received successfully.")
            return message
        except Exception as e:
            print(f"Failed to receive message: {e}")
            return None

    def close(self):
        """Close the connection to the medical device."""
        if self.socket:
            self.socket.close()
            self.connected = False
            print("Connection closed.")

class GDTReceiver:
    def __init__(self, host, port):
        """
        Initialize the GDTConnection with the specified host and port.

        Parameters:
        host (str): The hostname or IP address of the medical device.
        port (int): The port number to connect to.
        """
        self.host = host
        self.port = port
        self.socket = None
        self.running = False

    def startListener(self):
        """Establish a connection to the medical device."""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.bind((self.host, self.port))
            self.socket.listen(1)
            self.running = True
            print(f"Connected to {self.host}:{self.port}")
        except Exception as e:
            print(f"Failed to connect: {e}")
    
    def receiveMessage(self):
        print('waiting for a connection')
        if self.socket and self.running:
            connection , clinet_address = self.socket.accept()
            data = connection.recv(16000)
            print(data)
            

    def close(self):
        if self.socket:
            self.socket.close()
            self.connected = False
            print("Connection Closed")

    
