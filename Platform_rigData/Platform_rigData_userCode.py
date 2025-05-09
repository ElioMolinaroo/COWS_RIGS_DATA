keyLock_ctrl = api.Node("Platform_keyLock_M_ctrl", create=False)
api.Attribute(keyLock_ctrl, "translate").locked = True
api.Attribute(keyLock_ctrl, "rotateY").locked = True
api.Attribute(keyLock_ctrl, "rotateZ").locked = True
api.Attribute(keyLock_ctrl, "scale").locked = True

trapDoor_ctrl = api.Node("Platform_trapDoor_ctrl", create=False)
api.Attribute(trapDoor_ctrl, "translate").locked = True
api.Attribute(trapDoor_ctrl, "rotateX").locked = True
api.Attribute(trapDoor_ctrl, "rotateY").locked = True
api.Attribute(trapDoor_ctrl, "scale").locked = True
api.Attribute(trapDoor_ctrl, "minRotZLimitEnable").set_value(True)
api.Attribute(trapDoor_ctrl, "minRotZLimit").set_value(-155)
api.Attribute(trapDoor_ctrl, "maxRotZLimitEnable").set_value(True)
api.Attribute(trapDoor_ctrl, "maxRotZLimit").set_value(0)

ctrls = (
    api.Node("Platform_key001_L_ctrl", create=False), 
    api.Node("Platform_key002_L_ctrl", create=False), 
    api.Node("Platform_key003_L_ctrl", create=False), 
    api.Node("Platform_key004_L_ctrl", create=False), 
    api.Node("Platform_key005_L_ctrl", create=False), 
    api.Node("Platform_key006_L_ctrl", create=False), 
    api.Node("Platform_key007_L_ctrl", create=False), 
    api.Node("Platform_key008_L_ctrl", create=False), 
    api.Node("Platform_key009_L_ctrl", create=False),
    api.Node("Platform_key001_R_ctrl", create=False), 
    api.Node("Platform_key002_R_ctrl", create=False), 
    api.Node("Platform_key003_R_ctrl", create=False), 
    api.Node("Platform_key004_R_ctrl", create=False), 
    api.Node("Platform_key005_R_ctrl", create=False), 
    api.Node("Platform_key006_R_ctrl", create=False), 
    api.Node("Platform_key007_R_ctrl", create=False), 
    api.Node("Platform_key008_R_ctrl", create=False), 
    api.Node("Platform_key009_R_ctrl", create=False),
)

for ctrl in ctrls:
    api.Attribute(ctrl, "translateY").locked = True
    api.Attribute(ctrl, "translateZ").locked = True
    api.Attribute(ctrl, "rotate").locked = True
    #api.Attribute(ctrl, "scale").locked = True
    api.Attribute(ctrl, "maxTransXLimitEnable").set_value(True)
    api.Attribute(ctrl, "maxTransXLimit").set_value(0)
    api.Attribute(ctrl, "minTransXLimitEnable").set_value(True)
    api.Attribute(ctrl, "minTransXLimit").set_value(-0.07)