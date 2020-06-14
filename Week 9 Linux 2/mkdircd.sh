#!/bin/bash
#print hello world
echo "Hello World"
#print this program is called (file name)
echo "This Program is called: $0"
#make directory (user input 1)
mkdir $1
#Change into (user input 1)
cd $1
#Create file (user input 2)
touch $2
#edit file (user input 2)
nano $2
#print End Program
echo "End program"
