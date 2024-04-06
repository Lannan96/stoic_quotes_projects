import json

class Configs:
    '''
    This class is used to hold configuration settings for the project. These settings are read from a json file called configs.json.
    If the file doesn't exist, the class will create the file and write the default settings to it.
    
    The class has the following attributes:
    - __contact_numbers: A private dictionary of contact names and numbers to send the quotes to in the format {number: name}
    
    The class has the following methods:
    - create_config_file: Creates the config file with default settings
    - read_config_file: Reads the config file and assigns the values to the class attributes
    - add_contact_numbers: Adds a contact number to the contact_numbers dictionary
    - get_contact_numbers: Returns the contact_numbers dictionary
    '''
    
    def __init__(self):
        '''
        The constructor for the Configs class.
        '''
        self.__contact_numbers = {}
        self.read_config_file()
    
     
    def create_config_file(self):
        '''
        This function is used to create the config file with default settings.
        '''
        print('Config file not found: Creating config file... \n')
        with open('configs.json', 'w') as file:
                file.write('{\n')
                file.write(' "contact_numbers": {}')
                file.write('\n}')
        self.read_config_file()

    
    def read_config_file(self):
        '''
        Attempts to read the config file and assign the values to the class attributes. 
        If the file does not exist, it will call the create_config_file method.
        
        '''
        print('Reading config file...')
        try:
            with open('configs.json', 'r') as file:
                config = json.load(file)
    
                # get the config settings
                self.contact_numbers = config['contact_numbers']

        except FileNotFoundError:
            self.create_config_file()
    
    def add_contact_numbers(self,number, name):
        '''
        This function is used to add contact numbers to the contact_numbers dictionary and write them to the configs.json file.
        
        Args:
        - name: The name of the contact
        - number: The number of the contact
        '''
        
        print('Adding contact number...')
        # add the contact number to the dictionary object if it doesn't already exist, if it does update the name
        self.contact_numbers[number] = name
        
        # write the updated dictionary to the config file
        with open('configs.json', 'w') as file:
            json.dump({"contact_numbers": self.contact_numbers}, file)

    def get_contact_numbers(self):
        '''
        This function is used to return the contact_numbers dictionary.
                
        Returns:
        - contact_numbers: The dictionary of contact numbers
        '''
        return self.contact_numbers