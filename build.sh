#!/usr/bin/env bash

# defines
NAME=nmonchart
VERSION=35

# pack sources
tar -cvzf "${NAME}-${VERSION}.tar.gz" --exclude .git --exclude "*.tar.gz" --transform s/./"${NAME}-${VERSION}"/ ./*

# run rpm build command
rpmbuild -ta "${NAME}-${VERSION}.tar.gz"
