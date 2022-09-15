## SongShare Free Learning Resources Wep App v2
### 💡 Main Idea: 
* A Platform sharing free learning resources, such as instruments, programming languages or other materials.
* website: [PRODUCTION](http://websongsshare.ml/home-page)
* website: [TEST](http://35.201.217.195/home-page)


### ⛓ Framework:
* Backend: **Flask(Python)**
* Deployment: **Gunicorn**, **Docker Container(TEST)**, **Kubernetes(PROD)**
* Data Storage \& Migration: **MySQL**, **Redis**, **Alembic**
* Frontend: **HTML**, **CSS**, **Javascript**, **JQuery**

### 🧰 Used Tools:
* <a href="https://cloud.google.com/kubernetes-engine"><img alt="GitHub Actions" src="https://img.shields.io/badge/Google%20Kubernetes%20Engine-0078d7.svg?logo=Kubernetes&logoColor=white"></a> as a Production Environment
* <a href="https://cloud.google.com/products/compute"><img alt="GitHub Actions" src="https://img.shields.io/badge/GCP%20compute%20engine-0078d7.svg?logo=Amazon%20EC2&logoColor=white"></a> as a virtual machine
* <a href="https://cloud.google.com/container-registry"><img alt="GitHub Actions" src="https://img.shields.io/badge/Google%20Container%20Registry-0078d7.svg?logo=Docs.rs&logoColor=white"></a>  as a sotrage of built docker images
* <a href="https://aws.amazon.com/rds/"><img alt="GitHub Actions" src="https://img.shields.io/badge/Amazon%20RDS-F37626.svg?logo=Amazon%20RDS&logoColor=white"></a> as a MySQL service
* Implemented CI/CD process via <a href="https://www.jenkins.io/"><img alt="Jenkins" src="https://img.shields.io/badge/Jenkins-800000.svg?logo=Jenkins&logoColor=white"></a> and <a href="https://github.com/features/actions"><img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub%20Actions-010101.svg?logo=github%20actions&logoColor=white"></a>

### 🧱 Infractructure
* Web Services
    ![image](https://github.com/pcchencode/web-song-share/blob/master/static/infra1.PNG)

* CI/CD
    ![image](https://github.com/pcchencode/web-song-share/blob/master/static/infra2.PNG)

### 🧑🏻‍💻 Run on your local machine to see👀 the web interface
1. Build image(may take a while)
    ```ShellSession
    $ docker build -t app_img .
    ```

2. Docker run container and bind the port:80
    ```ShellSession
    $ docker run -p 80:80 app_img 
    ```

3. Click on http://0.0.0.0:80, then there you go : )
[![截圖 2022-08-30 上午11.13.39](https://i.im.ge/2022/08/30/OybAfM.2022-08-30-11-13-39.png)](https://im.ge/i/OybAfM)


### 🌟 Released Features
#### v2.0
1. Users can login to see the hidden materials: Hot Resources 🔥


#### v1.5
1. Add language: Chinese
2. Dark mode available 😎

#### v1.0
1. Users are able to share learning resources of guitar 🎸
2. Users are able to search shared resources