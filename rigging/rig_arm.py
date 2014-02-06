import maya.cmds as cmds

shoulder = "shoulder_jnt"
elbow = "elbow_jnt"
wrist = "wrist_jnt"
palm = "palm_jnt"

loc_info = ([shoulder, [0, 14.311348, 0.0477619]], [elbow, [0, 8.52323, -2.195134]], [wrist,[0, 1.613664, -0.422523]], [palm, [0, 0.492216, 0.373344]])
                                                                                      
                                                                                      
for loc in loc_info:
    print loc
    locator = cmds.spaceLocator(n=loc[0], p=loc[1]) 
    print arm                                                                                     

#cmds.spaceLocator(p=(0,0,0))









'''
cmds.joint(n= shoulder, p=(0, 14.311348, 0.0477619))
cmds.joint(n = elbow, p=(0, 8.52323, -2.195134))
cmds.joint(shoulder, e=True, zso = True, oj = 'xyz', sao = 'yup')
cmds.joint(n=wrist, p=(0, 1.613664, -0.422523))
cmds.joint(elbow, e=True, zso = True, oj = 'xyz', sao = 'yup')
cmds.joint(n=palm, p=(0, 0.492216, 0.373344))
cmds.joint(wrist, e=True, zso = True, oj = 'xyz', sao = 'yup')
cmds.joint(n=finger, p=(0, -0.737759, 1.060683))
cmds.joint(palm, e=True, zso = True, oj = 'xyz', sao = 'yup')'''

#put names in a list
#have another list for locators
#loop through list of locators
#assign name to locator via index num

#joints, names, positions