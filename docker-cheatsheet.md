

ezpz commands to remember:


docker build . -t <tag>

        -> build the image based on the dockerfile in your current send_from_directory
        -> and tag is with the tag provided


docker run --rm -it <tag> /bin/bash

        -> runs image <tag> and execute bash in it
        -> --rm ensure the container is destroyed once it is shut down
        -> -it (interactive mode)

ezpzier commands:

    docker ps
        -> list running containers
    
    docker images
        -> list docker images available locally (or not)
    
    docker rmi <tag>
        -> delete image from local repository

    docker network create <name>
        -> create a docker network with name `name`
        dock