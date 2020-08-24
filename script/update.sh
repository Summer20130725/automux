#!/usr/bin/env bash

printf "\033[36mUpdating\033[0m\n"

cd $PREFIX/share/AutoMux/

git stash

git pull

cd $HOME/

