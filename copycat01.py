#!/usr/bin/env python3

# import additional code to complete task
import shutil
import os

# move into the working directory
os.chdir("/home/student/mycode/")

#copy fileA to fileB AND copy entire directoryA to directoryB
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
shutil.copytree("5g_research/", "5g_research_backup/")

#end
