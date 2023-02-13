# README #

## What is this repository for? ##

This repository contains Python code for waterJar project for CS 331 - Data Structures and Algorithms.

## Description ##

The user enters 3 numbers for the size of 3 water jars up to size 9. The user also enters the target value for one of the jars to contain. 
The program will then find the shortest path to find this target jar. 
The jars are able to pull from an infinite supply of water and be poured between each other. 
When the jars are pouring between each other they have to pour till one is empty or the other is full.
For example if the jar sizes are 5, 7, 8 and the target is 4.
If the 7 jar is full and is pouring into the 8 jar, it will stop when the 7 jar is empty leaving 7 in the 8 jar.

## How do I get set up? ##

Instructions in this README file are for a Windows 11 environment or linux environment with python installed

### Summary of set up ###

Simply use python followed by fileName.py to run

### Configuration ###

1. Clone the repository:

```
$ git clone https://github.com/jloriso/waterJar.git
```

2. Run the program:

```
$ python waterJarFinal.py
```

3. Enter the size of the first, second, third, and target when prompted
*NOTE: the values must be in range (0,10)*

4. The program will then use a breadth first search to provide the shortest path to get the target value.

### Who do I talk to? ###

Email jloriso@hawk.iit.edu