import scrapy
import json
import pywhatkit
from configs import Configs
from quotes import Quotes

# intialise configs, read in values or create config file if it does not exist
configs = Configs()

# add contact numbers to the config file
configs.add_contact_numbers('07904818817', 'Lewis')

# print the contact numbers
for number, name in configs.get_contact_numbers().items():
    print(f'{name}: {number}')

# intialise quotes, read in values or scrape quotes if quotes file does not exist
#quotes = Quotes()

# check if we have already sent all the quotes from our quotes_file
#if quotes.check_all_quotes_sent() == False:
    # send quote
     #quote = quotes.get_current_quote()
        # send message to all contact numbers
        #for number in configs.contact_numbers:
            #pywhatkit.sendwhatmsg(number, quote, 9, 0)
#    pass

#else:
    # message that we have read all the quotes already

        #quote = 'All quotes have been sent'
        # send message to all contact numbers
        #for number in configs.contact_numbers:
            #pywhatkit.sendwhatmsg(number, quote, 9, 0)
#    pass