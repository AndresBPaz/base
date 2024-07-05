from MicroWebSrv2 import MicroWebSrv2
import os

class MiServidorWeb:
    """
    Class to create and manage a MicroWebSrv2 server in MicroPython.

    Provides methods for:
        - Server configuration (port, web root, etc.)
        - Route handling (binding URLs to specific functions)
        - Server startup and polling
    """

    def __init__(self, port=80, web_path="/www", max_websocket_recv_len=256):
        """
        Initializes the server object with default values.

        Args:
            port (int, optional): Port number for the server (default 80).
            web_path (str, optional): Path to the web root directory (default "/www").
            max_websocket_recv_len (int, optional): Maximum WebSocket receive buffer size (default 256).
        """

        self.port = port
        self.web_path = web_path
        self.max_websocket_recv_len = max_websocket_recv_len
        self.server = None  # Initialize server instance within the constructor

    def configurar_servidor(self):
        """
        Configures the server with port, web root, and maximum WebSocket receive buffer size.
        """

        self.server = MicroWebSrv2(webPath=self.web_path)
        self.server.MaxWebSocketRecvLen = self.max_websocket_recv_len

    def manejar_solicitud(self, request, response):
        """
        Handles incoming requests and serves HTML files from the "web_files" folder.

        Args:
            request (object): MicroWebSrv2 request object
            response (object): MicroWebSrv2 response object
        """

        if request.Path == "/web_files/":
            # Serve the index.html file for the root path
            try:
                with open(os.path.join(self.web_path, "web_files", "index.html"), "r") as f:
                    html_content = f.read()
                response.WriteResponseOk(contentType="text/html", contentCharset="UTF-8", content=html_content)
            except OSError:
                response.WriteResponse(status="404 Not Found")

        else:
            # Handle other request paths (e.g., "/about", "/data")
            # with appropriate responses
            response.WriteResponse(status="404 Not Found")


    def ejecutar(self):
        """
        Starts the server, binds the request handler to the root path ("/"),
        and enters a loop to poll for incoming requests.
        """

        self.configurar_servidor()  # Ensure server configuration before starting
        self.server.BindRoute("/", self.manejar_solicitud)  # Bind handler to root path
        self.server.Start(threaded=True)  # Start the server in a separate thread

        while True:
            self.server.Poll()  # Wait for and handle incoming requests

# Example usage:
# mi_servidor = MiServidorWeb()
# mi_servidor.ejecutar()
