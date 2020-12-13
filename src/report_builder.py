''' Module builds weather and news report based on scrapped data '''\


class ReportBuilder:
    
    @classmethod
    def builds_weather_report(cls):
        ''' Builds weather report '''
        # TODO
        pass

    @classmethod
    def build_news_report(cls, time, headline):
        ''' Builds news report '''
        return time + ' - BBC News - ' + headline


