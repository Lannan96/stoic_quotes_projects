import scrapy
import json

# intialise configs
configs = configs()

# check if quotes text file exists
if configs['quotes_txt_exists']:
    # check if quotes_txt_length is less than number_of_quotes
    if configs['quotes_length'] < configs['number_of_quotes']:
        # send current quote
        pass
    else:
        # send message that we have read all the quotes
        pass
else:
    # run scraper
    pass


'''
# check to see if the quotes_length variable is greater than 1 meaning we already have our quotes_txt file
try:
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
except FileNotFoundError:
    print('Config file not found: Creating config file... \n')
    with open('configs.json', 'w') as file:
        file.write('{\n')
        file.write(' "quotes_length": 0" \n')
        file.write(' "current_quote_number": 0" \n')
        file.write('}')


print(f'The quote length is: {quotes_length}')
 # check to see if the quotes_length variable is equal to the length of the quotes list

 # check if we have already sent all the quotes from our quotes_file


if current_quote_number < quotes_length:
    # get quote
    pass
else:
    pass
    # message that we have read all the quotes already





# run the setup.py file to install the packages and set up the project structure

# check to see if the quotes text file exists
# if it does, open it in read mode and read the contents
# if it does not, create it and open it in write mode

'''