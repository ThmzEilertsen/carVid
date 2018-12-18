#!/usr/bin/env python3

import slugify
from sys import argv

print(slugify.slugify(argv[1][:-3]))
