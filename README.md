# Lab 2
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- team member 1: Ishraq Rahman
- team member 2: Carrie Lei

## Lab Question Answers

Answer for Question 1: 
After adding 50% loss to our local envirment and entering the sequence on the terminal, we noticed the change in reliablility of UDP when the server does not receive all of the sequence that was sent by the client. This occurs due to possibly not requiring any connections to fully transfer information. Hence, UDP is less reliable. 

Answer for Question 2:
There was no change to the relability of TCP since the server received all of the information from the client. This occurs because its protocol ensures that all transmitting information was ditributed, hence, TCP is more reliable

Answer for Question 3:
After adding the 50% loss to our local environment, the speed of the TCP response was a bit slow. What may have caused this to occur is when there is a packet loss, it would take come time to transfer them again, which would reduce its speed. 

## TCP Server Questions 

Answer for Question 1: 
argc is an integer that counts how many arguments were entered on the command line and that will be pointed by argv. *argv[] are pointers which points to arrays of characters.

Source: (Carrie Lei)

Answer for Question 2: 
 A UNIX file descripter is a process-unique identifier   (handle) for a file or other input/output resource, such as a pipe or network socket. File descriptor table is the group of integer array indices that are file descriptors in which elements are ointers to file table entries.

Sources: 
(https://en.wikipedia.org/wiki/File_descriptor)
(https://www.geeksforgeeks.org/input-output-system-calls-c-create-open-close-read-write/)

Answer for Question 3: 
Struct is a composite data type declaration that defines a physically grouped list of variables in one place. The structure of sockaddr_in contains a short for the address family, and an unsigned short for the port number, an unsigned long with the address, and a char.
 
Source: 
(https://en.wikipedia.org/wiki/Struct_(C_programming_language)) 
(Carrie Lei)

Answer for Question 4: 
The input parameters of socket() are an integer for the domain used for communication, a communication type (tcp or udp), and a protocol value for internet protocol (IP). The function then returns a non-negative integer (named sockfd) that is a desctipter for the socket.

Sources: (
Carrie Lei)

Answer for Question 5: 
The input parameters of bind() are an integer for the socketfd, the server address pointed to by the sockaddr struct, and the length of the server address. The input parameters of listen() are an integer for the socketfd, and an integer for the backlog which defines the max length the sockfd can grow pending on connections. 

Sources: (Carrie Lei)

Answer for Question 6: 
We use while(1) because the server is always ready to accept the message from the client to create and bind to the new socket. Problems that might occur if there are multiple simultaneous connections are delats and missed packages. For instance, while the server is reading and processiong a package from one connection, it will miss / not be able to simultaneously handle an inocming package from another connection. 

Sources: (Carrie Lei)

Answer for Question 7: 
The command fork() is a way to duplicate the calling process -- it creates both a parent process, which is the original, and a child process (the duplication). The function does not have any parameters and returns an integer: 0 for when the child process is succesfully created, a positive value to the parent process that contains the ID, and a negative value when the child process fails. 

In this case, we could use fork() to better handle multiple connections by forking the newsockfd = accept() funtion. This way, there can be multiple sockets created simultaneously and accept multiple connections at once. 

Sources: (Carrie Lei)

Answer for Question 8: 
A system call is a request to the operating system to do something for the program. 

Source: (Carrie Lei)
... 
