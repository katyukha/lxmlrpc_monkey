# -*- coding: utf-8 -*-
from memory_profiler import profile

import argparse
import xmlrpclib

import lxmlrpc


loads = profile(xmlrpclib.loads)

@profile
def bench_load(xmldata):
    print ("Running unpatched loads")
    loads(xmldata)

    lxmlrpc.patch_xmlrpclib()

    print ("Running patched loads")
    loads(xmldata)

def main():
    parser = argparse.ArgumentParser(description='Do benchmark')
    parser.add_argument('--path', type=str,
                        help='Path to file to with test data')
    args = parser.parse_args()

    # Load data from file
    data = open(args.path, 'rt').read()

    # Do actual benchmarking
    bench_load(data)

if __name__ == '__main__':
    main()

