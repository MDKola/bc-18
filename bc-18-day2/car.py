class Car(object):
    """class for modelling car activities
    """

    def __init__(self, name='General', model='GM', cartype=None):
        self.name = name
        self.model = model
        self.num_of_doors = 4
        self.cartype = cartype
        self.num_of_wheels = 4
        self.speed = 0
	


        if self.name == 'Porshe' or self.name == 'Koenigsegg':
            self.num_of_doors = 2

        if self.cartype != 'trailer':
            self.cartype = 'saloon'

        if self.cartype == 'trailer':
            self.num_of_wheels = 8

        

    def is_saloon(self):
        return self.cartype == 'saloon'
        #returns true for cartype saloon

    def drive(self, drive):
        #speed depending on cartype * drive
        
        if self.cartype == 'trailer':
            self.speed = drive * 77 / 7
        else:
            self.speed = drive * 1000 / 3

        return self