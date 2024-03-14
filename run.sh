#!/bin/bash



up() {
    sudo docker compose up -d # Start Docker containers in the background
    sudo docker compose logs -f # Start logs
}

stop() {
    sudo docker compose stop # Stop container
}

down() {
    sudo docker compose down --volumes --remove-orphans # Stop and remove containers and volumes
}

rem_persistence() {
    sudo rm -rf postgres-data/
}

rem_images() {
    sudo docker rmi -f $(sudo docker images -aq) # Remove all Docker images
}

allowed_values=("up" "stop" "down" "restart" "restartp" "restarti" "restartpi")

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 [ ${allowed_values[*]} ]"
    exit 1
fi

argument=$1

is_valid=false
for value in "${allowed_values[@]}"; do
    if [ "$value" == "$argument" ]; then
        is_valid=true
        break
    fi
done

if $is_valid; then
    echo "The argument '$argument' is in the set of allowed values."
else
    echo "Error: The argument '$argument' is not in the set of allowed values."
    echo "Allowed values are: ${allowed_values[*]}"
    exit 1
fi


if [[ $argument = "up" ]]; then
    up
fi

if [[ $argument = "stop" ]]; then
    stop
fi

if [[ $argument = "down" ]]; then
    down
fi

if [[ $argument = "restart" ]]; then
    down
    up
fi

if [[ $argument = "restartp" ]]; then
    down
    rem_persistence
    up
fi

if [[ $argument = "restarti" ]]; then
    down
    rem_images
    up
fi

if [[ $argument = "restartpi" ]]; then
    down
    rem_images
    rem_persistence
    up
fi
