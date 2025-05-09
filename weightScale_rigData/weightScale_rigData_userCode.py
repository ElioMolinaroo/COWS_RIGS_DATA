# Lock stuff
weight = api.Node("weight_M_ctrl", create=False)
api.Attribute(weight, "translate").locked = True
api.Attribute(weight, "scale").locked = True
api.Attribute(weight, f"minRotXLimitEnable").set_value(True)
api.Attribute(weight, f"minRotXLimit").set_value(-1.3)
api.Attribute(weight, f"maxRotXLimitEnable").set_value(True)
api.Attribute(weight, f"maxRotXLimit").set_value(1.3)
api.Attribute(weight, f"minRotZLimitEnable").set_value(True)
api.Attribute(weight, f"minRotZLimit").set_value(-1.3)
api.Attribute(weight, f"maxRotZLimitEnable").set_value(True)
api.Attribute(weight, f"maxRotZLimit").set_value(1.3)

neck_clamp = api.Node("neckClamp_M004_ctrl", create=False)
api.Attribute(neck_clamp, "translate").locked = True
api.Attribute(neck_clamp, "rotateX").locked = True
api.Attribute(neck_clamp, "rotateZ").locked = True
api.Attribute(neck_clamp, "scale").locked = True
api.Attribute(neck_clamp, f"minRotYLimitEnable").set_value(True)
api.Attribute(neck_clamp, f"minRotYLimit").set_value(0.3)
api.Attribute(neck_clamp, f"maxRotYLimitEnable").set_value(True)
api.Attribute(neck_clamp, f"maxRotYLimit").set_value(-235)


leg_clampR11 = api.Node("legClamp_R001001_ctrl", create=False)
leg_clampR12 = api.Node("legClamp_R001002_ctrl", create=False)
leg_clampR13 = api.Node("legClamp_R001003_ctrl", create=False)
leg_clampR14 = api.Node("legClamp_R001004_ctrl", create=False)
leg_clampR15 = api.Node("legClamp_R001005_ctrl", create=False)
leg_clampR16 = api.Node("legClamp_R001006_ctrl", create=False)
leg_clampR17 = api.Node("legClamp_R001007_ctrl", create=False)
api.Attribute(leg_clampR11, "translateY").locked = True
api.Attribute(leg_clampR11, "translateZ").locked = True
api.Attribute(leg_clampR11, "rotateY").locked = True
api.Attribute(leg_clampR11, "rotateZ").locked = True
api.Attribute(leg_clampR11, "scale").locked = True
api.Attribute(leg_clampR11, f"minTransXLimitEnable").set_value(True)
api.Attribute(leg_clampR11, f"minTransXLimit").set_value(0)
api.Attribute(leg_clampR11, f"maxTransXLimitEnable").set_value(True)
api.Attribute(leg_clampR11, f"maxTransXLimit").set_value(13)
api.Attribute(leg_clampR12, "translate").locked = True
api.Attribute(leg_clampR12, "rotateX").locked = True
api.Attribute(leg_clampR12, "rotateY").locked = True
api.Attribute(leg_clampR12, "scale").locked = True
api.Attribute(leg_clampR13, "translate").locked = True
api.Attribute(leg_clampR13, "rotateX").locked = True
api.Attribute(leg_clampR13, "rotateY").locked = True
api.Attribute(leg_clampR13, "scale").locked = True
api.Attribute(leg_clampR14, "translate").locked = True
api.Attribute(leg_clampR14, "rotateX").locked = True
api.Attribute(leg_clampR14, "rotateY").locked = True
api.Attribute(leg_clampR14, "scale").locked = True
api.Attribute(leg_clampR15, "translate").locked = True
api.Attribute(leg_clampR15, "rotateX").locked = True
api.Attribute(leg_clampR15, "rotateY").locked = True
api.Attribute(leg_clampR15, "scale").locked = True
api.Attribute(leg_clampR16, "translate").locked = True
api.Attribute(leg_clampR16, "scale").locked = True
api.Attribute(leg_clampR17, "translate").locked = True
api.Attribute(leg_clampR17, "rotateX").locked = True
api.Attribute(leg_clampR17, "rotateZ").locked = True
api.Attribute(leg_clampR17, "scale").locked = True
api.Attribute(leg_clampR17, f"minRotYLimitEnable").set_value(True)
api.Attribute(leg_clampR17, f"minRotYLimit").set_value(-5)
api.Attribute(leg_clampR17, f"maxRotYLimitEnable").set_value(True)
api.Attribute(leg_clampR17, f"maxRotYLimit").set_value(30)

leg_clampR21 = api.Node("legClamp_R002001_ctrl", create=False)
leg_clampR22 = api.Node("legClamp_R002002_ctrl", create=False)
leg_clampR23 = api.Node("legClamp_R002003_ctrl", create=False)
leg_clampR24 = api.Node("legClamp_R002004_ctrl", create=False)
leg_clampR25 = api.Node("legClamp_R002005_ctrl", create=False)
leg_clampR26 = api.Node("legClamp_R002006_ctrl", create=False)
leg_clampR27 = api.Node("legClamp_R002007_ctrl", create=False)
api.Attribute(leg_clampR21, "translateY").locked = True
api.Attribute(leg_clampR21, "translateZ").locked = True
api.Attribute(leg_clampR21, "rotateY").locked = True
api.Attribute(leg_clampR21, "rotateZ").locked = True
api.Attribute(leg_clampR21, "scale").locked = True
api.Attribute(leg_clampR21, f"minTransXLimitEnable").set_value(True)
api.Attribute(leg_clampR21, f"minTransXLimit").set_value(0)
api.Attribute(leg_clampR21, f"maxTransXLimitEnable").set_value(True)
api.Attribute(leg_clampR21, f"maxTransXLimit").set_value(13)
api.Attribute(leg_clampR22, "translate").locked = True
api.Attribute(leg_clampR22, "rotateX").locked = True
api.Attribute(leg_clampR22, "rotateY").locked = True
api.Attribute(leg_clampR22, "scale").locked = True
api.Attribute(leg_clampR23, "translate").locked = True
api.Attribute(leg_clampR23, "rotateX").locked = True
api.Attribute(leg_clampR23, "rotateY").locked = True
api.Attribute(leg_clampR23, "scale").locked = True
api.Attribute(leg_clampR24, "translate").locked = True
api.Attribute(leg_clampR24, "rotateX").locked = True
api.Attribute(leg_clampR24, "rotateY").locked = True
api.Attribute(leg_clampR24, "scale").locked = True
api.Attribute(leg_clampR25, "translate").locked = True
api.Attribute(leg_clampR25, "rotateX").locked = True
api.Attribute(leg_clampR25, "rotateY").locked = True
api.Attribute(leg_clampR25, "scale").locked = True
api.Attribute(leg_clampR26, "translate").locked = True
api.Attribute(leg_clampR26, "scale").locked = True
api.Attribute(leg_clampR27, "translate").locked = True
api.Attribute(leg_clampR27, "rotateX").locked = True
api.Attribute(leg_clampR27, "rotateZ").locked = True
api.Attribute(leg_clampR27, "scale").locked = True
api.Attribute(leg_clampR27, f"minRotYLimitEnable").set_value(True)
api.Attribute(leg_clampR27, f"minRotYLimit").set_value(-5)
api.Attribute(leg_clampR27, f"maxRotYLimitEnable").set_value(True)
api.Attribute(leg_clampR27, f"maxRotYLimit").set_value(30)

leg_clampL11 = api.Node("legClamp_L001001_ctrl", create=False)
leg_clampL12 = api.Node("legClamp_L001002_ctrl", create=False)
leg_clampL13 = api.Node("legClamp_L001003_ctrl", create=False)
leg_clampL14 = api.Node("legClamp_L001004_ctrl", create=False)
leg_clampL15 = api.Node("legClamp_L001005_ctrl", create=False)
leg_clampL16 = api.Node("legClamp_L001006_ctrl", create=False)
leg_clampL17 = api.Node("legClamp_L001007_ctrl", create=False)
api.Attribute(leg_clampL11, "translateY").locked = True
api.Attribute(leg_clampL11, "translateZ").locked = True
api.Attribute(leg_clampL11, "rotateY").locked = True
api.Attribute(leg_clampL11, "rotateZ").locked = True
api.Attribute(leg_clampL11, "scale").locked = True
api.Attribute(leg_clampL11, f"minTransXLimitEnable").set_value(True)
api.Attribute(leg_clampL11, f"minTransXLimit").set_value(0)
api.Attribute(leg_clampL11, f"maxTransXLimitEnable").set_value(True)
api.Attribute(leg_clampL11, f"maxTransXLimit").set_value(13)
api.Attribute(leg_clampL12, "translate").locked = True
api.Attribute(leg_clampL12, "rotateX").locked = True
api.Attribute(leg_clampL12, "rotateY").locked = True
api.Attribute(leg_clampL12, "scale").locked = True
api.Attribute(leg_clampL13, "translate").locked = True
api.Attribute(leg_clampL13, "rotateX").locked = True
api.Attribute(leg_clampL13, "rotateY").locked = True
api.Attribute(leg_clampL13, "scale").locked = True
api.Attribute(leg_clampL14, "translate").locked = True
api.Attribute(leg_clampL14, "rotateX").locked = True
api.Attribute(leg_clampL14, "rotateY").locked = True
api.Attribute(leg_clampL14, "scale").locked = True
api.Attribute(leg_clampL15, "translate").locked = True
api.Attribute(leg_clampL15, "rotateX").locked = True
api.Attribute(leg_clampL15, "rotateY").locked = True
api.Attribute(leg_clampL15, "scale").locked = True
api.Attribute(leg_clampL16, "translate").locked = True
api.Attribute(leg_clampL16, "scale").locked = True
api.Attribute(leg_clampL17, "translate").locked = True
api.Attribute(leg_clampL17, "rotateX").locked = True
api.Attribute(leg_clampL17, "rotateZ").locked = True
api.Attribute(leg_clampL17, "scale").locked = True
api.Attribute(leg_clampL17, f"minRotYLimitEnable").set_value(True)
api.Attribute(leg_clampL17, f"minRotYLimit").set_value(-30)
api.Attribute(leg_clampL17, f"maxRotYLimitEnable").set_value(True)
api.Attribute(leg_clampL17, f"maxRotYLimit").set_value(5)

leg_clampL21 = api.Node("legClamp_L002001_ctrl", create=False)
leg_clampL22 = api.Node("legClamp_L002002_ctrl", create=False)
leg_clampL23 = api.Node("legClamp_L002003_ctrl", create=False)
leg_clampL24 = api.Node("legClamp_L002004_ctrl", create=False)
leg_clampL25 = api.Node("legClamp_L002005_ctrl", create=False)
leg_clampL26 = api.Node("legClamp_L002006_ctrl", create=False)
leg_clampL27 = api.Node("legClamp_L002007_ctrl", create=False)
api.Attribute(leg_clampL21, "translateY").locked = True
api.Attribute(leg_clampL21, "translateZ").locked = True
api.Attribute(leg_clampL21, "rotateY").locked = True
api.Attribute(leg_clampL21, "rotateZ").locked = True
api.Attribute(leg_clampL21, "scale").locked = True
api.Attribute(leg_clampL21, f"minTransXLimitEnable").set_value(True)
api.Attribute(leg_clampL21, f"minTransXLimit").set_value(0)
api.Attribute(leg_clampL21, f"maxTransXLimitEnable").set_value(True)
api.Attribute(leg_clampL21, f"maxTransXLimit").set_value(13)
api.Attribute(leg_clampL22, "translate").locked = True
api.Attribute(leg_clampL22, "rotateX").locked = True
api.Attribute(leg_clampL22, "rotateY").locked = True
api.Attribute(leg_clampL22, "scale").locked = True
api.Attribute(leg_clampL23, "translate").locked = True
api.Attribute(leg_clampL23, "rotateX").locked = True
api.Attribute(leg_clampL23, "rotateY").locked = True
api.Attribute(leg_clampL23, "scale").locked = True
api.Attribute(leg_clampL24, "translate").locked = True
api.Attribute(leg_clampL24, "rotateX").locked = True
api.Attribute(leg_clampL24, "rotateY").locked = True
api.Attribute(leg_clampL24, "scale").locked = True
api.Attribute(leg_clampL25, "translate").locked = True
api.Attribute(leg_clampL25, "rotateX").locked = True
api.Attribute(leg_clampL25, "rotateY").locked = True
api.Attribute(leg_clampL25, "scale").locked = True
api.Attribute(leg_clampL26, "translate").locked = True
api.Attribute(leg_clampL26, "scale").locked = True
api.Attribute(leg_clampL27, "translate").locked = True
api.Attribute(leg_clampL27, "rotateX").locked = True
api.Attribute(leg_clampL27, "rotateZ").locked = True
api.Attribute(leg_clampL27, "scale").locked = True
api.Attribute(leg_clampL27, f"minRotYLimitEnable").set_value(True)
api.Attribute(leg_clampL27, f"minRotYLimit").set_value(-30)
api.Attribute(leg_clampL27, f"maxRotYLimitEnable").set_value(True)
api.Attribute(leg_clampL27, f"maxRotYLimit").set_value(5)