# BASH SCRIPT

## 0x04. Loops, conditions and parsing Projects
In this project i did bash script, and those bash scripts 
i made all passes Shellcheck without any error.

shellcheck is a tool that helps to write proper Bash scripts. 
It makes recommendations on your syntax and semantics and provide 
advice on edge cases that you might not have thought about.

### Example of a bash script
```
nguweneza@nguweneza: ls *.xml
file1.xml  file2.xml  file3.xml

nguweneza@nguweneza: ls *.xml > list

nguweneza@nguweneza: for i in `cat list`; do cp "$i" "$i".bak ; done

nguweneza@nguweneza: ls *.xml*
file1.xml  file1.xml.bak  file2.xml  file2.xml.bak  file3.xml  file3.xml.bak
```
### An Example from one of my Tasks
this bash script, displays 'Best School' 10 times using [until loop]

until $i is greater or equal to 10, print 'Best School'
```
#!/usr/bin/env bash
#displays Best School 10 times using until loop

i=0
until [ $i -ge 10 ]
do
 echo "Best School"
 ((i++))
done
```
