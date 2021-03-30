# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 14:38:19 2021

@author: moghe
"""

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number",
                    type=int)
args = parser.parse_args()
print(args.square**2)