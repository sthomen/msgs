Msgs applet for PyMDCMS
=======================

This is an applet that can be loaded by pymdcms. Place the code in a directory
in the `apps` directory of pymdcms, it expects the Applet superclass to reside
in the parent directory of this module.

Example cms.conf fragment:

```
[apps]
messages = apps.msgs.msgs.Msgs
```

Configuration options
---------------------

An *optional* messages section can be added to your `cms.conf` in order to
load the msgs from an alternate directory.

This module is based on the BSD msgs program and will expect a file called
`bounds` to exist in the path with the upper and lower bound separated by a
space, and that the messages themselves are rfc822 email files named by their
index number. (e.g. a bounds file with "0 1" would expect a file named 0 and 1).

```
[messages]
path = /var/msgs
```
