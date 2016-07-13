#!/usr/bin/env python
# Phillip J. Wolfram
# 07/13/2016

import re
import os

def process_config(fname): #{{{
    """ 
    Builds configuration file from *.csh environment variable commands to
    build python dictionary.
    
    Phillip J. Wolfram
    07/13/2016
    """
    # filter to convert input types into something python understands
    dictfilter = {'true': True, 'True': True, 'False': False, 'false': False}
    config = {}
    processformat = re.compile('\w*\s+(\w*)\s*(.*)\n')
    with open(fname, 'r') as af:
        for aline in af.readlines():
            keyvals = processformat.findall(aline)[0]
            config.update({keyvals[0]: dictfilter.get(keyvals[1], keyvals[1])})
    return config #}}}

def write_config(config, fname): #{{{
    with open(fname, 'w') as af:
        for akey in config:
            af.write('setenv %s %s\n'%(akey, config[akey]))

    return #}}}

def test(fname):
    print process_config(fname)

if __name__ == "__main__":
    test('global_config_example.csh')
