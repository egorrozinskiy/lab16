import argparse
import sys
parser = argparse.ArgumentParser(
    description='Calc'
)
parser.add_argument(
    'values',
    metavar='VALUES',
    type=float,
    nargs=2,
    help='data'
)
parser.add_argument(
    '-a',
    '--action',
    nargs='+',
    metavar='SIGN',
    help='sign'
)
parser.add_argument(
    '-v',
    '--verbose',
    action='store_true',
    help='result'
)
args = parser.parse_args()
print(args.action)
if not args.action[0] in  ['+', '-', '*', '/']:
    print(
        'incor sign'
    )
    sys.exit(-1)

   
if args.action[0] == '+':
    result = float(args.values[0]) + float(args.values[1])
elif args.action[0] == '-':
    result = float(args.values[0]) - float(args.values[1])
elif args.action[0] == '*':
    result = float(args.values[0]) * float(args.values[1])
elif args.action[0] == '/':
    result = float(args.values[0]) / float(args.values[1])

if args.verbose:
    print('Result', result)