import json
from datetime import datetime

class Junk_Shop:
    __junk = {
        'Metal' : {'Weight' : 0, 'Buying Price' : 0, 'Selling Price' : 0, 'PnL' : 0},
        'PET' : {'Weight' : 0, 'Buying Price' : 0, 'Selling Price' : 0, 'PnL' : 0},
        'Bronze' : {'Weight' : 0, 'Buying Price' : 0, 'Selling Price' : 0, 'PnL' : 0},
        'Alluminum' : {'Weight' : 0, 'Buying Price' : 0, 'Selling Price' : 0, 'PnL' : 0},
        'Lata' : {'Weight' : 0, 'Buying Price' : 0, 'Selling Price' : 0, 'PnL' : 0},
    }
    
    
    def _get_junk(self):
        return self.__junk
    
    def __add_to_db(self):
        with open(f"{datetime.now().strftime('%B %Y')}.json", 'a') as jsfile:
            jsfile.write(f'{self._get_junk}')
            jsfile.close()