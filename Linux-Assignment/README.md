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
