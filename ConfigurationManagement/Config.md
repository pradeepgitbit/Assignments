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


# Que-2. Extend the CI pipeline to include continuous delivery using Jenkins or GitLab CI. Implement a blue-green deployment strategy?
**Solution:**

Implementing a blue-green deployment strategy in your CI/CD pipeline ensures zero downtime and provides a safe rollback mechanism by maintaining two identical production environments: 
- Blue (current live version) and Green (new version).
Core Blue-Green Workflow

*The standard process involves these high-level steps:*
1.	Build & Test: Compile code and run automated tests in the CI stage.
2.	Deploy to Green: Deploy the new version to the idle environment (e.g., Green).
3.	Smoke Testing: Verify the Green environment is stable while Blue still handles live traffic.
4.	Traffic Switch: Update the load balancer or service router to point 100% of traffic to the Green environment.
5.	Monitor & Cleanup: Monitor for issues; if successful, Blue becomes the idle environment for the next cycle.
________________________________________
**Implementation with GitLab CI**

In GitLab, you can use Environment Variables and Manual Actions to control the switch between blue and green deployments.  

•	Define Environments: Configure blue and green environments in your .gitlab-ci.yml.

•	Targeted Deployment: Use a script to determine which environment is currently idle and target it for the new build.

•	Manual Switch: Implement a manual switch-traffic job that updates your Kubernetes Service or Load Balancer config (e.g., NGINX reload) to redirect traffic.

Example .gitlab-ci.yml Snippet:

stages:
  - build
  - deploy
  - switch
```
deploy_green:
  stage: deploy
  script:
    - kubectl apply -f k8s/green-deployment.yaml
  environment:
    name: production/green

switch_to_green:
  stage: switch
  script:
    - kubectl patch service my-app-service -p '{"spec":{"selector":{"version":"green"}}}'
  when: manual
```
________________________________________
### Implementation with Jenkins
Jenkins uses Pipeline scripts (Jenkinsfile) to manage the logic of environment promotion and traffic routing.

•	Parameterized Builds: Use parameters (e.g., DEPLOY_ENV=green) to specify which environment to update.

•	Shared Queues: To prevent simultaneous deployments, use a "shared queue" configuration so only one deployment runs at a time.

•	Infrastructure as Code (IaC): Integrate tools like Terraform or Ansible within Jenkins stages to ensure both environments remain identical.

Example Jenkinsfile Logic:
```groovy
pipeline {
    agent any
    stages {
        stage('Deploy to Green') {
            steps {
                sh 'kubectl apply -f app-green.yaml'
            }
        }
        stage('Smoke Test') {
            steps {
                sh 'curl -f http://green-test-endpoint.com'
            }
        }
        stage('Switch Traffic') {
            input { message "Switch live traffic to Green?" }
            steps {
                sh 'kubectl patch svc my-service -p \'{"spec":{"selector":{"color":"green"}}}\''
            }
        }
    }
}
```
**Key Considerations:**

•	Database Synchronization: Both environments must access the same database or use migration strategies (like dual-writing) to avoid data loss during the switch.

•	Load Balancing: You need a mechanism (NGINX, F5, or a Cloud Load Balancer) that can instantly reroute traffic based on a config change.

•	Rollback: The "old" environment (Blue) should stay online for a short period so you can quickly switch traffic back if the new version fails in production.
