''' Main Module for Project '''

import sys
import scrapper
import deployment
import report_builder


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == '-d':
            deployment.deploy()

    scrapper = scrapper.Scrapper()
    report_builder = report_builder.ReportBuilder()

    report_builder.print_reports(scrapper.scrape())
