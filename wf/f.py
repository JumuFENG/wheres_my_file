# Python 2
# -*- coding: utf-8 -*-

import os
import sys
import argparse
import json
from subprocess import Popen

parser = argparse.ArgumentParser(description="where is my file")
parser.add_argument("-r", "--run", help="the executable file or file path to run.")
parser.add_argument("-s", "--start_work", help="run the programs in the start work list.", action="store_true")

args = parser.parse_args()
run = args.run
start_work = args.start_work

try:
    approot = os.path.dirname(os.path.abspath(__file__))
except NameError:  # We are the main py2exe script, not a module
    approot = os.path.dirname(sys.executable)

config_file = open(approot + os.sep + "wmf_config")
configurations = json.load(config_file)
alias_list = configurations["alias"]

def start_working_program_list():
    plist = configurations["start_list_work"]
    for prog in plist:
        if find_exe_and_open(prog):
            print("run program {0} in start working list".format(prog))
        else:
            print("can't find {0}".format(prog))

def run_portable(name):
    Popen(name)

def find_exe_and_open(exe_name):
    if os.path.exists(exe_name):
        run_portable(exe_name)
        return True

    root = approot
    exe_fullname = ""

    if os.path.exists(root + os.sep + exe_name + os.sep + exe_name + ".exe"):
        run_portable(root + os.sep + exe_name + os.sep + exe_name + ".exe")
        return True

    for parent, dirs, files in os.walk(root):
        for f in files:
            if f == exe_name:
                run_portable(os.path.join(parent, f))
                return True
            fname = os.path.splitext(f)
            if fname[0] == exe_name:
                exe_fullname = os.path.join(parent, f)
                run_portable(exe_fullname)
                return True
    return False

if start_work:
    start_working_program_list()
    sys.exit(0)

if not find_exe_and_open(alias_list.get(run, run)):
    print("Can't find any executable file named {0}".format(run))