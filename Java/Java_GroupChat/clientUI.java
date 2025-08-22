import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;
import java.net.Socket;

public class ClientUI extends JFrame {
    private JTextArea chatArea;
    private JTextField inputField;
    private JButton sendButton;
    private BufferedReader bufferedReader;
    private BufferedWriter bufferedWriter;
    private Socket socket;
    private String username;

    public ClientUI(Socket socket, String username) {
        this.socket = socket;
        this.username = username;

        try {
            bufferedWriter = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
            bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        } catch (IOException e) {
            e.printStackTrace();
            closeEverything(socket, bufferedReader, bufferedWriter);
        }


        setTitle("Chat - " + username);
        setSize(500, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        chatArea = new JTextArea();
        chatArea.setEditable(false);
        JScrollPane scrollPane = new JScrollPane(chatArea);

        inputField = new JTextField(30);
        sendButton = new JButton("Send");

        JPanel bottomPanel = new JPanel(new BorderLayout());
        bottomPanel.add(inputField, BorderLayout.CENTER);
        bottomPanel.add(sendButton, BorderLayout.EAST);

        add(scrollPane, BorderLayout.CENTER);
        add(bottomPanel, BorderLayout.SOUTH);

        // Send button action
        sendButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                sendMessage();
            }
        });

        // Enter key also sends message
        inputField.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                sendMessage();
            }
        });

        // Start a thread to listen for messages
        new Thread(() -> listenForMessage()).start();
    }

    private void sendMessage() {
        String messageToSend = inputField.getText().trim();
        if (!messageToSend.isEmpty()) {
            try {
                bufferedWriter.write(username + ": " + messageToSend);
                bufferedWriter.newLine();
                bufferedWriter.flush();
                chatArea.append("Me: " + messageToSend + "\n");
                inputField.setText("");
            } catch (IOException e) {
                e.printStackTrace();
                closeEverything(socket, bufferedReader, bufferedWriter);
            }
        }
    }

    private void listenForMessage() {
        String msgFromChat;
        while (socket.isConnected()) {
            try {
                msgFromChat = bufferedReader.readLine();
                if (msgFromChat != null) {
                    chatArea.append(msgFromChat + "\n");
                }
            } catch (IOException e) {
                closeEverything(socket, bufferedReader, bufferedWriter);
                break;
            }
        }
    }

    private void closeEverything(Socket socket, BufferedReader bufferedReader, BufferedWriter bufferedWriter) {
        try {
            if (bufferedReader != null) bufferedReader.close();
            if (bufferedWriter != null) bufferedWriter.close();
            if (socket != null) socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // Entry point for testing
    public static void main(String[] args) {
        try {
            String username = JOptionPane.showInputDialog("Enter username:");
            Socket socket = new Socket("localhost", 1234);
            ClientUI clientUI = new ClientUI(socket, username);
            clientUI.setVisible(true);

            clientUI.bufferedWriter.write(username);
            clientUI.bufferedWriter.newLine();
            clientUI.bufferedWriter.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
