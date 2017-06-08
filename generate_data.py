# -*- coding: utf-8 -*-
import argparse
import random
import base64
import xmlrpclib


def prepare_data(size):
    """ generate random data
    """
    chunk_size = 2000000
    generated = 0
    todo_size = size
    data = b''
    while todo_size > 0:
        chunk = chunk_size if todo_size > chunk_size else todo_size
        data += b''.join(chr(random.randrange(0,254)) for _ in xrange(chunk))
        todo_size -= chunk

    return base64.encodestring(data)

def prepare_xml(data):
    """ Prepare test xml with specified data
    """
    return xmlrpclib.dumps(('test-data', 42, 'z-test-222452', data),
                           methodname='testMethod54')


def prepare_data_file(data_path, data_size):
    with open(data_path, 'wt') as f:
        f.write(
            prepare_xml(
                prepare_data(data_size)
            )
        )

def main():
    parser = argparse.ArgumentParser(description='Generate test data.')
    parser.add_argument('--size', type=int,
                        help='How many bytes of demo data to be generated.')
    parser.add_argument('--path', type=str,
                        help='Path to file to save demo data in')
    args = parser.parse_args()
    prepare_data_file(args.path, args.size)

if __name__ == '__main__':
    main()
