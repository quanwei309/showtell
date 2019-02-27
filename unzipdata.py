#!/bin/env python
#-*- coding:utf-8 -*-
import zipfile,os
import platform,sys,os
from zipfile import *
import zipfile
systty = platform.system()
system1 = 'windows'
system2 = 'Linux'
def unzip():
    if systty.lower() == system1.lower():
    # if systty.lower() == 'windows':
        flag = "\\"
        source_zip="E:\\test.zip"
        target_dir="E:\\a\\"
        #print(systty,"这是一台windows机器!!!")
        print(systty,"thisi is windows machine!!!")
    elif system2.lower() == 'linux':
        flag = "/"
        source_zip="/data/helloworld309/showandtell-data/cocodata_test.zip"
        target_dir="/output/cocodata_test/"
        print(systty,"thisi is linux machine!!!")
    else:
        print("not found....!")
        sys.exit(1)
    myzip = zipfile.ZipFile(source_zip)
    myfilelist=myzip.namelist()
    for name in myfilelist:
        mylist = name.split('/')
        mylist.pop()
        tmp_dir = flag.join(mylist)
        base_dir = "%s%s" % (target_dir,tmp_dir)
        #print(base_dir)
        if os.path.isdir(base_dir):
            pass
        else:
            os.makedirs(base_dir)
        f_handle = open(target_dir+name,"wb")
        f_handle.write(myzip.read(name))
    f_handle.close()
unzip()
