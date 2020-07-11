#!/usr/bin/bash

echo -e "\033[\34 AutoMux的需求库安装 \033[0m"

sleep 3

apt update && apt upgrade -y 

apt install python python2 -y

pip3 install termcolor 

touch $PREFIX/bin/automux

echo "clear" >> $PREFIX/bin/automux
echo "python $PREFIX/share/AutoMux/automux.py" >> automux

chmod +x $PREFIX/bin/automux

echo -e "\033[44m The End of \033[0m"
