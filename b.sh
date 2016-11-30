#!/bin/bash
nohup python argparse_test.py test_0 1 > /dev/null 2>&1 &
sleep 0.01
nohup python argparse_test.py test_1 1 > /dev/null 2>&1 &
sleep 1.5
nohup python argparse_test.py test_3 1 > /dev/null 2>&1 &
sleep 0.01
nohup python argparse_test.py test_4 1 > /dev/null 2>&1 &
