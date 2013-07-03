#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""vol

volume control in the shell for your mac

Usage:
    vol (in|out|alert) <volume>
    vol mute
    vol unmute
    vol load <profile>
    vol info

    vol (-h | --help)
    vol --version

Options:
    -h --help     Show this screen.
    --version     Show version.

"""

import ConfigParser
import os
import subprocess
import sys

from docopt import docopt

from . import __version__ as version


def asrun(ascript):
    "Run the given AppleScript and return the standard output and error."

    ## shamelessly stolen from  
    ## http://www.leancrew.com/all-this/2013/03/combining-python-and-applescript/

    osa = subprocess.Popen(['osascript', '-'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE)

    return osa.communicate(ascript)[0]

def setvolume(device, amount):
    "Set the volume to 'amount' on 'device' "

    if device == 'out':
        device = 'output'
    if device == 'in':
        device = 'input'

    cmd = 'set volume {0} volume {1}'.format(device, amount) 
    return asrun(cmd)

def main():
    "Run the main programm."
    args = docopt(__doc__, version='vol version '+ version)
    
    #print args ## todo delete!
    
    if args['load'] and args['<profile>']:

        home = os.path.expanduser("~")
        cfile = os.path.join(home, '.vol')

        try:
            cfg = ConfigParser.RawConfigParser()
            cfg.read(cfile)

            profile = args['<profile>']
 
            if cfg.has_section(profile):
                for o in cfg.options(profile):
                    if o == 'out' or o == 'in' or o == 'alert':
                        setvolume(o, cfg.get(profile, o))
                    elif o == 'mute':
                        if cfg.getboolean(profile, o):
                            asrun('set volume output muted true')
                        else:
                            asrun('set volume output muted false')
            else:
                raise Error

        except Exception, e:
            print "Error: {0} in {1} does not exist or is malformed".format(args['<profile>'], cfile)


    elif args['info']:
        print asrun('get volume settings')

    elif args['mute']:
        asrun('set volume output muted true')

    elif args['unmute']:
        asrun('set volume output muted false')

    elif args['out']:
        setvolume('out', args['<volume>']) 

    elif args['in']:
        setvolume('in', args['<volume>'])

    elif args['alert']:
        setvolume('alert', args['<volume>'])


    sys.exit(0)
