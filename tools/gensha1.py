#!/usr/bin/python

import os
import hashlib
import json
import collections

def gen_file(path):
    f = open(path, 'r')
    content = f.read()
    f.close()
    return hashlib.sha1(content).hexdigest()

def gen_dir(path):
    prefix = os.path.split(path)[1]
    sha1s = {}
    for item in os.listdir(path):
        itempath = os.path.join(path, item)
        sha1hex = gen_file(itempath)
        value = os.path.join(prefix, item)
        key = sha1hex
        sha1s[key] = value

    return sha1s

def gen_all(filepath):
    #sha1s = collections.OrderedDict()
    sha1s = {}
    res = gen_dir('../js')
    sha1s.update(res)

    res = gen_dir('../css')
    sha1s.update(res)

    res = gen_dir('../images')
    sha1s.update(res)

    res = gen_dir('../fonts')
    sha1s.update(res)

    sha1s[gen_file('../index.html')] = 'index.html'
    sha1s[gen_file('../README.md')] = 'README.md'
    sha1s[gen_file('../LICENSE')] = 'LICENSE'

    sha1s = collections.OrderedDict(sorted(sha1s.iteritems(), key=lambda x: x[1]))

    f = open(filepath, 'w')
    json.dump(sha1s, f, indent=4)
    f.close()

if __name__ == '__main__':
    gen_all('../sha1sum')
