

import argparse


parser = argparse.ArgumentParser(
prog='app'
)

parser.add_argument('f')

args = vars(parser.parse_args())

txt_file = args['f']

if txt_file is not None:
  with open(txt_file) as ot:
    line = ot.readlines()[0]
    print(line)


