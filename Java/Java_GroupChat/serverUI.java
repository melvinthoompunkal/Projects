import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.net.ServerSocket;

public class serverUI extends JFrame {
    private JTextArea logArea;
    private JButton startButton, stopButton;
    private Server server;
    private Thread serverThread;

    public serverUI() {
        setTitle("Chat Server");
        setSize(500, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        // Log area
        logArea = new JTextArea();
        logArea.setEditable(false);
        JScrollPane scrollPane = new JScrollPane(logArea);

        // Buttons
        startButton = new JButton("Start Server");
        stopButton = new JButton("Stop Server");
        stopButton.setEnabled(false);

        JPanel buttonPanel = new JPanel();
        buttonPanel.add(startButton);
        buttonPanel.add(stopButton);

        add(scrollPane, BorderLayout.CENTER);
        add(buttonPanel, BorderLayout.SOUTH);

        // Action listeners
        startButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                startServer();
            }
        });

        stopButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                stopServer();
            }
        });
    }

    private void startServer() {
        try {
            ServerSocket serverSocket = new ServerSocket(1234);
            server = new Server(serverSocket) {
                @Override
                public void startServer() {
                    try {
                        while (!serverSocket.isClosed()) {
                            var socket = serverSocket.accept();
                            appendLog("New client connected: " + socket.getInetAddress());

                            ClientHandler clientHandler = new ClientHandler(socket);
                            Thread thread = new Thread(clientHandler);
                            thread.start();
                        }
                    } catch (IOException e) {
                        appendLog("Server stopped or error: " + e.getMessage());
                    }
                }
            };

            serverThread = new Thread(() -> server.startServer());
            serverThread.start();

            appendLog("Server started on port 1234");
            startButton.setEnabled(false);
            stopButton.setEnabled(true);

        } catch (IOException e) {
            appendLog("Failed to start server: " + e.getMessage());
        }
    }

    private void stopServer() {
        if (server != null) {
            server.closeServerSocket();
            server = null;
            appendLog("Server stopped.");
            startButton.setEnabled(true);
            stopButton.setEnabled(false);
        }
    }

    private void appendLog(String message) {
        SwingUtilities.invokeLater(() -> {
            logArea.append(message + "\n");
        });
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new serverUI().setVisible(true);
        });
    }
}
