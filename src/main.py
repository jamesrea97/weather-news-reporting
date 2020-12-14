import scrapper


if __name__ == "__main__":
    scrapper = scrapper.Scrapper()

    print('\n')
    for report in scrapper.scrape():
        print(report)
        print('\n')
