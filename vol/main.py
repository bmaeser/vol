#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""vol

volume control in the shell for your mac

Usage:
    vol (in|out) <volume>
    vol load <profile>

    vol (-h | --help)
    vol --version

Options:
    -h --help     Show this screen.
    --version     Show version.

"""


import sys
import vol

from docopt import docopt


def setvolume(device, amount):
    # set amount, if mute or full translate to integer
    print amount

def main():
    args = docopt(__doc__, version='vol version '+vol.__version__)
    
    print args ## todo delete!
    
    if args['load'] and args['<profile>']:
        print args['<profile>']
        ## todo implement!
    elif args['out']:
        setvolume('out', args['<volume>']) 
    elif args['in']:
        setvolume('in', args['<volume>'])


    sys.exit(0)