## SongShare Free Learning Resources Wep App v2
### 💡 Main Idea: 
* A Platform sharing free learning resources, such as instruments, programming languages or other materials.
* [PRODUCTION](https://link-url-here.org)
* [TEST](https://link-url-here.org)


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

### 🧑🏻‍💻 Run on your local machine and see the web interface
1. Build image(may take a while)
    ```linux
    $ docker build -t app_img .
    ```

2. Docker run container and bind the port:80
    ```linux
    docker run -p 80:80 app_img 
    ```

3. Click on http://0.0.0.0:80, there you go:)

### Feature Updated
* v1.0
* v2.0