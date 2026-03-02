# Que-1 What is linux?
**Ans**
- linux is an operating system just like Windows OS ,
    linux is Unix based open-source OS, known for its flexibility, stability, and strong security.
    - Unix is a powerful OS , we can create multiple users with specified permissions, also it's an multitasking operating system.
- Linux combines a wide range of open-source tools and components to form a complete computing environment.
- Architecture of Linux:
    - Linux architecture refers to the layered structure of the Linux operating system that defines how its components - such as the kernel, shell, system libraries, and hardware - interact with each other to manage system resources and execute user programs efficiently.
---

# Que-2 What is the difference between Hard Link & Soft Link?
**Ans**
- Hard Link : Its a direct copy of a file with the same data, if we delete the original file other one would not delete. Deleting the original file does not break a hard link.
    - command : ```ln source target```

- Soft Link : Also known as Symbolic link , Its a shortcut that points to the file name, not the data itself. If the original file is deleted, the soft link breaks.
    - command : ```ln -s source target```
---
# Que-3 What is a Kernel in Linux?
**Ans**
- The kernel is the core component of the operating system that acts as the bridge between software applications and the physical hardware, controls the communication between software and hadware. 
- It manages CPU scheduling, memory allocation, input/output operations, and device drivers, operating in a privileged, protected area of memory.
- Prevents conflicts between multiple running programs.
---

# Que-4 How do you create a user account?
**Ans**
You can create a user using the useradd or adduser command with root privileges. 
- first create the user using command- ```sudo adduser username```
    - it will create the user and home directory for user and also asks for setting up password, if don't ask then set the password using command- ``` sudo passwd username```
---
# Que-5 What is the 'grep' command used for?
**Ans**

- ```grep ``` command used to search for specific patterns, words, or regular expressions from a text file .
- Example: ```grep "error" /var/log/syslog``` searches for the word "error" in a log file.
---
# Que-6
#### Step 1: Create user p1
- ```sudo adduser p1```
    - it will create the user p1 and will also create the default group p1 for p1 user ( the user's primary group is their own name).

#### Step 2: Create groups g1, g2, g3 and the user p1 to all the groups
```
sudo groupadd g1
sudo groupadd g2
sudo groupadd g3
sudo usermod -aG g1,g2,g3 p1
```
- Note: This makes g1,g2,g3 secondary groups. The user's primary group is usually their own name.

#### Step 3: Make 'g1' the default group for new files.
- Set the primary group of p1 to g1:
    ```sudo usermod -g g1 p1```

- now whenever p1 creates a file g1 will automatically be the group owner
---
# Que-7.
#### Step 1: Create directory /tmp/bg as root user and create files inside it.
    - sudo mkdir /tmp/bg
    - sudo touch /tmp/bg/file1.txt

#### Step 2: Set "abhi" as owner and provide necessary permissions
- ```sudo chown -R abhi:abhi /tmp/bg```

Set permissions: Owner can read/write/execute (7), others can't (0).

- ```sudo chmod -R 700 /tmp/bg```

---
# Que-8 Identify and terminate high CPU process
- Identify: Run ```top``` or ```htop``` to see the highest CPU-consuming process and note its Process ID (PID).


- Terminate: Use the kill command to terminate the process gently, or kill -9 for a forced shutdown.
    - ``` kill -9 [PID] ```
