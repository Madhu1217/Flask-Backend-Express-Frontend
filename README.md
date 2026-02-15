## Flask + Node.js Docker Project

### Run Locally

```bash
docker-compose up --build
```
## 1. Project Overview
This project demonstrates deploying a Flask backend API and an Express frontend application on Amazon Web Services using three different architectures:
- Single EC2 Instance Deployment
- Separate EC2 Instances Deployment
- Dockerized Deployment using Amazon ECR, ECS (Fargate), and VPC.

## 2. Single EC2 Deployment
Both Flask and Express applications are deployed on a single EC2 instance. Nginx is configured as a reverse proxy to route traffic.

![one_EC2](./images/image.png)

![BackEnd](image-1.png)

![FrontEnd](image-2.png)

![Nginx_Configure](image-3.png)

![Nginx_FrontEnd](image-4.png)

![Nginx_backEnd](image-5.png)

## 3. Separate EC2 Deployment
Frontend and backend applications are deployed on separate EC2 instances. The frontend communicates with the backend using the backend’s public IP.

![Two_EC2](image-6.png)
 
![backEnd](image-7.png)

![FrontEnd](image-8.png)

![Terminal](image-9.png)

## 4. Docker + ECR + ECS + VPC Deployment
Both applications are containerized using Docker. Docker images are pushed to Amazon ECR and deployed using ECS Fargate inside a VPC. An Application Load Balancer (ALB) exposes the application publicly.

![ECR](image-10.png)

![DockerImagePush](image-11.png)

![FrontEndECR](image-12.png)

![BackEndECR](image-13.png)

![ECSCluster](image-14.png)

![ClusterServices](image-15.png)

![ECS](image-16.png)
