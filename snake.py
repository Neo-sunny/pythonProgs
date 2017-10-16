class snake:
    poison='venom'    # shared by all instances

    def __init__(self, name):
        self.name=name        # instance variable unique to each instance
        
    def change_name(self, new_name):
        self.name=new_name

cobra= snake('cobra') 
print(cobra.name)       
