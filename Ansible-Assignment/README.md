# Que-1 Install and configure Ansible on Local Environment
**To install and configure Ansible and run a basic configuration script, we will need at least two machines: an Ansible control node (where Ansible is installed) and one or more managed nodes (the target servers).**

#### 1. Install and Configure Ansible (using an Ubuntu system for the control node).


***Step 1: Install Ansible on the Control Node**
- Update the system's package list, add the Ansible Personal Package Archive (PPA) for the latest version, and install the software:

```bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install ansible -y
```
- Verify the installation by checking the version:
```bash
ansible --version
```
***Step 2: Set Up SSH Access to Managed Nodes**

- Ansible communicates via SSH, so passwordless SSH access from the control node to the managed nodes is required.
    - Generate an SSH key pair on the control node if don't have one:
```bash
ssh-keygen -t rsa -b 4096
```

- Copy the public key to each managed node using ```ssh-copy-id```. Replace username and ```remote_server_ip``` with our actual values:
```bash
ssh-copy-id username@remote_server_ip
```
- Test the connection:
```bash
ssh username@remote_server_ip
```

***Step 3: Configure the Inventory File**

- The inventory file lists the managed hosts. By default, Ansible uses ```/etc/ansible/hosts```, but we can create a custom file for our project.

- Create a file named ```inventory``` in our project directory:

```bash
nano inventory
```
- Add the hosts, organizing them into groups. In this example, we define a webservers group:
```ini
[webservers]
server1 ansible_host=192.168.1.101
server2 ansible_host=192.168.1.102

[all:vars]
ansible_user=your_remote_username
# Uncomment the next line if you are using an SSH key file
# ansible_ssh_private_key_file=~/.ssh/id_rsa
```
- Replace the IP addresses and your_remote_username with the actual details.


***Step 4: Test Connectivity**

- Use an ad-hoc command to verify Ansible can connect to your hosts:
```bash
ansible all -i inventory -m ping
```
A successful connection will return a "pong" message for each host.
---
---
# Que-2 Write and execute basic configuration scripts.?
**Solution:**

The following playbook installs the Nginx web server on the webservers group defined in the inventory.

**Step 1: Create the Playbook**

- Created a new file named ```install_nginx.yml```:
```bash
nano install_nginx.yml
```
- Add the following content:
```yaml
---
- name: Install and start Nginx
  hosts: webservers
  become: yes
  tasks:
    - name: Update apt package cache
      apt:
        update_cache: yes
    - name: Install Nginx
      apt:
        name: nginx
        state: present
    - name: Start Nginx service
      service:
        name: nginx
        state: started
        enabled: yes
```       
***Step 2: Execute the Playbook**

- Run the playbook using the ansible-playbook command, specifying your inventory file:
```bash
ansible-playbook -i inventory install_nginx.yml
```
Ansible will connect to the specified servers, update the package cache, install Nginx, and ensure the service is running and enabled on boot