class SpaceAge:
    def __init__(self, seconds):
        self.seconds=seconds
      
    
    def on_earth(self):
        oed=1
        s=self.seconds/(31557600*oed)
        return round(s,2)
    
    def on_mercury(self):
        oed=0.2408467
        s=self.seconds/(31557600*oed)
        return round(s,2)
    
    def on_venus(self):
        oed= 0.61519726
        s=self.seconds/(31557600*oed)
        return round(s,2)
    
    def on_mars(self):
        oed= 1.8808158 
        s=self.seconds/(31557600*oed)
        return round(s,2)
    
    def on_jupiter(self):
        oed= 11.862615
        s=self.seconds/(31557600*oed)
        return round(s,2)
    
    def on_saturn(self):
        oed= 29.447498
        s=self.seconds/(31557600*oed)
        return round(s,2)
    
    def on_uranus(self):
        oed= 84.016846 
        s=self.seconds/(31557600*oed)
        return round(s,2)
    
    def on_neptune(self):
        oed= 164.79132
        s=self.seconds/(31557600*oed)
        return round(s,2)
    

    
   
        pass

print(SpaceAge(901876382).on_jupiter())