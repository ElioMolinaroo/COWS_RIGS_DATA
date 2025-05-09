user_code_nodes = []

# Finalise the components blends
blends_data = [
    {
        "blend_attr": api.Attribute(api.Node("arm_L_blend_inputs", create=False), "FK_IK_blend"),
        "cmpt01_controls": (
            api.DagNode("armFK_L001_ctrl", create=False),
            api.DagNode("armFK_L002_ctrl", create=False),
            api.DagNode("armFK_L003_ctrl", create=False),
        ),
        "cmpt02_controls": (
            api.DagNode("armIK_L_end_ctrl", create=False),
            api.DagNode("armIK_L_poleVector_ctrl", create=False),
        ),
    },
    {
        "blend_attr": api.Attribute(api.Node("arm_R_blend_inputs", create=False), "FK_IK_blend"),
        "cmpt01_controls": (
            api.DagNode("armFK_R001_ctrl", create=False),
            api.DagNode("armFK_R002_ctrl", create=False),
            api.DagNode("armFK_R003_ctrl", create=False),
        ),
        "cmpt02_controls": (
            api.DagNode("armIK_R_end_ctrl", create=False),
            api.DagNode("armIK_R_poleVector_ctrl", create=False),
        ),
    }
]
for data in blends_data:
    # Finalise the blends on all
    rev_node = utilities.rig_utils.finalise_components_blend(data["blend_attr"], data["cmpt01_controls"], data["cmpt02_controls"])
    user_code_nodes.append(rev_node)


# LOCK ATTRIBUTES ---------------------------------------------------------------
for side in ("L", "R"):
    api.Attribute(api.Node(f"armFK_{side}001_ctrl", create=False), "translate").locked = True
    api.Attribute(api.Node(f"armFK_{side}001_ctrl", create=False), "rotateX").locked = True
    api.Attribute(api.Node(f"armFK_{side}001_ctrl", create=False), "rotateY").locked = True
    api.Attribute(api.Node(f"armFK_{side}001_ctrl", create=False), "scale").locked = True
    api.Attribute(api.Node(f"armFK_{side}002_ctrl", create=False), "translate").locked = True
    api.Attribute(api.Node(f"armFK_{side}002_ctrl", create=False), "rotateX").locked = True
    api.Attribute(api.Node(f"armFK_{side}002_ctrl", create=False), "rotateY").locked = True
    api.Attribute(api.Node(f"armFK_{side}002_ctrl", create=False), "scale").locked = True
    api.Attribute(api.Node(f"armFK_{side}003_ctrl", create=False), "translate").locked = True
    api.Attribute(api.Node(f"armFK_{side}003_ctrl", create=False), "rotateY").locked = True
    api.Attribute(api.Node(f"armFK_{side}003_ctrl", create=False), "rotateZ").locked = True
    api.Attribute(api.Node(f"armFK_{side}003_ctrl", create=False), "scale").locked = True

    api.Attribute(api.Node(f"armIK_{side}_end_ctrl", create=False), "translateZ").locked = True
    api.Attribute(api.Node(f"armIK_{side}_end_ctrl", create=False), "rotate").locked = True
    api.Attribute(api.Node(f"armIK_{side}_end_ctrl", create=False), "scale").locked = True
    api.Attribute(api.Node(f"armIK_{side}_poleVector_ctrl", create=False), "translate").locked = True
    api.Attribute(api.Node(f"armIK_{side}_poleVector_ctrl", create=False), "rotate").locked = True
    api.Attribute(api.Node(f"armIK_{side}_poleVector_ctrl", create=False), "scale").locked = True


# Hinges
hinge_attr = api.Attribute(api.Node("body_M_ctrl", create=False), "hinges", attr_type="angle", keyable=True, create=True)
hinge_attr.min = math.radians(-120)
hinge_attr.max = math.radians(35)
for i in range(22):
    hinge_attr.connect_to(f"hinge_{str(i+1).zfill(3)}_jnt.rotateZ")


cmds.container("Baron_RIG", edit=True, addNode=[i.name for i in user_code_nodes])