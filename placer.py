import pymel.core as pm
import constant as con
import pymel.core.datatypes as dt


class Placer:
    def __init__(self, color = "cyan", side= "center", size= 1.0, pos= dt.Vector(0,0,0), n= "placer"):
        self.color = con.colour_dict[color]
        self.side = con.side_dict[side]
        #visit later (left side, right side, front, back, top, bottom)
        self.size = size 
        #self.parent =
        #self.transform =
        self.shape = pm.sphere(po = 0, r = self.size )
        pm.xform(self.shape, ws= True, t= pos)
        