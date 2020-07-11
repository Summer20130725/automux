#!/usr/bin/bash

echo -e "\033[32m AutoMux的需求库安装 \033[0m"
echo -e "\033[33m 倒计时3s开始安装AutoMux的需求库 \033[0m"
sleep 2

clear

echo -e "\033[32m  Start right now!  \033[0m"

sleep 2s

clear 

echo -e "\033[31m  3   \033[0m"

sleep 2s 

clear

echo -e "\033[33m  2   \033[0m"

sleep 2s

clear 

echo -e "\033[34m  1   \033[0m"

sleep 2s

clear

echo -e "\033[32m  Start! \033[0m"

apt update && apt upgrade -y 

apt install python python2 -y

pip3 install termcolor 

touch $PREFIX/bin/automux

echo "clear" >> $PREFIX/bin/automux
echo "python $PREFIX/share/AutoMux/automux.py" >> automux

chmod +x $PREFIX/bin/automux

echo -e "\033[44m Automux configuration complete \033[0m"
