# Console

####~~~~~~####
import os
import platform
import cpuinfo
import subprocess
import psutil
import shutil
import ctypes

os.system('color')
from colorama import init, Fore, Back, Style

init(convert=True)


####~~~~~~####

# Global Variables Part
# Color class
class csForeColor:
    Red = Fore.RED
    Green = Fore.GREEN
    Blue = Fore.BLUE
    Yellow = Fore.YELLOW
    White = Fore.WHITE
    Cyan = Fore.CYAN
    Magenta = Fore.MAGENTA
    ForeReset = '\033[39m'


class csBackColor:
    Red = Back.RED
    Green = Back.GREEN
    Blue = Back.BLUE
    Yellow = Back.YELLOW
    White = Back.WHITE
    Cyan = Back.CYAN
    BackReset = '\033[39m'


class csTextFormat:
    tBright = Style.BRIGHT
    tReset = Style.RESET_ALL

class sysHardware:
    getProcessor = cpuinfo.get_cpu_info()['brand_raw']
    getVideocard = "Generic VGA Adapter"
    softGetOsVersion = platform.system() + '' + platform.release()
    getRamGeneric = sysVirtMemTotal = psutil.virtual_memory().total
    #getRamGeneric = str(round(sysVirtMemTotal / 1073741824)) + ',00 GB'
#global var

ctypes.windll.kernel32.SetConsoleTitleW("Mad Shell Beta")
total, used, free = shutil.disk_usage("/")
# funcs


# Counter Main stat (don't change btw)
mainStat = 0
clVoid = []
print(csForeColor.Red, 'MAD' + csForeColor.White, 'SHELL ~ ~ ~ Dev Build 0.1 by Said')
while mainStat == 0:
    ComUserInput = input(csForeColor.Red + "root" + csForeColor.White + "@madshell :>>$ ")


    # single line commands
    if len(ComUserInput.split(' ')) == 2:
        clMainArg, clArgument = ComUserInput.split(' ')
        if clMainArg == 'echo':
            print(clArgument)
    elif ComUserInput == 'version':
        print("Mad Shell ~ Dev Build 0.1")

        #sysfetch module
    elif ComUserInput == 'sysfetch':
        print('>\t' + csForeColor.Cyan + 'CPU:', csForeColor.White + sysHardware.getProcessor)
        print('>\t' + csForeColor.Cyan + 'GPU: ', csForeColor.White + sysHardware.getVideocard)
        print('>\t' + csForeColor.Cyan + 'OS: ', csForeColor.White + sysHardware.softGetOsVersion)
        print('>\t' + csForeColor.Cyan + 'RAM Total: ', csForeColor.White + str(round(sysHardware.getRamGeneric / 1073741824)) + ',00 GB')
        print('>\t' + csForeColor.Cyan + "ROM Status: " + csForeColor.White + "%d GiB from" % (used // (2 ** 30)), "%d GiB" % (total // (2 ** 30)))
        print('>\t' + csForeColor.Cyan + "Free space: " + csForeColor.White + "%d GiB" % (free // (2 ** 30)))
        print('>\t' + csForeColor.Red + "■" + csForeColor.Green + "■" + csForeColor.Yellow + "■" + csForeColor.Blue + "■" + csForeColor.White + "■" + csForeColor.Magenta + "■" + csTextFormat.tBright + csForeColor.Red + "■" + csForeColor.Green + "■" + csForeColor.Yellow + "■" + csForeColor.Blue + "■" + csForeColor.White + "■" + csForeColor.Magenta + "■" + csForeColor.White + csTextFormat.tReset)
    else:
        print('Unknown Command! >> Try to type "help"')
    if ComUserInput == 'break':
        break