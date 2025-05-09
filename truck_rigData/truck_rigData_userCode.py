# Connect the wheels
wheel_move_local = api.Attribute(api.Node("truck_body_M_ctrl", create=False), "dagLocalMatrix")
wheel_move_local.connect_to(f"wheel001_L_inputs.wheelLocal_mtx")
wheel_move_local.connect_to(f"wheel002_L_inputs.wheelLocal_mtx")
wheel_move_local.connect_to(f"wheel003_L_inputs.wheelLocal_mtx")
wheel_move_local.connect_to(f"wheel001_R_inputs.wheelLocal_mtx")
wheel_move_local.connect_to(f"wheel002_R_inputs.wheelLocal_mtx")
wheel_move_local.connect_to(f"wheel003_R_inputs.wheelLocal_mtx")