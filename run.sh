#! /usr/bin/env bash

docker  run --rm -it \
        --network bootcamp \
        --name bff \
        -p 8080:8080 \
        bootcamp/bff:1