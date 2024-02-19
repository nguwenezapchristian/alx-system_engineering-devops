# Command line for the win Challenge


#Description

This repo is for the command line challenge done in ALX,
and i also used secure file transfer SFTP to transfer screenshoots
which show the challenges i did.



#How i used SFTP to upload files on remote system:

- On my local machine, I genereted the public and private
key using this command:
```ssh-keygen```
- I copied and saved my public key on my intranet
- I cloned the repository on the remote system
```git clone```
- I created the dir called command line for the win
```mkdir```
- then on my local machine, i opened the directory containing
the files i want to transfer in my terminal
- i used the SFTP command:
```sftp username@your_server_ip_or_remote_hostname``` 
- In sftp prompt i used the command ls, cd, and put. ```put <filename>``` used to
upload file on my ubuntu server.
for example: 
```put 0-first_9_tasks.png```
- after uploading all files one by one, i went back on my remote system which
is the sandbox and pushed all files on the github

#Author
- [Nguweneza P Christian]
##Got feedback for me
- on X [NguwenezaC](https://x.com/NguwenezaC)
- on Discord [nguweneza1](https://discord.com/users/nguweneza1)

