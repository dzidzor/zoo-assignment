class Zoo:
    def __init__(self,zoo_name,location,size,history):
        self.zoo_name = zoo_name
        self.location = location
        self.size = size
        self.hidtory = history

    def getZooDetails(self):
        pass

##ANIMALS

        
class Animal():
    def __init__(self, name, animal_status, feeding_type,no_species,sound,weight):
        self.name = name
        self.feeding_type = feeding_type
        self.animal_status = animal_status
        self.activities = []
        self.sound = sound
        self.no_of_animal = no_of_species
        self.weight = weight
        
    def animalActivity(self, activity):
        self.activities.append(activity)

    def getSound(self):
        return sound
    
    def getInfo(self):
        pass

    def getWeight(self):
        pass

    def getName(self):
        pass
    
    
   ##subclasses of Animal class
    
    class Mammal(Animal):
        def __init__(self, gestationPeriod, name, animal_status, feeding_type,no_species,sound,weight)
            Animal.__init(self,name, animal_status, feeding_type,no_species,sound,weight)
            self.gestationPeriod = gestationPeriod

        

        
    class Bird(Animal):
        def __init__(self,typeOfBeak,typeOfFeathers,name,animal_status, feeding_type,no_species,sound,weight):
            Animal.__init(self,name, animal_status, feeding_type,no_species,sound,weight)
            self.typeOfFeathers = typeOfFeathers
            self.typeOfbeak = typeOfFeathers


            
    class Reptile(Animal):
        def __init__(self,sname, animal_status, feeding_type,no_species,sound,weight)):
            Animal.__init(self,name, animal_status, feeding_type,no_species,sound,weight)

    class Amphibian(Animal):
        def __init__(self):
            Animal.__init(self,name, animal_status, feeding_type,no_species,sound,weight)
            

    class Invertibrate(Animal): """eg Spiders animals wt no back bones"""
        def __init__(self,numberOflegs,name, animal_status, feeding_type,no_species,sound,weight):
            Animal.__init(self,name, animal_status, feeding_type,no_species,sound,weight)
            self.numberOflegs = numberOflegs

        def getNumberOflegs(self):
            pass

    class Fish(Animal):
        def __init__(self, typeOfWater,name, animal_status, feeding_type,no_species,sound,weight):
            Animal.__init(self,name, animal_status, feeding_type,no_species,sound,weight)
            self.typeOfWater = typeOfWater
        


##HUMANS
class People:

class Group:

     def __init__(self,group_name, group_num):
        self.g_name = group_name
        self.p = group_num


class Person:
    def __init__(self,p_name, p_type):
        self.p_name = p_name
        self.p_type = p_type

        
class Visitor(Person):
    def __init__(self,visitor_type):
        Person.__init__()
        self.task=task
        self.visitor_type = visitor_type

class Worker(Person):
    Person.__init__()
    def __init__(self):





##BUILDINGS       


class Building:
    def __init__():
        
        
        
class Restaurant(Building):
    def __init__():
        Building.__init__()

class Vertinary(Building):
    def __init__():
        Building.__init()

class Clinic(Building):
    def __init__():
            Building.__init()

class Administration(Building):
    def __init__():
            Building.__init()

class RecreationalCenter(Building):
    def __init__():
        Building.__init__()

class StoreHouse(Building):
    def __init__():
        Building.__init__()



