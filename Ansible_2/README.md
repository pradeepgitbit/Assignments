# **Task:** Write Ansible playbooks to automate the setup and configuration of a web server (e.g., Apache or Nginx)?

### **- Steps:**

#### Ansible playbook to set up an Apache web server on Ubuntu/Debian systems. 

1. **The Playbook** (```setup_webserver.yml```)
```yaml
---
- name: Configure Apache Web Server
  hosts: webservers
  become: yes
  tasks:
    - name: Update apt cache
      apt:
        update_cache: yes

    - name: Install Apache
      apt:
        name: apache2
        state: present

    - name: Ensure Apache is started and enabled
      service:
        name: apache2
        state: started
        enabled: yes

```

2. **The Inventory** (```inventory.ini```)

Create a file to tell Ansible where your server is: 
```bash
[webserver]
192.168.1.100 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/id_rsa
```


3. **How to Run It**

Execute the following command in your terminal:

```bash
ansible-playbook -i inventory.ini setup_webserver.yml
```

#### - **Key Components:**

**```become: yes:```** Runs commands with sudo privileges.

**```apt```** **module**: Handles package management.

**```service```** **module**: Manages the background process (daemon).

**```copy```** **module**: Places your website files on the target machine.