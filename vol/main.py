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

import subprocess
import sys
from . import __version__ as version

from docopt import docopt


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

    return asrun('set volume {0} volume {1}'.format(device, amount) )

def main():
    "Run the main programm."
    args = docopt(__doc__, version='vol version '+ version)
    
    #print args ## todo delete!
    
    if args['load'] and args['<profile>']:
        print args['<profile>']
        ## todo implement!

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
