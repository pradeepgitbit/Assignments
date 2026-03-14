# Que-1. Research and compare different configuration management tools (Ansible, Puppet, Chef) and write a report on their use cases and advantages?

### Configuration Management Tools: Ansible vs Puppet vs Chef
- Configuration management tools are used in DevOps to automate server setup, maintain system
consistency, and manage infrastructure using code.

#### |>- Three widely used tools are Ansible, Puppet, and Chef. 

**Ansible:** An open■source automation tool developed by Red Hat. It uses an agentless architecture
and YAML-based playbooks for automation. It is easy to learn and widely used for application
deployment, cloud automation, and CI/CD pipelines.

**Puppet:** A configuration management tool that uses a declarative language to manage
infrastructure. It follows a master–agent architecture and is widely used in large enterprises
requiring centralized management and compliance.

**Chef:** A configuration management platform that uses Ruby-based scripting to define infrastructure
as code. It is highly flexible and suited for complex infrastructure automation and developer-driven
DevOps environments.


| Feature | Ansible | Puppet | Chef |
|---|---|---|---|
| **Architecture** | Agentless | Master-Agent | Client-Server |
| **Language** | YAML | Puppet DSL | Ruby DSL |
| **Ease of Use** | Easy | Moderate | Complex |
| **Best For** | Quick automation | Enterprise compliance | Complex infrastructure |
---
---


###
 **Conclusion:** 
- Ansible is best for simple and fast automation, Puppet is ideal for large enterprise
environments with compliance needs, and Chef is suitable for complex infrastructures requiring
deep customization
----

# Que-2. Extend the CI pipeline to include continuous delivery using Jenkins or GitLab CI. Implement a blue-green deployment strategy?

To extend a CI pipeline into Continuous Delivery (CD) with a blue-green deployment strategy, you must automate the transition of code from a validated build to a production environment where two identical infrastructures ("blue" and "green") coexist. 

1. **Blue-Green Strategy Overview**

**Two Environments:** Maintain two identical production-ready environments.

- **Blue (Live):** Currently serves 100% of production traffic.

- **Green (New):** Used for deploying and testing the new version before it goes live.

**Switch Traffic:** Once "green" is verified, the load balancer or router points to "green," making it the new "blue".

**Rollback:** If issues occur, traffic is instantly rerouted back to the stable environment. 


2. **Implementation with Jenkins**

Jenkins uses a Jenkinsfile (Declarative Pipeline) to manage the CD flow. 

- **Build & Push:** Compile code and push a Docker image to a registry (e.g., ECR or Docker Hub).

- **Deploy Green:** Automate the deployment of the new version to the "green" infrastructure using tools like Terraform, Ansible, or Kubectl.

- **Automated Testing:** Run smoke tests or health checks against the "green" environment's private endpoint.

- **Manual Approval (Optional):** Insert an input step to pause the pipeline for manual verification before switching traffic.

- **Switch Traffic:** Use a shell script to update your Load Balancer (NGINX, AWS ELB) or Kubernetes Service to point to the "green" pods. 

Below is a **simple DevOps project example** showing how to **extend a CI pipeline to Continuous Delivery (CD) using Jenkins and implement a Blue-Green deployment strategy**. 

---

# CI/CD Pipeline with Jenkins + Blue-Green Deployment

## 1. Project Architecture

```
Developer
   │
   ▼
GitHub Repository
   │
   ▼
Jenkins CI Pipeline
   │
   ├── Build Application
   ├── Run Tests
   ├── Build Docker Image
   ├── Push Image to DockerHub
   │
   ▼
Deployment Stage
   │
   ├── Deploy to Blue Environment
   ├── Deploy to Green Environment
   │
   ▼
Load Balancer / Nginx
   │
   ▼
Users
```

### Tools Used

| Tool                | Purpose             |
| ------------------- | ------------------- |
| Jenkins             | CI/CD automation    |
| Docker              | Containerization    |
| GitHub              | Source code         |
| Nginx               | Load balancer       |
| Bash                | Deployment scripts  |
| Kubernetes / Docker | Deployment platform |

---

# 2. Blue-Green Deployment Concept

Blue-Green deployment uses **two identical environments**.

| Environment | Status                       |
| ----------- | ---------------------------- |
| Blue        | Currently running production |
| Green       | New version deployment       |

### Deployment Flow

1. Application runs in **Blue**
2. New version deployed to **Green**
3. Test Green environment
4. Switch traffic from Blue → Green
5. Blue becomes standby

Benefits:

* Zero downtime
* Easy rollback
* Safer releases

---

# 3. Example Project Structure

```
project/
│
├── app/
│   └── app.py
│
├── Dockerfile
│
├── Jenkinsfile
│
├── docker-compose.blue.yml
├── docker-compose.green.yml
│
└── switch.sh
```

---

# 4. Sample Application (Python)

`app/app.py`

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Blue Green Deployment Example"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

# 5. Dockerfile

```dockerfile
FROM python:3.9

WORKDIR /app

COPY app/ .

RUN pip install flask

CMD ["python","app.py"]
```

---

# 6. Jenkins CI/CD Pipeline

`Jenkinsfile`

```groovy
pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "yourdockerhubusername/bluegreen-app"
    }

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/yourrepo/project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE:$BUILD_NUMBER .'
            }
        }

        stage('Push Image') {
            steps {
                withDockerRegistry([credentialsId: 'dockerhub', url: '']) {
                    sh 'docker push $DOCKER_IMAGE:$BUILD_NUMBER'
                }
            }
        }

        stage('Deploy Green') {
            steps {
                sh 'docker-compose -f docker-compose.green.yml up -d'
            }
        }

        stage('Test Green Environment') {
            steps {
                sh 'curl http://localhost:5001'
            }
        }

        stage('Switch Traffic') {
            steps {
                sh './switch.sh'
            }
        }

    }
}
```

---

# 7. Blue Environment

`docker-compose.blue.yml`

```yaml
version: '3'

services:
  app:
    image: yourdockerhubusername/bluegreen-app:latest
    ports:
      - "5000:5000"
```

---

# 8. Green Environment

`docker-compose.green.yml`

```yaml
version: '3'

services:
  app:
    image: yourdockerhubusername/bluegreen-app:latest
    ports:
      - "5001:5000"
```

---

# 9. Traffic Switching Script

`switch.sh`

```bash
#!/bin/bash

echo "Switching traffic to GREEN environment"

docker stop blue_container
docker rename green_container blue_container
```

Make executable:

```
chmod +x switch.sh
```

---

# 10. Nginx Load Balancer Example

```
upstream app {
    server blue:5000;
}

server {
    listen 80;

    location / {
        proxy_pass http://app;
    }
}
```

To switch traffic:

```
blue -> green
```

Reload nginx:

```
nginx -s reload
```

---

# 11. CI/CD Workflow

```
1 Developer pushes code to GitHub
2 Jenkins pipeline triggers automatically
3 Docker image builds
4 Image pushed to DockerHub
5 Deploy new version to Green environment
6 Test Green
7 Switch traffic from Blue → Green
8 Old version kept for rollback
```

---

# 12. Rollback Strategy

If deployment fails:

```
Switch traffic back to Blue
Stop Green environment
Fix bug
Redeploy
```

---



This project demonstrates:

* Jenkins CI/CD
* Docker containerization
* Blue-Green deployment
* Zero-downtime releases
* Automation scripts
* Production deployment strategy


---



