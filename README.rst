lxmlrpc - XMLRPClib patch
=========================

This module monkeypatch python's `xmlrpclib` to use `lxml <http://lxml.de>`__ based parser
to reduce memory consumption on big xmlrpc requests / responses (100+ Mb)


NOTE
----

This module is useful only for ***python2.7***.
Use it **only** if you suffer from **high memory usage** by **xmlrpclib**


Usage
-----

To use this module just do following:

```python

import xmlrpclib
import lxmlrpc

# This line will monkey-patch xmlrpclib to use lxml for parser
patch_xmlrpclib()
``` 

Benchmarks (how to run)
-----------------------

To run benchmarks:

1. install `memory_profiler <https://pypi.python.org/pypi/memory_profiler>`__
2. prepare data with ``python generate_data.py --path <demo data path> --size 50000000``
3. run benchmarks with ``python benchmark.py --path <demo data path>``



Benchmark results (50 Mb (real 65 Mb) data file)
================================================

look at ```p.feed(data)``` call in ```loads``` function of *xmlrpclib*

***Running unpatched loads***
Filename: /usr/lib/python2.7/xmlrpclib.py

Line #    Mem usage    Increment   Line Contents
------------------------------------------------
  1134    104.7 MiB      0.0 MiB   def loads(data, use_datetime=0):
  1135                                 """data -> unmarshalled data, method name
  1136                             
  1137                                 Convert an XML-RPC packet to unmarshalled data plus a method
  1138                                 name (None if not present).
  1139                             
  1140                                 If the XML-RPC packet represents a fault condition, this function
  1141                                 raises a Fault exception.
  1142                                 """
  1143    104.7 MiB      0.0 MiB       p, u = getparser(use_datetime=use_datetime)
->1144    622.4 MiB    517.7 MiB       p.feed(data)
  1145    558.0 MiB    -64.4 MiB       p.close()
  1146    558.0 MiB      0.0 MiB       return u.close(), u.getmethodname()


***Running patched loads***
Filename: /usr/lib/python2.7/xmlrpclib.py

Line #    Mem usage    Increment   Line Contents
------------------------------------------------
  1134    106.9 MiB      0.0 MiB   def loads(data, use_datetime=0):
  1135                                 """data -> unmarshalled data, method name
  1136                             
  1137                                 Convert an XML-RPC packet to unmarshalled data plus a method
  1138                                 name (None if not present).
  1139                             
  1140                                 If the XML-RPC packet represents a fault condition, this function
  1141                                 raises a Fault exception.
  1142                                 """
  1143    106.9 MiB      0.0 MiB       p, u = getparser(use_datetime=use_datetime)
->1144    235.9 MiB    129.0 MiB       p.feed(data)
  1145    171.5 MiB    -64.4 MiB       p.close()
  1146    171.5 MiB      0.0 MiB       return u.close(), u.getmethodname()


Filename: bechmark.py

Line #    Mem usage    Increment   Line Contents
------------------------------------------------
    13    104.7 MiB      0.0 MiB   @profile
    14                             def bench_load(xmldata):
    15    104.7 MiB      0.0 MiB       print ("Running unpatched loads")
    16    106.9 MiB      2.2 MiB       loads(xmldata)
    17                             
    18    106.9 MiB      0.0 MiB       lxmlrpc.patch_xmlrpclib()
    19                             
    20    106.9 MiB      0.0 MiB       print ("Running patched loads")
    21    107.1 MiB      0.2 MiB       loads(xmldata)



Benchmark results (100 Mb (real 129 Mb) data file)
==================================================

***Running unpatched loads***

---

Filename: /usr/lib/python2.7/xmlrpclib.py

Line #    Mem usage    Increment   Line Contents
------------------------------------------------
  1134    169.2 MiB      0.0 MiB   def loads(data, use_datetime=0):
  1135                                 """data -> unmarshalled data, method name
  1136                             
  1137                                 Convert an XML-RPC packet to unmarshalled data plus a method
  1138                                 name (None if not present).
  1139                             
  1140                                 If the XML-RPC packet represents a fault condition, this function
  1141                                 raises a Fault exception.
  1142                                 """
  1143    169.2 MiB      0.0 MiB       p, u = getparser(use_datetime=use_datetime)
->1144   1203.0 MiB   1033.8 MiB       p.feed(data)
  1145   1074.2 MiB   -128.8 MiB       p.close()
  1146   1074.2 MiB      0.0 MiB       return u.close(), u.getmethodname()


***Running patched loads***

---

Filename: /usr/lib/python2.7/xmlrpclib.py

Line #    Mem usage    Increment   Line Contents
------------------------------------------------
  1134    171.6 MiB      0.0 MiB   def loads(data, use_datetime=0):
  1135                                 """data -> unmarshalled data, method name
  1136                             
  1137                                 Convert an XML-RPC packet to unmarshalled data plus a method
  1138                                 name (None if not present).
  1139                             
  1140                                 If the XML-RPC packet represents a fault condition, this function
  1141                                 raises a Fault exception.
  1142                                 """
  1143    171.6 MiB      0.0 MiB       p, u = getparser(use_datetime=use_datetime)
->1144    429.4 MiB    257.8 MiB       p.feed(data)
  1145    300.6 MiB   -128.8 MiB       p.close()
  1146    300.6 MiB      0.0 MiB       return u.close(), u.getmethodname()


Filename: bechmark.py

Line #    Mem usage    Increment   Line Contents
------------------------------------------------
    13    169.2 MiB      0.0 MiB   @profile
    14                             def bench_load(xmldata):
    15    169.2 MiB      0.0 MiB       print ("Running unpatched loads")
    16    171.6 MiB      2.4 MiB       loads(xmldata)
    17                             
    18    171.6 MiB      0.0 MiB       lxmlrpc.patch_xmlrpclib()
    19                             
    20    171.6 MiB      0.0 MiB       print ("Running patched loads")
    21    171.8 MiB      0.2 MiB       loads(xmldata)

