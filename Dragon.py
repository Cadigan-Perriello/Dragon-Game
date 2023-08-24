'''
Created on Jan 6, 2023

@author: cadiganperriello
'''
# from ctypes.test.test_pickling import name
# from test.test_largefile import size

class Dragon:
    total_Dragons_Alive = 0;
    def __init__(self, name:str, color:str, size, fire_breather:bool):
        self.name = name
        self.color = color
        self.size = size
        self.health = 100
        self.kills = 0
        self.fire_breather = fire_breather
        self.total_Dragons_Alive+=1


    def getName(self):
        return self.name
    
    def getColor(self):
        return self.color
    
    def getSize(self):
        return self.size
    
    def getHealth(self):
        return self.health
    
    def getKills(self):
        return self.kills
    
    def getFireBreather(self):
        return self.fire_breather
    
    def getTotalDragonsAlive(self):
        return self.total_Dragons_Alive
    
    def attack(self, target):
        target_Alive = True
        
        if self.health<=0:
            print("You cannot attack anymore.")
        elif target.health<=0:
            print(target.name + " is already dead. You cannot attack them.")
            target_Alive = False
        elif self.fire_breather:
            target.health-=20
            if target.health>= 0: 
                print(self.name + " health ", self.health)
                print(target.name + " health: ",  target.health)
        elif not self.fire_breather:
            target.health-=10
            if target.health>= 0:
                print(self.name + " health ", self.health)
                print(target.name + " health: ", target.health)
        if target.health <= 0 and target_Alive:
            self.kills+=1
            self.total_Dragons_Alive-=1
            print(self.name + " kills: ", self.kills);
            print(self.name + " health ", self.health);
            print(target.name + " health: ", target.health);
            print(self.getTotalDragonsAlive());
            
        
        
        
        
cadigan = Dragon("Cadigan", "Green", 10.3, True)
amelia =  Dragon("Amelia", "Green", 8.5, False)
for x in range(0, 12):
    cadigan.attack(amelia)




    
    


