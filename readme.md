## SongShare Free Learning Resources Wep App v2
### 💡 Main Idea: 
* A Platform sharing free learning resources, such as instruments, programming languages or other materials.
* website: [PRODUCTION](https://link-url-here.org)
* website: [TEST](http://35.201.217.195/home-page)


### ⛓ Framework:
* Backend: **Flask(Python)**
* Deployment: **Gunicorn**, **Docker Container(TEST)**, **Kubernetes(PROD)**
* Data Storage \& Migration: **MySQL**, **Redis**, **Alembic**
* Frontend: **HTML**, **CSS**, **Javascript**, **JQuery**

### 🧰 Used Tools:
* Google Kubernetes Engine as a Production Environment
* Google Cloud Compute Engine as a virtual machine
* Google Container Registry as a sotrage of built docker images
* AWS RDS as a MySQL service
* Implemented CI/CD process via Jenkins srver(on VM) and Github Actions

### 🧑🏻‍💻 Run on your local machine to see👀 the web interface
1. Build image(may take a while)
    ```ShellSession
    $ docker build -t app_img .
    ```

2. Docker run container and bind the port:80
    ```ShellSession
    $ docker run -p 80:80 app_img 
    ```

3. Click on http://0.0.0.0:80, there you go:)
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