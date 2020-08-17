#!/usr/bin/env bash

printf "\n\033[36mThis is the installation script of automux.\033[0m
\033[33mDon't use it for Linux System.\033[0m
\033[34mOnly for Termux!\n\033[0m"

printf "\033[34mPlease Wating 10s!\033[0m\n"
printf "\033[36mPress Ctrl + C Quit\033[0m"

sleep 10s

apt update && apt upgrade -y

apt install git python

git clone https://github.com/whitedays2007/automux.git $PREFIX/share/AutoMux

echo "clear\npython $PREFIX/share/AutoMux/automux.py" > $PREFIX/bin/automux

chmod 777 $PREFIX/bin/automux

printf  "\n\033[31m安装完成，请输入'automux'来启动AutoMux。\033[0m\n"