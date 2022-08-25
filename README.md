# MyCrossword
Currently WIP due to other commitments, but will revisit. 

MyCrossword is a crossword puzzle web game based on Django and Angular.
## Requirements
- python >= 3.10
- Django >= 4.0.5
## Quick Start
```bash
# to start
$ ./scripts/quickstart.sh # -r flag to reset database

# to quit
$ docker-compose -f ./docker/docker-compose.yml down
```

## Staring w/o Docker
Before starting, make sure to have psql and all the dependencies installed, specifically, 
```bash 
# install django dependencies
$ cd MyCrossword/myCrossword/server
$ poetry install

# install angular dependencies
$ cd MyCrossword/myCrossword/client
$ npm i

# check if psql is installed 
psql --version 
```
```bash
# first, start database
$ ./scripts/start-psql.sh # -r flag to reset database

# next, start django server
$ cd MyCrossword/myCrossword/server
$ python3 manage.py makemigrations # apply model changes
$ python3 manage.py migrate # apply migrations if db reset
$ python3 manage.py runserver 8080 # start

# finally, start angular
$ cd MyCrossword/myCrossword/client
$ ng serve --host 0.0.0.0 --poll=2000 --port 4200 --disable-host-check
```

## Developing with Docker
1. Make sure to have installed docker and docker-compose
2. the `quickstart` above pulls relevant images from docker hub, and starts three containers:
   - Angular Frontend (localhost:4200), 
   - Django Backend(localhost:8080), 
   - PSQL database(localhost:5432)
3. Navigating to `localhost:4200`, you will be able to interact with the full-stack web application right away.
4. Highly recommend getting [Docker Desktop](https://www.docker.com/products/docker-desktop/) and using that instead of all the CLI debugging below.
### Subscribing to logs
1. First, run `docker ps` to get information on running containers
```bash
$ docker ps

CONTAINER ID   IMAGE                         COMMAND                  CREATED         STATUS                   PORTS                                        NAMES
091d2d7cdbfc   ksimon12/crossword:backend    "bash runserver.sh"      5 minutes ago   Up 5 minutes             5432/tcp, 8081/tcp, 0.0.0.0:8080->8080/tcp   docker_server_1
87c562c3f9f9   ksimon12/crossword:frontend   "docker-entrypoint.s…"   5 minutes ago   Up 5 minutes             0.0.0.0:4200->4200/tcp, 8080-8081/tcp        docker_client_1
bcf2289e9b35   postgres                      "docker-entrypoint.s…"   5 minutes ago   Up 5 minutes (healthy)   5432/tcp                                     docker_db_1
```
2. If you want to subscribe to logs coming from the backend, take the backend container id
```bash
$ docker logs -f 091d2d7cdbfc 

Making migrations...
No changes detected
Applying migrations...
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, home, sessions, testapp
Running migrations:
  Applying contenttypes.0001_initial... OK
  ...
```

### Debugging Docker Environment
1. There may be times when you want to debug docker images (to see if the right volumes were mounted, etc.)
```bash
$ docker run --rm -it ksimon12/crossword:frontend /bin/sh
```
... will bring you to a shell session within the frontend docker environment 

### Building Docker Images
1. Source files are mounted at `docker-compose` phase, so changes in source code are automatically reflected in websites
2. However, installing dependencies all happen when docker images are built. Therefore, docker images must be rebuilt when packages are added/removed. 
```bash
$ pwd
MyCrossword/

$ docker build -f ./docker/Dockerfile.django -t ksimon12/crossword:backend .
```
...this will rebuild docker image with tag `ksimon12/crossword:backend` using `Dockerfile.django`. 
3. Make sure to also push this image to the repository. 

## Current Issues
1. An empty file `runserver.sh` keeps getting generated at `docker-compose` in `myCrossword/server`. It's probably an issue with volume mounting in the Dockerfile.
