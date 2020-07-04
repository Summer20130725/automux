# -*- coding: utf-8 -*-

import os, sys
import getpass
from Module.AMcore import *
from time import sleep as timeout
from termcolor import *

pwd = os.getcwd()

class install:
    def xxsj():
        print(colored("\n       [01]","yellow") + " : Nmap")
        print(colored("       [02]","yellow") + " : Sqlmap")
        print(colored("       [03]","yellow") + " : RED_HAWK")
        print(colored("       [04]","yellow") + " : webdirscan")
        print(colored("       [05]","yellow") + " : dnsmap")
        print(colored("       [06]","yellow") + " : tcpscan")
        print(colored("       [07]","yellow") + " : piescan")
        print(colored("       [08]","yellow") + " : httpscan")
        print(colored("       [09]","yellow") + " : httpscan-python3")
        print(colored("       [10]","yellow") + " : D-Tect")
        print(colored("       [11]","yellow") + " : scanless\n")
        print(colored("       [00]","yellow") + " : Back Menu\n")
        xxsj = input(colored("AutoMux >>> ","yellow",attrs=['bold']))
        if xxsj.strip() == "1" or xxsj.strip() == "01":install_nmap()
        elif xxsj.strip() == "2" or xxsj.strip() == "02":install_sqlmap()
        elif xxsj.strip() == "3" or xxsj.strip() == "03":install_RED_HAWK()
        elif xxsj.strip() == "4" or xxsj.strip() == "04":install_webdirscan()
        elif xxsj.strip() == "5" or xxsj.strip() == "05":install_dnsmap()
        elif xxsj.strip() == "6" or xxsj.strip() == "06":install_tcpscan()
        elif xxsj.strip() == "7" or xxsj.strip() == "07":install_piescan()
        elif xxsj.strip() == "8" or xxsj.strip() == "08":install_httpscan()
        elif xxsj.strip() == "9" or xxsj.strip() == "09":install_httpscan_python3()
        elif xxsj.strip() == "10" or xxsj.strip() == "10":install_D_Tect()
        elif xxsj.strip() == "11" or xxsj.strip() == "11":install_scanless()
        elif xxsj.strip() == "0" or xxsj.strip() == "00":restart()
        else:error()

    def ldsm():
        print(colored("\n       [01]","yellow") + " : Nmap")
        print(colored("       [02]","yellow") + " : Sqlmap")
        print(colored("       [03]","yellow") + " : RED_HAWK")
        print(colored("       [04]","yellow") + " : RouterSploit")
        print(colored("       [05]","yellow") + " : sslscan\n")
        print(colored("       [00]","yellow") + " : Back Menu\n")
        ldsm = input(colored("AutoMux >>> ","yellow",attrs=['bold']))
        if ldsm.strip() == "1" or ldsm.strip() == "01":install_nmap()
        elif ldsm.strip() == "2" or ldsm.strip() == "02":install_RED_HAWK()
        elif ldsm.strip() == "3" or ldsm.strip() == "03":install_sqlmap()
        elif ldsm.strip() == "4" or ldsm.strip() == "04":install_RouterSploit()
        elif ldsm.strip() == "5" or ldsm.strip() == "05":install_sslscan()
        elif ldsm.strip() == "0" or ldsm.strip() == "00":restart()
        else:error()

    def ylce():
        print(colored("\n       [01]","yellow") + " : Slowloris")
        print(colored("       [02]","yellow") + " : Aircrack-ng" + colored(" * ","red"))
        print(colored("       [03]","yellow") + " : Hydra")
        print(colored("       [04]","yellow") + " : hping3" + colored(" * ","red"))
        print(colored("       [05]","yellow") + " : SlowHTTPTest\n")
        print(colored("       [00]","yellow") + " : Back Menu\n")
        ylce = input(colored("AutoMux >>> ","yellow",attrs=['bold']))
        if ylce.strip() == "1" or ylce.strip() == "01":install_slowloris()
        elif ylce.strip() == "2" or ylce.strip() == "02":install_aircrack_ng()
        elif ylce.strip() == "3" or ylce.strip() == "03":install_Hydra()
        elif ylce.strip() == "4" or ylce.strip() == "04":install_hping3()
        elif ylce.strip() == "5" or ylce.strip() == "05":install_SlowHTTPTest()
        elif ylce.strip() == "0" or ylce.strip() == "00":restart()
        else:error()      

    def mmgj():
        print(colored("\n       [01]","yellow") + " : Hydra")
        print(colored("       [02]","yellow") + " : Cupp")
        print(colored("       [03]","yellow") + " : Crunch")
        print(colored("       [04]","yellow") + " : Aircrack-ng" + colored(" * ","red"))
        print(colored("       [05]","yellow") + " : HashBuster")
        print(colored("       [06]","yellow") + " : WebCrack")
        print(colored("       [07]","yellow") + " : Wifite2" + colored(" * \n","red"))
        print(colored("       [00]","yellow") + " : Back Menu\n")
        mmgj = input(colored("AutoMux >>> ","yellow",attrs=['bold']))
        if mmgj.strip() == "1" or mmgj.strip() == "01":install_Hydra()
        elif mmgj.strip() == "2" or mmgj.strip() == "02":install_Cupp()
        elif mmgj.strip() == "3" or mmgj.strip() == "03":install_Crunch()
        elif mmgj.strip() == "4" or mmgj.strip() == "04":install_aircrack_ng()
        elif mmgj.strip() == "5" or mmgj.strip() == "05":install_HashBuster()
        elif mmgj.strip() == "6" or mmgj.strip() == "06":install_WebCrack()
        elif mmgj.strip() == "7" or mmgj.strip() == "07":install_wifite()
        elif mmgj.strip() == "0" or mmgj.strip() == "00":restart()
        else:error() 

    def xtqp():
        print(colored("\n       [01]","yellow") + " : Bettercap")
        print(colored("       [00]","yellow") + " : Back Menu\n")
        xtqp = input(colored("AutoMux >>> ","yellow",attrs=['bold']))
        if xtqp.strip() == "1" or xtqp.strip() == "01":install_bettercap()
        elif xtqp.strip() == "0" or xtqp.strip() == "00":restart()
        else:error() 

    def lygj():
        print(colored("\n       [01]","yellow") + " : Metasploit")
        print(colored("       [02]","yellow") + " : Sqlmap")
        print(colored("       [03]","yellow") + " : Routersploit\n")
        print(colored("       [00]","yellow") + " : Back Menu\n")
        lygj = input(colored("AutoMux >>> ","yellow",attrs=['bold']))
        if lygj.strip() == "1" or lygj.strip() == "01":install_msf()
        elif lygj.strip() == "2" or lygj.strip() == "02":install_sqlmap()
        elif lygj.strip() == "3" or lygj.strip() == "03":install_RouterSploit()
        elif lygj.strip() == "0" or lygj.strip() == "00":restart()
        else:error() 


    def ipgz():
        print(colored("\n       [01]","yellow") + " : IPGeolocation")
        print(colored("       [02]","yellow") + " : IP-Tracer")
        print(colored("       [00]","yellow") + " : Back Menu\n")
        ipgz = input(colored("AutoMux >>> ","yellow",attrs=['bold']))
        if ipgz.strip() == "1" or ipgz.strip() == "01":install_IPGeolocation()
        elif ipgz.strip() == "2" or ipgz.strip() == "02":install_IP_Tracer()
        elif ipgz.strip() == "0" or ipgz.strip() == "00":restart()
        else:error()


    def scfs():
        print(colored("\n       [01]","yellow") + " : backdoor-apk" + colored(" LINUX ","blue"))
        print(colored("       [02]","yellow") + " : msfpc " + colored("LINUX ","blue") + colored(" * ","red"))
        print(colored("       [00]", "yellow") + " : Back Menu\n")
        scfs = input(colored("AutoMux >>> ","yellow",attrs=['bold']))
        if scfs.strip() == "1" or scfs.strip() == "01":install_backdoor_apk()
        elif scfs.strip() == "2" or scfs.strip() == "02":install_msfpc()
        elif scfs.strip() == "0" or scfs.strip() == "00":restart()
        else:error()
        
    def Other(): 
        print(colored("\n       [01]","yellow") + " : Lazymux")
        print(colored("       [02]","yellow") + " : oh-my-zsh\n")
        print(colored("       [00]","yellow") + " : Back Menu\n")
        other = input(colored("AutoMux >>> ","yellow",attrs=['bold']))
        if other.strip() == "1" or other.strip() == "01":install_lazymux()
        elif other.strip() == "2" or other.strip() == "02":install_zsh()
        elif other.strip() == "0" or other.strip() == "00":restart()
        else:error() 

def main():
    banner()
    print(colored("Hello ","cyan",attrs=['bold']) + colored(getpass.getuser(),"yellow",attrs=['bold']) + colored(", welcome to AutoMux!\n","cyan",attrs=['bold']))
    automux = input(colored("AutoMux >>> ","yellow",attrs=['bold']))

    if automux == "help":
        help()
        menu = input(colored("AutoMux >>> ","yellow",attrs=['bold']))
        if menu.strip() == "1" or menu.strip() == "01" or menu.strip() == "change":change()
        elif menu.strip() == "2" or menu.strip() == "02" or menu.strip() == "install":install_list()
        elif menu.strip() == "3" or menu.strip() == "03" or menu.strip() == "repair":repair_msf()
        elif menu.strip() == "4" or menu.strip() == "04" or menu.strip() == "trojan":msf_mm()
        elif menu.strip() == "5" or menu.strip() == "05" or menu.strip() == "update":update()
        elif menu.strip() == "0" or menu.strip() == "00" or menu.strip() == "exit":sys.exit()
        else:error()

    elif automux.strip() == "1" or automux.strip() == "01" or automux.strip() == "change":change()
    elif automux.strip() == "2" or automux.strip() == "02" or automux.strip() == "install":install_list()
    elif automux.strip() == "3" or automux.strip() == "03" or automux.strip() == "repair":repair_msf()
    elif automux.strip() == "4" or automux.strip() == "04" or automux.strip() == "trojan":msf_mm()
    elif automux.strip() == "5" or automux.strip() == "05" or automux.strip() == "update":update()
    elif automux.strip() == "0" or automux.strip() == "00" or automux.strip() == "exit":sys.exit()
    elif automux.strip() == "pwd":
        print(pwd)
    else:error()  
 

def change():
    print(colored("\n请选择要更换的源:\n","cyan",attrs=['bold']))
    print(colored("\n       [01]","yellow") + " : Termux官方源")
    print(colored("       [02]","yellow") + " : Termux清华源\n")
    print(colored("       [00]","yellow") + " : Back Menu\n")
    source = input(colored("AutoMux >>> ","yellow",attrs=['bold']))

    if source.strip() == "1" or source.strip()  == "01":gfy()
    elif source.strip() == "2" or source.strip()  == "02":qhd()
    elif source.strip()  == "0" or source.strip()  == "00":
        restart()
    else:error()  

def update():
    print(colored("\n请选择更新方式:\n","cyan",attrs=['bold']))
    print(colored("\n       [01]","yellow") + " : 一键安装的更新")
    print(colored("       [02]","yellow") + " : 克隆安装的更新\n")
    print(colored("       [00]","yellow") + " : Back Menu\n")
    up = input(colored("AutoMux >>> ","yellow"))

    if up.strip() == "0" or up.strip() == "00" or up.strip() == "exit":
        restart()
    elif up.strip() == "02" or up.strip() == "2":
        print(colored("\n更新中，请稍候...\n","green"))
        pwd = os.getcwd()
        os.system("cd %s" %pwd)
        os.system("git stash && git pull origin master")
        os.system("cd ~")
        print(colored("\n更新完成AutoMux将在3秒后重启AutoMux\n","green"))
        timeout(3)
        restart()
    elif up.strip() == "01" or up.strip() == "1":   
        print(colored("\n更新中，请稍候...\n","green"))
        os.system("bash $PREFIX/share/AutoMux/script/update.sh")
        print(colored("\n更新完成AutoMux将在3秒后重启AutoMux\n","green"))
        timeout(3)
        restart()
    else:error()

def install_list():
    print(colored("\n       [01]","yellow") + " : 信息收集")
    print(colored("       [02]","yellow") + " : 漏洞扫描")
    print(colored("       [03]","yellow") + " : 压力测试")
    print(colored("       [04]","yellow") + " : 密码攻击")
    print(colored("       [05]","yellow") + " : 嗅探和欺骗")
    print(colored("       [06]","yellow") + " : 利用工具")
    print(colored("       [07]","yellow") + " : IP地址跟踪")
    print(colored("       [08]","yellow") + " : 木马生成和反杀")
    print(colored("       [09]","yellow") + " : 其他\n")
    print(colored("       [00]","yellow") + " : Back Menu\n")
    ilist = input(colored("AutoMux >>> ","yellow",attrs=['bold']))
    if ilist.strip() == "1" or ilist.strip() == "01":install.xxsj()
    elif ilist.strip() == "2" or ilist.strip() == "02":install.ldsm()
    elif ilist.strip() == "3" or ilist.strip() == "03":install.ylce()
    elif ilist.strip() == "4" or ilist.strip() == "04":install.mmgj()
    elif ilist.strip() == "5" or ilist.strip() == "05":install.xtqp()
    elif ilist.strip() == "6" or ilist.strip() == "06":install.lygj()
    elif ilist.strip() == "7" or ilist.strip() == "07":install.ipgz()
    elif ilist.strip() == "8" or ilist.strip() == "08":install.scfs()
    elif ilist.strip() == "9" or ilist.strip() == "09":install.Other()
    elif ilist.strip() == "0" or ilist.strip() == "00":restart()
    else:error()


if __name__ == "__main__":
	main()
