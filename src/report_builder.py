''' Module builds weather and news report based on scrapped data '''\



class ReportBuilder:

    @classmethod
    def build_weather_report(cls, time, temperature):
        ''' Builds weather report '''

        return ('Weather Report London -: ' + time + ' - ' + temperature
                )

    @classmethod
    def build_news_report(cls, time, headline):
        ''' Builds news report '''
        return 'BBC News Report -: ' + time + ' - ' + headline

    @classmethod
    def print_reports(cls, reports):
        ''' Prints reports to the Terminal '''

        print('#### NEWS AND WEATHER REPORT ####')
        print('\n')
        for report in reports:
            print(report)
            print('\n')
        print('####     END  REPORT     ####')
