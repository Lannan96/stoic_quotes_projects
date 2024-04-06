class Quotes:
    '''
    This class is used to hold the quotes data and methods for scraping the quotes from the web.
    
    The class has the following attributes:
    - number_of_quotes: The total number of quotes
    - current_quote_idx: The current quote index
    - quotes: A list of quotes
    - quotes_file_exists: A boolean value to indicate if the quotes.txt file exists
    
    The class has the following methods:
    - scrape_quotes: Scrapes the quotes from the web and writes them to the quotes.txt file
    
    '''
    def __init__(self):
        '''
        
        '''
        self.__number_of_quotes = 0
        self.__current_quote_idx = -1
        self.__quotes = []
        self.__quotes_file_exists = False
        
        if self.__quotes_file_exists == False:
            self.scrape_quotes()
    
    def scrape_quotes(self):
        pass
    def get_current_quote(self):
        pass
    def check_all_quotes_sent(self):
        pass
