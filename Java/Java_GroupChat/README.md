# Java Chat Application

A simple multithreaded **Client-Server Chat Application** built in Java.  
This project demonstrates socket programming, multithreading, and a Swing-based UI for sending and receiving chat messages.

---

##  Features
- **Server**
  - Accepts multiple client connections using threads
  - Broadcasts messages from one client to all connected clients
- **Client**
  - Swing UI with a chat window
  - Send messages via button or Enter key
  - Displays messages from all connected users in real-time
- **Networking**
  - Uses `Socket` and `ServerSocket` for TCP communication
  - Buffered I/O streams for efficient message handling

---

## Project Structure


├── Server.java          # Runs the server, accepts client connections
├── ClientHandler.java   # Handles each client on its own thread
├── Client.java          # Console-based client (from WittCode tutorial)
├── ClientUI.java        # GUI client (Swing-based, my extension)



---

## How to Run
1. **Start the server**  
   ```bash
   javac Server.java ClientHandler.java
   java Server


The server will listen on port **1234**.

2. **Start a client**

   ```bash
   javac ClientUI.java
   java ClientUI
   ```

   * Enter a username when prompted.
   * Multiple clients can be started (each in a new terminal/window).

3. **Chat!**

   * Type messages in the client window.
   * Messages are broadcast to all connected clients.

---

## Technologies

* Java (JDK 8+)
* Swing (UI framework)
* Multithreading (`Thread`)
* Socket Programming (`Socket`, `ServerSocket`)

---

## Future Improvements

* Add authentication (username/password login)
* Show list of online users
* Save chat logs to a file or database
* Encryption for secure messaging
* Improved UI (colors, formatting, notifications)

---

## Credits

The base client-server chat project was created by [**WittCode**](https://www.youtube.com/@WittCode) in his tutorial:
[Java Socket Programming - Build a Chat Application](https://www.youtube.com/watch?v=gLfuZrrfKes&ab_channel=WittCode).

This repository builds on that foundation with additional features such as a Swing-based graphical client.

```

---

The base code of the server, client, and clientHandler are from WittCode and I used it to learn how sockets work as well as threading. This project helped me take a deeper dive into threading practices.
The serverUI and clientUI were done by me through research and looking through different sources. 
```
