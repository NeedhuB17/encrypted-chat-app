

##  How It Works (Architecture)

1. Client connects to the server using TCP sockets
2. Messages are encrypted using AES before sending
3. Each message uses a randomly generated IV for security
4. Server receives and decrypts the message
5. Server broadcasts the message to all connected clients
6. Other clients decrypt and display the message

---

##  Security Considerations

* AES encryption ensures confidentiality of messages
* CBC mode is used with proper padding (PKCS7)
* Random IV prevents pattern-based attacks
* Pre-shared key is used for simplicity

---

##  Sample Output

### Server:

[NEW CONNECTION] ('127.0.0.1', 56554)
('127.0.0.1', 56554): Hello

### Client:

You: Hello
('127.0.0.1', 56554): Hello

---

##  Key Concepts Used

* Socket Programming (TCP)
* Symmetric Encryption (AES)
* Cipher Block Chaining (CBC Mode)
* Threading (Concurrency)
* Secure Message Handling

---

##  Learning Outcomes

* Understood how encrypted communication works
* Implemented real-time client-server architecture
* Learned importance of IV in encryption
* Gained hands-on experience with Python networking and cryptography

---

##  GitHub Repository

👉 https://github.com/NeedhuB17/encrypted-chat-app

---

##  Conclusion

This project demonstrates a basic but functional secure communication system using encryption techniques. It highlights the integration of networking and cryptography concepts in a real-world scenario.
