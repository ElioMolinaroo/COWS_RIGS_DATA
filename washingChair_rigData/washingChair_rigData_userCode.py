# Connect the wheel
api.Attribute(api.Node("body_M_ctrl", create=False), "dagLocalMatrix").connect_to(f"wheel_M_inputs.wheelLocal_mtx")