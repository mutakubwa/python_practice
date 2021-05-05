#!/usr/bin/env python3

import shutil
import sys

def check_disk_usage(disk, min_absolute, min_percent):
    """Returns True if there is enough free disk space, false otherwise"""

    du = shutil.disk_usage(disk)
    #calculate Percentage of free space
    percent_free = 100 * du.free / du.total
    #calculate how many free gigabytes
    g_free = du.free/ 2**30
    if percent_free < min_percent or g_free < min_absolute:
        return False
    return True

#check for 2GB and 10% free
if not check_disk_usage("/", 2, 10):
    print("Error: Not enough disk space")
    sys.exit(1)

print("Everything ok")
sys.exit(0)
