# EE-exercise deployment on Kubernetes!
This is example how to write a simple hello world application and deploy it on kubernets cluster
Technology:
- python(flask)
- docker
- kubernetes

### Clone the repostiory locally

```bash
$ git clone --recursive git@github.com:yorg666/ee_exercise.git
```

### Docker
1. Building docker image

```bash
$ docker build -t ee-exercise:v2 -f docker/Dockerfile .
```

2. Tag the new image

```bash
$ docker image tag ee-exercise:v2 yorgdockers/ee-exercise:v2
```

#### Test image locally to verify that application is responding
1. Choose random port from 1024-49151 {I choose 5000} and see if its available

```bash
$ sudo nc localhost 5000 < /dev/null; echo $?
```
  If last command return 1, port is free and can be use for test purposes, if not choose different port

2. Forward local port to application port

```bash
$ docker run -dp ee-exercise:v1 5000:5000
```
5000:5000 {local port:remote port}

3. Check if there is network connectivity

```bash
$ nc -vz localhost 5000
Connection to localhost 5000 port [tcp/*] succeeded
```
4. Send the request to application

```bash
$ curl  localhost:5000
Hello EE, Krystian Nowaczyk here, can anyone hear me?
```

5. Push the image to Docker hub

```bash
$ docker push yorgdockers/ee-exercise:v2
```

### Kubernetes
1. Create alias for kubectl

```bash
$ alias k="kubectl"
```
2. Create kubernetes Deployment

```bash
$ k create -f k8s/deployment.yaml
deployment.apps/ee-exercise created
```

3. Check if image is being sucessfully pulled

```bash
$ k get events -w
```

4. Create the Kubernetes service

```bash
$ k create -f k8s/service.yaml
service/ee-exercise-service created
```

### Check if application is accesible and exposed internally as a service

```bash
$ k get svc
NAME                  TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
ee-exercise-service   ClusterIP   10.98.62.167   <none>        80/TCP    37s
kubernetes            ClusterIP   10.96.0.1      <none>        443/TCP   2m8s
```
```bash
k port-forward service/ee-exercise-service 5000:80 &
```

```bash
$ curl 127.0.0.1:5000
Handling connection for 5000
Hello EE, Krystian Nowaczyk here, can anyone hear me?$ 
```