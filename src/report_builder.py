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
