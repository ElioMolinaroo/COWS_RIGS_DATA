user_code_nodes = []


# Finalise the components blends
cmpt_01_ctrls = [api.DagNode(f"milkingTubeFK{str(i).zfill(3)}_ctrl", create=False) for i in range(1, 65)]
cmpt_02_ctrls = [api.DagNode(f"milkingTubeIK_tweak{str(i).zfill(3)}_ctrl", create=False) for i in range(1, 65)] + [api.DagNode(f"milkingTubeIK_IK{str(i).zfill(3)}_ctrl", create=False) for i in range(1, 9)] + [api.DagNode(f"milkingTubeIK_master_ctrl", create=False)]
rev_node = utilities.rig_utils.finalise_components_blend(api.Attribute(api.Node("milkingTubeBlend_inputs", create=False), "FK_IK_blend"), cmpt_01_ctrls, cmpt_02_ctrls)
user_code_nodes.append(rev_node)


cmds.container("MilkingTube_RIG", edit=True, addNode=[i.name for i in user_code_nodes])