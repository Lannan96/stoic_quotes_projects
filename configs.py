import json

class Configs:
    
    def __init__(self):
    
        try:
            self.read_config_file()
        except FileNotFoundError:
            print('Config file not found: Creating config file... \n')
            self.create_config_file()
        
    
    def create_config_file(self):
        with open('configs.json', 'w') as file:
                file.write('{\n')
                file.write(' "quotes_length": 0" \n')
                file.write(' "current_quote_number": 0" \n')
                file.write('}')
    
    def read_config_file(self):
        '''
        Attempts to read the config file and assign the values to the class variables
        
        
        '''

        with open('configs.json', 'r') as file:
            config = json.load(file)
    
            # get the config settings
            quotes_length = config['quotes_length']
            current_quote_number = config['current_quote_number']

            if quotes_length > 1:
                # if it does, we already have our quotes text file to read from
                quotes_txt_exists = True
        
            else:
                pass
                # run scraper

    
