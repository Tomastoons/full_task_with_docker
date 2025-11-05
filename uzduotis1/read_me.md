

# this is first services (Event propagator)

## how to run:

## if you are using conda or miniconda then you need to activate isolated environment by running: 


conda activate uzd1_env



# (skip step bellow if using conda)
##  or if you do not prefer to install conda or miniconda then you need to install pip:
python3 -m ensurepip --upgrade
##  and then install requirements modules with pip:
# (skip step bellow if using conda)
pip install requests

## and then run services:

python3 main.py

## for windows:

python3 .\main.py

## change main.py if you are in diffrent directory {path to main.py file} - python3 {path}


## To deactivate an active environment, use

conda deactivate
