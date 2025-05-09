# Lock control attributes
door_L_ctrl = api.Node("Plane_holdDoor_L_ctrl", create=False)
api.Attribute(door_L_ctrl, "translate").locked=True
api.Attribute(door_L_ctrl, "scale").locked=True
api.Attribute(door_L_ctrl, "rotateX").locked=True
api.Attribute(door_L_ctrl, "rotateY").locked=True

door_R_ctrl = api.Node("Plane_holdDoor_R_ctrl", create=False)
api.Attribute(door_R_ctrl, "translate").locked=True
api.Attribute(door_R_ctrl, "rotateX").locked=True
api.Attribute(door_R_ctrl, "rotateY").locked=True
api.Attribute(door_R_ctrl, "scale").locked=True

propeller_ctrl = api.Node("Plane_propeller_M_ctrl", create=False)
api.Attribute(propeller_ctrl, "translate").locked=True
api.Attribute(propeller_ctrl, "rotateY").locked=True
api.Attribute(propeller_ctrl, "rotateZ").locked=True
api.Attribute(propeller_ctrl, "scale").locked=True
api.Attribute(propeller_ctrl, "minRotXLimitEnable").set_value(True)
api.Attribute(propeller_ctrl, "minRotXLimit").set_value(0)

# Create auto rotation
auto_rotate = api.Attribute(propeller_ctrl, "autoRotate", attr_type="boolean", keyable=True, create=True)
auto_rotate.set_value(True)
speed = api.Attribute(propeller_ctrl, "speed", attr_type="double", keyable=True, create=True)
speed.set_value(100)
rotate_bool = api.Node("Plane_propeller_rotateMult", "multDoubleLinear")
rotate_speed = api.Node("Plane_propeller_speedMult", "multDoubleLinear")
auto_rotate_srt2mtx = api.Node("Plane_propeller_autoRotate_srt2mtx", "composeMatrix")
auto_rotate_mtx = api.Node("Plane_propeller_autoRotate_mtx", "multMatrix")

api.Attribute(api.Node("time1", create=False), "outTime").connect_to(f"{rotate_bool}.input1")
auto_rotate.connect_to(f"{rotate_bool}.input2")
api.Attribute(rotate_bool, "output").connect_to(f"{rotate_speed}.input1")
speed.connect_to(f"{rotate_speed}.input2")
api.Attribute(rotate_speed, "output").connect_to(f"{auto_rotate_srt2mtx}.inputRotateX")
cmds.connectAttr(f"{auto_rotate_srt2mtx}.outputMatrix", f"{auto_rotate_mtx}.matrixIn[0]")
cmds.connectAttr("Plane_propeller_M_inputs.componentPosition", f"{auto_rotate_mtx}.matrixIn[1]")

srt = api.Node("Plane_propeller_M_cmptPos_mtx2srt", create=False)
attr = api.Attribute(srt, "inputMatrix")
attr.disconnect_in()
api.Attribute(auto_rotate_mtx, "matrixSum").connect_to(attr)

conversion_node = api.Node("timeToUnitConversion1", create=False)
conversion_node.name = "Plane_propeller_time_angle2float"
nodes = [rotate_bool, rotate_speed, auto_rotate_srt2mtx, auto_rotate_mtx, conversion_node]
cmds.container("Plane_RIG", edit=True, addNode=[i.name for i in nodes])