apt update
apt install git python -y
pip install termcolor
git clone https://github.com/whitedays/automux.git $PREFIX/share/AutoMux
echo "clear\npython $PREFIX/share/AutoMux/automux.py" >$PREFIX/bin/automux
chmod 777 $PREFIX/bin/automux
echo -e "\n\033[31m安装完成，请输入'automux'来启动AutoMux。\033[0m\n"
