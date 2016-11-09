#!/usr/bin/env python

import os
#os.system("./lasershark_stdin_circlemaker | ./lasershark_stdin")
#os.system("./lasershark_stdin_square | ./lasershark_stdin")
os.system("python ./trace.py | ./lasershark_stdin")
