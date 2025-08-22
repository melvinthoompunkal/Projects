import java.io.*;
import java.net.Socket;
import java.util.Scanner;

public class Client {

    private Socket socket;
    private BufferedReader bufferedReader;
    private BufferedWriter bufferedWriter;
    private String username;


    public Client(Socket socket, String username){
        try{
            this.socket = socket; // Assign the socket
            this.bufferedWriter = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
            this.bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            this.username = username; // Assign username
        }catch(IOException e){
            // If an error occurs during setup, close everything
            closeEverything(socket, bufferedReader, bufferedWriter);
        }
    }

    public void sendMessage(){
        try{
            bufferedWriter.write(username);
            bufferedWriter.newLine();
            bufferedWriter.flush();

            Scanner scanner = new Scanner(System.in);
            while(socket.isConnected()){
                String message = scanner.nextLine();
                bufferedWriter.write(username+ ": " + message);
                bufferedWriter.newLine();
                bufferedWriter.flush(); // Flush buffer to ensure message is sent
            }
        }catch(IOException e){
            closeEverything(socket, bufferedReader, bufferedWriter);
        }
    }

    public void listenForMessage(){
        new Thread(new Runnable(){ // Start a new thread so listening doesn't block sending
            @Override
            public void run(){
                String messageFromGroup;

                while(socket.isConnected()){
                    try{
                        messageFromGroup = bufferedReader.readLine();
                        System.out.println(messageFromGroup);
                    }catch (IOException e){
                        // Close everything if reading fails
                        closeEverything(socket, bufferedReader, bufferedWriter);
                    }
                }
            }
        }).start(); 
    }


    public void closeEverything(Socket socket, BufferedReader bufferedReader, BufferedWriter bufferedWriter){
        try{
            if(bufferedReader != null) bufferedReader.close();// close socket
            if(bufferedWriter != null) bufferedWriter.close(); //close reader
            if(socket != null) socket.close(); // Close socket if open
        }catch (IOException e){
            e.printStackTrace(); // Print stack trace if closing fails
        }
    }

    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter your username: ");
        String username = scanner.nextLine();

        Socket socket = new Socket("localhost", 1234);
        Client client = new Client(socket, username); // Create new client instance

        client.listenForMessage();
        client.sendMessage();
    }
}
