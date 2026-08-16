#!/usr/bin/env python3

import shutil
import psutil

def diskUsage(disk) :
    du = shutil.disk_usage(disk)
    print("Total disk space" + str(du))

    freeDiskPercent = du.free / du.total * 100
    print("Free disk percentage is {} %".format(freeDiskPercent))
    return freeDiskPercent > 20  # returns True or False

def cpuUsage() :
    usage = psutil.cpu_percent(1)
    print("cpu usage is {}".format(usage))
    return usage < 75  # returns True or False

# "/" means this current directory

if not diskUsage("/") or not cpuUsage():  # reverses the result
    print("Error")

else : 
    print("Everything is OK!")


