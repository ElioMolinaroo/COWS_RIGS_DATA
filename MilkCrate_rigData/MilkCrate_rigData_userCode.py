# Connect the wheels
wheel_move_local = api.Attribute(api.Node("body_M_ctrl", create=False), "dagLocalMatrix")
wheel_move_local.connect_to(f"wheel_LF_inputs.wheelLocal_mtx")
wheel_move_local.connect_to(f"wheel_RF_inputs.wheelLocal_mtx")
wheel_move_local.connect_to(f"wheel_LBa_inputs.wheelLocal_mtx")
wheel_move_local.connect_to(f"wheel_RBa_inputs.wheelLocal_mtx")

trap_ctrl = api.Node("trap_M_ctrl", create=False)
api.Attribute(trap_ctrl, "translate").locked = True
api.Attribute(trap_ctrl, "rotateY").locked = True
api.Attribute(trap_ctrl, "rotateZ").locked = True
api.Attribute(trap_ctrl, "scale").locked = True
api.Attribute(trap_ctrl, f"minRotYLimitEnable").set_value(True)
api.Attribute(trap_ctrl, f"minRotYLimit").set_value(-263)
api.Attribute(trap_ctrl, f"maxRotYLimitEnable").set_value(True)
api.Attribute(trap_ctrl, f"maxRotYLimit").set_value(0)