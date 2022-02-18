import pymel.core as pm
import pymel.core.datatypes as dt
import ctrls 


class Leg_Rig: 
    '''
    Rita Rigs
    7-26-2021

    Meant to be run after placers are in position
    Constructs rig idioms around the placers
    '''

    def __init__(self):
        #reference placements: either assessing the height of the model and placing reference proportionally
        # or creating an prepositioned reference "skeleton" to then have the references placed by rigger.
        self.hip = pm.circle(nr=(0,0,1),n=("Hip_Ref_Loc"))[0]
        self.hip.translate.set(7,12,1)
        self.knee = pm.circle(nr=(0,0,1),n=("Knee_Ref_Loc"))[0]
        self.knee.translate.set(7,6,2)
        self.ankle = pm.circle(nr=(0,0,1),n=("Ankle_Ref_Loc"))[0]
        self.ankle.translate.set(7,1,1)
        #self.ball = pm.circle(nr=(0,0,1),n=("Ball_Ref_Loc"))[0]
        #self.ball.translate.set
        
    def joint_place(self, side, suffix):
        pm.select(cl=True)
        hip_jnt = pm.joint(p= self.hip.translate.get(), n=(side+"_Hip_"+ suffix))
        knee_jnt = pm.joint(p=self.knee.translate.get(),n=(side+"_Knee_"+ suffix))
        ankle_jnt = pm.joint(p=self.ankle.translate.get(),n=(side+"_Ankle_"+ suffix))

        return [hip_jnt, knee_jnt, ankle_jnt]


    def pv_build(self):
        hip_vec= dt.Vector(self.hip.translate.get())
        ankle_vec= dt.Vector(self.ankle.translate.get())
        knee_vec= dt.Vector(self.knee.translate.get())
        thigh_vec= hip_vec-knee_vec
        thigh_vec.normalize()
        shin_vec= ankle_vec - knee_vec
        shin_vec.normalize()
        pv = (thigh_vec + shin_vec) *10
        pv_pos = knee_vec - pv
        self.pv_ctrl = pm.circle(nr=(0,0,1), n=("PV_Ctrl"))[0]
        self.pv_ctrl.translate.set(pv_pos)

        pm.delete(self.hip, self.knee, self.ankle)

    def create_ik(self, side):
        self.leg_ik = pm.ikHandle(sj=self.IK_jnt_list[0] , ee=self.IK_jnt_list[2] , n=(side+"_Leg_IK"))[0]
        self.leg_pv = pm.poleVectorConstraint(self.pv_ctrl, self.leg_ik)

    def stretch_ik(self, side):
        #create nodes: distanceDim, decomposeMatrix, top and bottom nulls, multiply/divide, condition
        #assign attributes: extend IK to max length. Input this value in input 2X of multiply/divide
        #connect nodes:  Convert WorldSpace Matrix to Euler (decompose) 
        # then input start and end points into distanceDim. connect to multiply/divide input 1X 
        # function "greater than". connect output 1R to condition TRUE
        pass

    def build_all(self):
        self.SK_jnt_list= self.joint_place('L','SKjnt')
        self.FK_jnt_list= self.joint_place('L','FKjnt')
        self.IK_jnt_list= self.joint_place('L','IKjnt')
        self.pv_build()
        self.create_ik('L')
        



    
        
        