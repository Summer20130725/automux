#!/usr/bin/bash
echo -e "\033[1;36mbonesi DDoS工具安装脚本\n此脚本只对基于Debian的系统有用\n在安装过程中请勿关闭终端\n如果已经安装了请Ctrl+C终止操作\n请等待.........\033[0m"
echo -e "\033[1;35m\nBiliBili:Windows 7\n \033[0m"

sleep 5

clear

echo -e "\033[1;36mbonesi DDoS工具需要安装一下库\033[0m"
echo -e "\033[1;36m以下库名：libpcap-dev(Debian系统) libnet-dev(Debian系统) autoconf automake gcc git make cmake clang\033[0m"
echo -e "\033[1;36m这些库务必要进行安装，否则无法正常运行\033[0m"

sleep 2

clear

echo -e "\033[1;36m正在安装依赖\033[0m"

apt-get install libpcap-dev libnet-dev autoconf automake gcc git make cmake clang -y

echo -e "\033[1;36m依赖安装完成\033[0m"

echo -e "\033[1;36m克隆bonesi到本地路径/opt/\033[0m"

git clone https://github.com/Markus-Go/bonesi /opt/bonesi

ls

echo -e "\033[1;36m克隆完成\033[0m"

sleep 1

cd /opt/bonesi/

echo -e "\033[1;36m开始检查环境\033[0m"

pwd

ls

autoreconf -f -i

./configure 

echo -e "\033[1;36m开始编译\033[0m"

pwd 

make 

make install 

cp src/bonesi /usr/bin

echo -e "\033[1;36m全部工作已经完成\n程序安装完成\033[0m"
echo -e "\033[1;36m你可以输入\033[0m\033[1;31m'bonesi'\033[0m\033[1;36m启动DDoS工具\033[0m"
time=$(date "+%Y-%m-%d %H:%M:%S")
echo -e "\033[1;36m$time\033[0m"
