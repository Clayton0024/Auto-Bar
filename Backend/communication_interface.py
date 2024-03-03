from abc import ABC, abstractmethod
import json
from typing import Callable
import socket
import threading


class CommunicationInterface(ABC):
    """
    This class defines the interface for the communication between the backend and the frontend.
    At the most basic level, this needs to be initialized, started, stopped, send messages
    The implementation is responsible for receiving messages and doing something with them.
    """

    @abstractmethod
    def start(self):
        """
        Start the communication interface.
        """
        pass

    @abstractmethod
    def stop(self):
        """
        Stop the communication interface.
        """
        pass

    @abstractmethod
    def send_message(self, message: dict):
        """
        Send a message to the frontend.
        Message must be a dictionary, which will be converted to JSON.
        """
        pass


class TcpCommunicator(CommunicationInterface):
    """
    A TCP communicator.

    Parameters:
        host: The host to listen on
        port: The port to listen on
        on_message_received: A callback function that will be called when a message is received.
            The callback function should take a single parameter, which will be a dictionary
            containing the received message.

    Example usage:
        communicator = TcpCommunicator("127.0.0.1", 6969, on_message_received)
        communicator.start()
        communicator.send_message({"message": "Hello world!"})
        communicator.stop()
    """

    def __init__(self, host: str, port: int, on_message_received: Callable[[dict], None]):
        """
        Initialize the TCP communicator.
        """
        self._host = host
        self._port = port
        self._on_message_received = on_message_received
        self._server_socket = None
        self._stop_flag = threading.Event()

    def _start_server(self) -> bool:
        # Create a TCP server socket
        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # Bind the socket to the specified host and port
            self._server_socket.bind((self._host, self._port))

            # Start listening for incoming connections
            self._server_socket.listen()

            print(f"Server listening on {self._host}:{self._port}")

            # Accept incoming connections in a loop
            while not self._stop_flag.is_set():
                # Wait for a connection
                connection, client_address = self._server_socket.accept()
                print(f"Connection from {client_address}")
                self._handle_connection(connection)
                return True
        except Exception as e:
            print(f"Error in _start_server: {e}")
            return False

    def start(self):
        """
        Start the TCP communicator.
        """
        # Create a TCP server socket
        threading.Thread(target=self._start_server, daemon=True).start()

    def _handle_connection(self, connection):
        """
        Handle an incoming connection.
        """
        try:
            # Receive data in a loop until the connection is closed
            while not self._stop_flag.is_set():
                data = connection.recv(1024)
                if not data:
                    break

                # Decode the received data as JSON
                message = json.loads(data.decode("utf-8"))

                # Call the callback with the received message
                self._on_message_received(message)

        except Exception as e:
            print(f"Error in _handle_connection: {e}")

        finally:
            # Clean up the connection
            connection.close()

    def stop(self):
        """
        Stop the TCP communicator.
        """
        self._stop_flag.set()
        if self._server_socket:
            self._server_socket.close()

    def send_message(self, message: dict):
        """
        Send a message to the frontend.
        Message must be a dictionary, which will be converted to JSON.
        """
        # Implementation of sending a message to the client (frontend) goes here
        json_message = json.dumps(message)
        print(f"Sending message: {json_message}")

        pass


if __name__ == "__main__":
    import time

    def tcp_client(host, port, message):
        # Create a TCP client socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            print("Connecting to server")
            # Connect to the server
            client_socket.connect((host, port))

            # Send a message to the server
            json_message = json.dumps(message)
            client_socket.sendall(json_message.encode("utf-8"))

        except Exception as e:
            print(f"Error in tcp_client: {e}")

        finally:
            # Clean up the connection
            client_socket.close()

    # Create a TCP communicator
    communicator = TcpCommunicator(
        "127.0.0.1", 6969, lambda message: print(f"Received message: {message}")
    )
    communicator.start()
    print("Communicator started")
    time.sleep(1)

    client_message = {"client_message": "Hello from client!"}
    print("Sending message from client")
    tcp_client("127.0.0.1", 6969, client_message)

    # Wait for a moment to allow the server to receive the message
    time.sleep(1)

    communicator.stop()
