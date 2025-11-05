
# instructions how to run:


## double-check Python 3 installation:

python3 --version

## If Python 3 is already installed on your machine, this command will return the current version of Python 3 installation. In case it is not installed, for UBUNTU OS, you can run the following command and get the Python 3 installation:

sudo apt install python3

## For Windows
https://www.python.org/downloads/

## install docker engine (for LINUX)

https://docs.docker.com/engine/install/

## install docker-desktop

https://docs.docker.com/desktop/setup/install/windows-install/


# and now run server with this command:

## LINUX
sudo docker compose up --build
## WINDOWS
docker compose up --build

# ADDITIONAL endpoints usage example: 

# POST:

http://127.0.0.1:8000/event

{
	"event_type":"message",
	"event_payload":"hello sir!"
}

# GET:

http://127.0.0.1:8000/event  
