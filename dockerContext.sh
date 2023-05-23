#!/bin/bash
#
# lists files in the current docker context

docker build --no-cache -t build-context --progress plain -f - . <<EOF
FROM busybox
COPY . /build_context
WORKDIR /build_context
RUN find .
EOF
docker image rm build-context
