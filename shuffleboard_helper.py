from wpilib import SmartDashboard as sd

class ShuffleboardHelper:

    '''
    A helper class for using shuffleboard variables as regular variables.
    '''

    def setup(self):
        pass

    def updateVal(self, dictionary: dict):

        '''
        A class that updates int/bool/float variables. Probably best to call this in .execute() function of the subsystem. Example code on how you can use this with magicbot is in lines 42-66, just ctrl+left click on this method. \n
        !!! THE KEYS OF THE VARIABLES SHOULD THE STRING FORM OF THE VARIABLE'S NAME !!!

        @param1: Dictionary which contains the variables
        '''

        new_dict = {}
        variables = list(dictionary.values())
        keys = list(dictionary.keys())
        
        for index,i in enumerate(variables):
            type_of_i = type(i)
            print(keys[index])

            if type_of_i == int or type_of_i == float:
                val = sd.getNumber(str(keys[index]), None)
            
            elif type_of_i == bool:
                val = sd.getBoolean(str(keys[index]), None)
            
            else:
                raise Exception(f"{i} is not an int/bool/float. If you see this in comp, beware that i am your old self before cussing.")

            new_dict.update({keys[index]: val})
                
        return new_dict

        # from shuffleboardhelper import ShuffleboardHelper

        # class deneme:

        #     helper: ShuffleboardHelper

        #     a = 0
        #     b = 1
        #     c = 2

        #     def setup(self):
        #         self.helper.createVal("a", 4)

        #     def execute(self):
        #         values_dict = {
        #             "a": self.a,
        #         }

        #         new_vals_dict = self.helper.updateVal(values_dict)

        #         keys = list(new_vals_dict.keys())
        #         vals = list(new_vals_dict.values())

        #         for i, val in enumerate(vals):
        #             exec(f'self.{keys[i]} = {val}')
    
    def createVal(self, name:str, val):
        type_of_val = type(val)

        if type_of_val == int or type_of_val == float:
            sd.putNumber(str(name), val)
        
        elif type_of_val == bool:
            sd.putBoolean(str(name), val)
        
        else:
            raise Exception(f"{val} is not an int/bool/float. If you see this in comp, beware that i am your old self before cussing.")
        
        return val
    
    def execute(self):
        pass