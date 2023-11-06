#! /usr/bin/env python3
"""
ENIGMA2: Find a password from a hash password

This module allows you to retrieve a password from its hash
"""

import sys


if __name__ == "__main__":
    # Check if the user is using the correct version of Python
    python_version = sys.version.split()[0]

    if sys.version_info < (3, 6):
        print("Gpwd requires Python 3.6+\nYou are using Python %s, which is not supported by Sherlock" % (python_version))
        sys.exit(1)

    import enigma2
    enigma2.main()
