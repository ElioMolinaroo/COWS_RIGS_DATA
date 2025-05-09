master_ctrl = api.Node("master_M_root_ctrl", create=False)

# Create auto rotation
auto_rotate = api.Attribute(master_ctrl, "autoRotate", attr_type="boolean", keyable=True, create=True)
auto_rotate.set_value(True)
auto_rotate.default_value = True
speed = api.Attribute(master_ctrl, "speed", attr_type="double", keyable=True, create=True)
speed.set_value(300)
speed.default_value = 300
rotate_bool = api.Node("Grinder_bladesRotation_rotateMult", "multDoubleLinear")
rotate_speed = api.Node("Grinder_bladesRotation_speedMult", "multDoubleLinear")
auto_rotate_srt2mtx = api.Node("Grinder_bladesRotation_autoRotate_srt2mtx", "composeMatrix")

api.Attribute(api.Node("time1", create=False), "outTime").connect_to(f"{rotate_bool}.input1")
auto_rotate.connect_to(f"{rotate_bool}.input2")
api.Attribute(rotate_bool, "output").connect_to(f"{rotate_speed}.input1")
speed.connect_to(f"{rotate_speed}.input2")

for i in range(1, 7):
    api.Attribute(rotate_speed, "output").connect_to(f"blades{str(i).zfill(3)}_T_jnt.rotateX")
    api.Attribute(rotate_speed, "output").connect_to(f"blades{str(i).zfill(3)}_Bo_jnt.rotateX")

nodes = [rotate_bool, rotate_speed, auto_rotate_srt2mtx, api.Node("timeToUnitConversion1", create=False)]
cmds.container("Grinder_RIG", edit=True, addNode=[i.name for i in nodes])