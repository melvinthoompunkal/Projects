import java.io.*;
import java.net.Socket;
import java.util.ArrayList;

public class ClientHandler implements Runnable{


    public static ArrayList<ClientHandler> clientHandlers = new ArrayList<>();

    private Socket socket;
    private BufferedReader bufferedReader;
    private BufferedWriter bufferedWriter;
    private String clientUsername;


    public ClientHandler(Socket socket){
        try{
            this.socket = socket; // Assign the client socket
            this.bufferedWriter = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream())); // Initialize writer to send messages
            this.bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream())); // Initialize reader to receive messages
            this.clientUsername = bufferedReader.readLine(); // Read the client's username from the first message
            clientHandlers.add(this); // Add this client to the global list
            broadcastMessage("SERVER: " + clientUsername + " has entered the chat!"); // Notify all other clients
        }catch(IOException e){
            closeEverything(socket, bufferedReader, bufferedWriter); // Close everything if initialization fails
        }
    }

    @Override
    public void run() {
        String messageFromClient;

        // Keep reading messages while the client socket is connected
        while(socket.isConnected()){
            try{
                messageFromClient = bufferedReader.readLine(); // Read a message from the client
                broadcastMessage(messageFromClient); // Send it to all other clients
            }catch(IOException e){
                closeEverything(socket, bufferedReader, bufferedWriter); // Close connection if reading fails
                break; // Exit the loop after closing
            }
        }
    }

    // Broadcast a message to all clients except the sender
    public void broadcastMessage(String message){
        if(message == null) return; // Ignore null messages (client disconnected)

        for(ClientHandler clientHandler : clientHandlers){
            try{
                if(!clientHandler.clientUsername.equals(clientUsername)){ // Skip the sender
                    clientHandler.bufferedWriter.write(message); // Send the message
                    clientHandler.bufferedWriter.newLine(); // Add a newline
                    clientHandler.bufferedWriter.flush(); // Flush to ensure it's sent immediately
                }
            }catch(IOException e){
                // Close this client if sending fails
                closeEverything(clientHandler.socket, clientHandler.bufferedReader, clientHandler.bufferedWriter);
            }
        }
    }

    // Remove this client from the list and notify others
    public void removeClientHandler(){
        clientHandlers.remove(this); // Remove from global list
        if(clientUsername != null){
            broadcastMessage("SERVER: " + clientUsername + " has left the chat :("); // Notify remaining clients
        }
    }

    // Close socket, reader, and writer safely
    public void closeEverything(Socket socket, BufferedReader bufferedReader, BufferedWriter bufferedWriter){
        try{
            if(bufferedReader != null) bufferedReader.close();
            if(bufferedWriter != null) bufferedWriter.close();
            if(socket != null) socket.close();
        }catch(IOException e){
            e.printStackTrace(); // Print error if closing fails
        }
        removeClientHandler(); // Remove client from list after closing streams
    }
}
