import meet

meet_urls = {
    '國文':'https://meet.google.com/lookup/cum3hsamhz',
    '閱讀理解與表達':'https://meet.google.com/lookup/huqchbqg6n',
    '化學':'https://meet.google.com/lookup/djnrvglhnd',
    '地理':'https://meet.google.com/lookup/dt4cuvznvr',
    '體育':'https://meet.google.com/lookup/as3tjorhxn',
    '歷史':'https://meet.google.com/lookup/acdbopx4tq',
    '生命教育':'',
    '音樂':'https://meet.google.com/lookup/er3x3kndxe',
    '生物':'https://meet.google.com/lookup/c6mnkq6efh',
    '資訊':'https://meet.google.com/lookup/h5xipou4b3',
    '多元選修':'https://meet.google.com/lookup/d3r2azaeym'
}

class others:
    def __init__(self, subject, chrome):
        self.subject = subject
        self.chrome = chrome
        
        meet_url = meet_urls[self.subject]
        self.chrome.get(meet_url)
        meet.enter_meet(self.chrome)
        