import os
from connectors.discover import Discover
from connectors.greatlakes import GreatLakes
from connectors.heartland import Heartland
from connectors.nelnet import Nelnet
import settings
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    # Heartland
    parser.add_argument('--heartland-user', action='store',
                        dest='heartland_user',
                        help='User to use for heartland')
    parser.add_argument('--heartland-pass', action='store',
                        dest='heartland_pass',
                        help=('Password to use for heartland. '
                              'Default: env HEARTLAND_PASS'),
                        default=os.environ.get('HEARTLAND_PASS'))
    # Nelnet
    parser.add_argument('--nelnet-user', action='store',
                        dest='nelnet_user', help='User to use for nelnet')
    parser.add_argument('--nelnet-pass', action='store',
                        dest='nelnet_pass',
                        help=('Password to use for nelnet. '
                              'Default: env NELNET_PASS'),
                        default=os.environ.get('NELNET_PASS'))
    # Discover
    parser.add_argument('--discover-user', action='store',
                        dest='discover_user', help='User to use for discover')
    parser.add_argument('--discover-pass', action='store',
                        dest='discover_pass',
                        help=('Password to use for discover. '
                              'Default: env DISCOVER_PASS'),
                        default=os.environ.get('DISCOVER_PASS'))
    # GreatLakes
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

    if (args.discover_user and args.discover_pass):
        discover = Discover(args.discover_user, args.discover_pass)
        discover_balance = discover.getBalance()
        print(f'Discover Balance: {discover_balance}')
    elif (args.discover_user and not args.discover_pass):
        print('--discover_pass and (--discover-pass or DISCOVER_PASS) '
              'are required to get Discover loan information')

    if (args.greatlakes_user and args.greatlakes_pass):
        greatlakes = GreatLakes(args.greatlakes_user,
                                args.greatlakes_pass,
                                args.greatlakes_pin)
        greatlakes_balance = greatlakes.getBalance()
        print(f'Great Lakes Balance: {greatlakes_balance}')
    elif (args.greatlakes_user and not args.greatlakes_pass):
        print('--greatlakes-user and '
              '(--greatlakes-pass or GREATLAKES_PASS) '
              'are required to get GreatLakes loan information')

    if (args.heartland_user and args.heartland_pass):
        heartland = Heartland(args.heartland_user,
                              args.heartland_pass,
                              security_questions=settings.SECURITY_QUESTIONS)
        heartland_balance = heartland.getBalance()
        print(f'Heartland Balance: {heartland_balance}')
    elif (args.heartland_user and not args.heartland_pass):
        print('--heartland-user and '
              '(--heartland-pass or HEARTLAND_PASS) '
              'are required to get Heartland loan information')

    if (args.nelnet_user and args.nelnet_pass):
        nelnet = Nelnet(args.nelnet_user,
                        args.nelnet_pass)
        nelnet_balance = nelnet.getBalance()
        print(f'Nelnet Balance: {nelnet_balance}')
    elif (args.nelnet_user and not args.nelnet_pass):
        print('--nelnet-user and '
              '(--nelnet-pass or NELNET_PASS) '
              'are required to get Nelnet loan information')


if __name__ == '__main__':
    args = parse_args()

    main()
