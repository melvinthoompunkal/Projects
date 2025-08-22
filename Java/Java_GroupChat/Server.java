import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
    private ServerSocket serverSocket; // The server socket that listens for incoming client connections

    
    public Server(ServerSocket serverSocket){
        this.serverSocket = serverSocket;
    }

   
    public void startServer(){
        try{
           
            while(!serverSocket.isClosed()){
                Socket socket = serverSocket.accept(); n
                System.out.println("A new client has connected"); 
                ClientHandler clientHandler = new ClientHandler(socket); // Create a handler for this client

                Thread thread = new Thread(clientHandler); // Wrap the client handler in a new thread
                thread.start(); 
            }
        } catch (IOException e){
            e.printStackTrace();
        }
    }

    public void closeServerSocket(){
        try{
            if (serverSocket != null){
                serverSocket.close(); // Close the server socket to stop accepting clients
            }
        } catch (IOException e){
            e.printStackTrace(); 
        }
    }

    // Main method to start the server
    public static void main(String[] args) {
        try {
            ServerSocket serverSocket = new ServerSocket(1234); 
            Server server = new Server(serverSocket); 
            server.startServer(); 
        } catch (IOException e) {
            e.printStackTrace(); 
        }
    }
}
