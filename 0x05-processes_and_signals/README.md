# Linux Processes
## 0x05. Processes and signals
In this project i learned linux process management. Some concept which
were covered are:
### What is a PID?
### What is a process?
### How to find a process’ PID?
### How to kill a process?
### What is a signal?
### What are the 2 signals that cannot be ignored?
### An example from the Tasks I did
```
#!/usr/bin/env bash
# A bash script which that displays lines containing the bash word
# shellcheck disable=SC2009

pidd=$(echo $$)
ps auxf | grep "$pidd"
```
