#!/bin/bash

#print this program is (file name)
echo "This program is called: $0"
#set prefix equal to (user input)
PREFIX=$1
#print Scanning prefix.0/24... 
echo "Scanning $PREFIX.0/24..."
#Make a for loop looping 1-255
for HOST in $(seq 1 255)

do
#set TARGET equal to (userinput).(seq 1-255)
 TARGET="$PREFIX.$HOST"
#test code
# echo $TARGET
#ping count once TARGET pipe the output to /dev/null then print if the Target is UP or DOWN and pipe the output to a fie called live or down hosts
 ping -c 1 $TARGET &> /dev/null && echo "$TARGET is UP" >> live_hosts || echo "$TARGET is down" >> down_hosts

done
#print out Scan Completed. Here are your previous searches:
echo "Scan Completed. Here are your previous searches:"
#print the contents of live and down hosts to the screen
cat live_hosts
cat down_hosts

#print End program
echo "End Program"
