''' Main Module for Project '''

import sys
import scrapper
import deployment


def print_reports():
    ''' Prints reports to the Terminal '''
    print('\n')
    for report in scrapper.scrape():
        print(report)
        print('\n')


if __name__ == "__main__":
    scrapper = scrapper.Scrapper()

    if sys.argv[1] == '-d':
        deployment.deploy()

    print_reports()
