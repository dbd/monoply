import os
from connectors.discover import Discover
from connectors.greatlakes import GreatLakes
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    # Discover
    parser.add_argument('-d', '--discover', action='store_true',
                        help='Get the discover loan balance')
    parser.add_argument('--discover-user', action='store',
                        dest='discover_user', help='User to use for discover')
    parser.add_argument('--discover-pass', action='store',
                        dest='discover_pass',
                        help=('Password to use for discover. '
                              'Default: env DISCOVER_PASS'),
                        default=os.environ.get('DISCOVER_PASS'))
    # GreatLakes
    parser.add_argument('-g', '--greatlakes', action='store_true',
                        help='Get the great lakes loan balance')
    parser.add_argument('--greatlakes-pin', action='store',
                        dest='greatlakes_pin',
                        help='PIN to use for Great Lakes')
    parser.add_argument('--greatlakes-user', action='store',
                        dest='greatlakes_user',
                        help='User to use for Great Lakes')
    parser.add_argument('--greatlakes-pass', action='store',
                        dest='greatlakes_pass',
                        help=('Password to use for Great Lakes. '
                              'Default: env GREATLAKES_PASS'),
                        default=os.environ.get('GREATLAKES_PASS'))
    return parser.parse_args()


def main():
    if args.discover:
        if args.discover_user and args.discover_pass:
            discover = Discover(args.discover_user, args.discover_pass)
            discover_balance = discover.getBalance()
            print(discover_balance)
        else:
            print('--discover_pass and (--discover-pass or DISCOVER_PASS) '
                  'are required to get Discover loan information')
    if args.greatlakes:
        if args.greatlakes_user and args.greatlakes_pass:
            greatlakes = GreatLakes(args.greatlakes_user,
                                    args.greatlakes_pass,
                                    args.greatlakes_pin)
            greatlakes_balance = greatlakes.getBalance()
            print(greatlakes_balance)
        else:
            print('--greatlakes-user and '
                  '(--greatlakes-pass or GREATLAKES_PASS) '
                  'are required to get GreatLakes loan information')


if __name__ == '__main__':
    args = parse_args()

    main()
