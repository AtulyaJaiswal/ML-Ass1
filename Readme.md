# ELL887 Cloud Computing - Assignment 1 (Containers)

## Overview
This assignment consists of three parts:
1. *Modifying an existing web server container* (Nginx)
2. *Creating and pushing a container* (C++ program + MySQL database)
3. *Deploying a web server in Kubernetes*
---

# ELL887 Cloud Computing - Assignment 1 (Containers)

## Overview
This assignment consists of three parts:
1. *Modifying an existing web server container* (Nginx)
2. *Creating and pushing a container* (C++ program + MySQL database)
3. *Deploying a web server in Kubernetes*
---

## Part 1: Modifying an Existing Web Server Container

### Objective
This part modifies an Nginx container to serve a custom webpage at http://localhost/ELL887.

### Files Provided:
- Dockerfile (to create a custom Nginx container)
- index.html (to display the required message)

### Steps to Run:
1. *Build the container:*
   docker build -t part1 .

2. **Run the container:**
   docker run -d -p 80:80 part1
   ![Screenshot (5)](https://github.com/user-attachments/assets/fdab5a8f-dd42-4414-b3a1-98c4db641787)

4. *Verify the output:*
    [htttp://localhost/ELL887](http://localhost/ELL887)

   OUTPUT: "Hello World! I am Atulya Jaiswal".
   ![Screenshot (6)](https://github.com/user-attachments/assets/ec9a1e39-0fc8-4514-8793-6314c8e9e86a)

   
## Part 2: Creating and Pushing a Container

### Objective
This part containerizes a C++ program that prints "Hello world!! I am Atulya Jaiswal from karakoram Hostel (2024EET2380)" and includes a MySQL database.

### Files Provided:
- `Dockerfile` (to create a custom Nginx container)
- `docker-compose.yaml` (to include a MySQL database)
- `main.cpp` (to display the required message)

### Steps to Run:
A. **Run the c++ program container**
1. **Build the C++ container:**
   docker build -t part2 .

2. *Run the container:*
   docker run part2

3. **Verify the output:**
   OUTPUT: "Hello world!! I am Atulya Jaiswal from karakoram Hostel (2024EET2380)".
![Screenshot (3)](https://github.com/user-attachments/assets/6e7b9bb5-0c43-492a-b6b7-893af19c0d55)


B. *Start the Database using Docker Compose*
1. *Run the services(c++ ap + MySql database)*
    docker-compose up

2. **Use different terminal to use MySql**
     docker exec -it mysql-db mysql -u root -p
     #password: tutumeranaam

3. *Repositories pull command*
   
    docker pull atulyajaiswal/ell887:app

   
    docker pull atulyajaiswal/ell887:db 


For connecting the cpp and MySQL, I have used the top docker-compose file and submitted the (bottom image_ docker-compose file in which I have updated the image as docker repositories.

![Screenshot (4)](https://github.com/user-attachments/assets/d35dd816-c003-46d9-8093-76493e85b2d9)
![Screenshot (7)](https://github.com/user-attachments/assets/9dfb1406-dfb2-426b-9d8b-7c61b2c49375)


4. **To verify the output**
   docker compose up


## Part 3: Modifying an Existing Web Server Container

### Objective
Deploy a web server in a Kubernetes cluster using Minikube. web server runs on port 30081

### Files Provided:
- deployment.yaml (K8s Deployment & service for the web server)

### Steps to Run:
1. *Apply the Kubernetes configuration using:*
   kubectl apply -f deployment.yaml

2. **check the running pods using:**
   kubectl get pods
   
3. *check the service pods using (wait until webserver pod is in running state the use below cmd):*
   
   minikube service webserver-service

![Screenshot (8)](https://github.com/user-attachments/assets/87a88af0-c196-4aad-afd4-d33d25d9f8fa)


4. **Access the web server using:**
   [htttp://<minikube-ip>:30081](htttp://<minikube-ip>:30081)

   OUTPUT: nginx web page.

![Screenshot (9)](https://github.com/user-attachments/assets/a437dd3a-9ce3-443f-a43d-5e9fcccf9484)
