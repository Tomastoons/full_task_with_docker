# for this task I was using UBUNTU OS

## instructions how to run:


## double-check Python 3 installation:

python3 --version

## If Python 3 is already installed on your machine, this command will return the current version of Python 3 installation. In case it is not installed, for UBUNTU OS, you can run the following command and get the Python 3 installation:

sudo apt install python3

## install docker engine

https://docs.docker.com/engine/install/

## install docker-desktop by installing Docker Desktop on Linux enables host.docker.internal to work, if using Windows just install docker

https://docs.docker.com/desktop/setup/install/windows-install/


# and now run server by this command:

sudo docker compose up --build


# ADDITIONAL endpoints usage example: 

# POST:

http://127.0.0.1:8000/event

{
	"event_type":"message",
	"event_payload":"hello sir!"
}

# GET:

http://127.0.0.1:8000/event  
