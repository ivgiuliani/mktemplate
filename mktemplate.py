#!/usr/bin/env python

import os
import shutil
import sys

def main(args):
    if not 2 <= len(args) <= 3:
        help_message()
        return True
    
    template_dir = os.path.join(os.path.expanduser("~"), ".mktemplates")

    if args[1] == "--list":
        for item in listdir(template_dir):
            if os.path.isdir(os.path.join(template_dir, item)):
                print "%s [d]" % item
            else:
                print item
        return False

    template_name = args[1]
    output_file = template_name
    if len(args) == 3:
        output_file = args[2]

    template = os.path.join(template_dir, template_name)
    if os.path.isfile(template) or os.path.isdir(template):
        shutil.copy(os.path.join(template_dir, template_name), output_file)
    else:
        print("Template doesn't exist, use --list to show available templates")

    return False

def listdir(path):
    dirs = []
    if os.path.isdir(path):
        dirs = sorted([d for d in os.listdir(path) if os.path.isdir(path + os.path.sep + d)])
        dirs.extend(sorted([f for f in os.listdir(path) if os.path.isfile(path + os.path.sep + f)]))
    return dirs

def help_message():
    print "Usage: mktemplate [--list] <template_name> [<output_file>]"

if __name__ == '__main__':
    sys.exit(main(sys.argv))
