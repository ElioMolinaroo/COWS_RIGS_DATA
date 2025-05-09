user_code_nodes = []


# Connect the wheels
wheel_move_local = api.Attribute(api.Node("wheelMove_M_ctrl", create=False), "dagLocalMatrix")
wheel_move_local.connect_to(f"wheel_M_inputs.wheelLocal_mtx")
wheel_move_local.connect_to(f"outWheel_L_inputs.wheelLocal_mtx")
wheel_move_local.connect_to(f"outWheel_R_inputs.wheelLocal_mtx")


# Finalise the components blends
blends_data = [
    {
        "blend_attr": api.Attribute(api.Node("coreMechBlend_M_inputs", create=False), "FK_IK_blend"),
        "cmpt01_controls": (
            api.DagNode("coreMechFK_M001_ctrl", create=False),
            api.DagNode("coreMechFK_M002_ctrl", create=False),
            api.DagNode("coreMechFK_M003_ctrl", create=False),
        ),
        "cmpt02_controls": (
            api.DagNode("coreMechIK_M_end_ctrl", create=False),
            api.DagNode("coreMechIK_M_poleVector_ctrl", create=False),
        ),
    },
    {
        "blend_attr": api.Attribute(api.Node("armBlend_L_inputs", create=False), "FK_IK_blend"),
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
        "blend_attr": api.Attribute(api.Node("armBlend_R_inputs", create=False), "FK_IK_blend"),
        "cmpt01_controls": (
            api.DagNode("armFK_R001_ctrl", create=False),
            api.DagNode("armFK_R002_ctrl", create=False),
            api.DagNode("armFK_R003_ctrl", create=False),
        ),
        "cmpt02_controls": (
            api.DagNode("armIK_R_end_ctrl", create=False),
            api.DagNode("armIK_R_poleVector_ctrl", create=False),
        ),
    },
]
for data in blends_data:
    # Finalise the blends on all
    rev_node = utilities.rig_utils.finalise_components_blend(data["blend_attr"], data["cmpt01_controls"], data["cmpt02_controls"])
    user_code_nodes.append(rev_node)


# Lock and limit controls ---------------------------------------------------------

# Wheel
api.Attribute(api.Node("wheelMove_M_ctrl", create=False), "scale").locked = True
for wheel_ctrl in (api.Node("wheel_M_ctrl", create=False), api.Node("outWheel_L_ctrl", create=False), api.Node("outWheel_R_ctrl", create=False), api.Node("wheelStopper_M001_ctrl", create=False), api.Node("wheelStopper_M002_ctrl", create=False)):
    api.Attribute(wheel_ctrl, "translate").locked = True
    api.Attribute(wheel_ctrl, "rotateX").locked = True
    api.Attribute(wheel_ctrl, "rotateY").locked = True
    api.Attribute(wheel_ctrl, "scale").locked = True


# Core Mech
for wheel_ctrl in (api.Node("coreMechFK_M001_ctrl", create=False), api.Node("coreMechFK_M002_ctrl", create=False)):
    api.Attribute(wheel_ctrl, "translate").locked = True
    api.Attribute(wheel_ctrl, "rotateX").locked = True
    api.Attribute(wheel_ctrl, "rotateY").locked = True
    api.Attribute(wheel_ctrl, "scale").locked = True

api.Attribute(api.Node("coreMechFK_M003_ctrl", create=False), "translateY").locked = True
api.Attribute(api.Node("coreMechFK_M003_ctrl", create=False), "translateZ").locked = True
api.Attribute(api.Node("coreMechFK_M003_ctrl", create=False), "rotate").locked = True
api.Attribute(api.Node("coreMechFK_M003_ctrl", create=False), "scale").locked = True
api.Attribute(api.Node("coreMechFK_M003_ctrl", create=False), f"minTransXLimitEnable").set_value(True)
api.Attribute(api.Node("coreMechFK_M003_ctrl", create=False), f"minTransXLimit").set_value(0)
api.Attribute(api.Node("coreMechFK_M003_ctrl", create=False), f"maxTransXLimitEnable").set_value(True)
api.Attribute(api.Node("coreMechFK_M003_ctrl", create=False), f"maxTransXLimit").set_value(2)

api.Attribute(api.Node("coreMechIK_M_poleVector_ctrl", create=False), "translate").locked = True
api.Attribute(api.Node("coreMechIK_M_poleVector_ctrl", create=False), "rotate").locked = True
api.Attribute(api.Node("coreMechIK_M_poleVector_ctrl", create=False), "scale").locked = True


# Neck & Head
api.Attribute(api.Node("neckHead_M001_ctrl", create=False), "translate").locked = True
api.Attribute(api.Node("neckHead_M001_ctrl", create=False), "scale").locked = True
for axis in ("Y", "Z"):
    api.Attribute(api.Node("neckHead_M001_ctrl", create=False), f"minRot{axis}LimitEnable").set_value(True)
    api.Attribute(api.Node("neckHead_M001_ctrl", create=False), f"minRot{axis}Limit").set_value(-35)
    api.Attribute(api.Node("neckHead_M001_ctrl", create=False), f"maxRot{axis}LimitEnable").set_value(True)
    api.Attribute(api.Node("neckHead_M001_ctrl", create=False), f"maxRot{axis}Limit").set_value(35)

api.Attribute(api.Node("neckHead_M002_ctrl", create=False), "translate").locked = True
api.Attribute(api.Node("neckHead_M002_ctrl", create=False), "rotateX").locked = True
api.Attribute(api.Node("neckHead_M002_ctrl", create=False), "rotateZ").locked = True
api.Attribute(api.Node("neckHead_M002_ctrl", create=False), "scale").locked = True
api.Attribute(api.Node("neckHead_M002_ctrl", create=False), f"minRotYLimitEnable").set_value(True)
api.Attribute(api.Node("neckHead_M002_ctrl", create=False), f"minRotYLimit").set_value(-37.5)
api.Attribute(api.Node("neckHead_M002_ctrl", create=False), f"maxRotYLimitEnable").set_value(True)
api.Attribute(api.Node("neckHead_M002_ctrl", create=False), f"maxRotYLimit").set_value(43.5)

api.Attribute(api.Node("neckHead_M003_ctrl", create=False), "translate").locked = True
api.Attribute(api.Node("neckHead_M003_ctrl", create=False), "rotateX").locked = True
api.Attribute(api.Node("neckHead_M003_ctrl", create=False), "rotateZ").locked = True
api.Attribute(api.Node("neckHead_M003_ctrl", create=False), "scale").locked = True


# Arms and hands
unlock_shoulders_reverse = api.Node("Robot_unlockShoulders_reverse", "reverse")
user_code_nodes.append(unlock_shoulders_reverse)
unlock_shoulders_attr = api.Attribute(api.Node("master_M_root_ctrl", create=False), "unlockShoulders", attr_type="boolean", create=True, keyable=True)
unlock_shoulders_attr.connect_to(f"{unlock_shoulders_reverse}.inputX")
unlock_shoulders_reverse_attr = api.Attribute(unlock_shoulders_reverse, "outputX")
for side in ("L", "R"):
    for i in range(3):
        api.Attribute(api.Node(f"handIn_{side}00{i+1}_ctrl", create=False), "translate").locked = True
        api.Attribute(api.Node(f"handIn_{side}00{i+1}_ctrl", create=False), "rotateX").locked = True
        api.Attribute(api.Node(f"handIn_{side}00{i+1}_ctrl", create=False), "rotateY").locked = True
        api.Attribute(api.Node(f"handIn_{side}00{i+1}_ctrl", create=False), "scale").locked = True
        api.Attribute(api.Node(f"handOut_{side}00{i+1}_ctrl", create=False), "translate").locked = True
        api.Attribute(api.Node(f"handOut_{side}00{i+1}_ctrl", create=False), "rotateX").locked = True
        api.Attribute(api.Node(f"handOut_{side}00{i+1}_ctrl", create=False), "rotateY").locked = True
        api.Attribute(api.Node(f"handOut_{side}00{i+1}_ctrl", create=False), "scale").locked = True

    api.Attribute(api.Node(f"armIK_{side}_end_ctrl", create=False), "rotate").locked = True
    api.Attribute(api.Node(f"armIK_{side}_end_ctrl", create=False), "scale").locked = True

    unlock_shoulders_reverse_attr.connect_to(f"armIK_{side}_end_ctrl.minTransZLimitEnable")
    unlock_shoulders_reverse_attr.connect_to(f"armIK_{side}_end_ctrl.maxTransZLimitEnable")
    api.Attribute(api.Node(f"armIK_{side}_end_ctrl", create=False), f"minTransZLimit").set_value(0)
    api.Attribute(api.Node(f"armIK_{side}_end_ctrl", create=False), f"maxTransZLimit").set_value(0)
    unlock_shoulders_reverse_attr.connect_to(f"armIK_{side}_poleVector_ctrl.minTransXLimitEnable")
    unlock_shoulders_reverse_attr.connect_to(f"armIK_{side}_poleVector_ctrl.maxTransXLimitEnable")
    api.Attribute(api.Node(f"armIK_{side}_poleVector_ctrl", create=False), f"minTransXLimit").set_value(0)
    api.Attribute(api.Node(f"armIK_{side}_poleVector_ctrl", create=False), f"maxTransXLimit").set_value(0)
    unlock_shoulders_reverse_attr.connect_to(f"armFK_{side}001_ctrl.minRotYLimitEnable")
    unlock_shoulders_reverse_attr.connect_to(f"armFK_{side}001_ctrl.maxRotYLimitEnable")
    api.Attribute(api.Node(f"armFK_{side}001_ctrl", create=False), f"minRotYLimit").set_value(0)
    api.Attribute(api.Node(f"armFK_{side}001_ctrl", create=False), f"maxRotYLimit").set_value(0)
    unlock_shoulders_reverse_attr.connect_to(f"armFK_{side}001_ctrl.minRotXLimitEnable")
    unlock_shoulders_reverse_attr.connect_to(f"armFK_{side}001_ctrl.maxRotXLimitEnable")
    api.Attribute(api.Node(f"armFK_{side}001_ctrl", create=False), f"minRotXLimit").set_value(0)
    api.Attribute(api.Node(f"armFK_{side}001_ctrl", create=False), f"maxRotXLimit").set_value(0)

    api.Attribute(api.Node(f"armFK_{side}001_ctrl", create=False), "translate").locked = True
    api.Attribute(api.Node(f"armFK_{side}001_ctrl", create=False), "scale").locked = True

    api.Attribute(api.Node(f"armFK_{side}002_ctrl", create=False), "translate").locked = True
    api.Attribute(api.Node(f"armFK_{side}002_ctrl", create=False), "rotateX").locked = True
    api.Attribute(api.Node(f"armFK_{side}002_ctrl", create=False), "rotateY").locked = True
    api.Attribute(api.Node(f"armFK_{side}002_ctrl", create=False), "scale").locked = True
    api.Attribute(api.Node(f"armFK_{side}002_ctrl", create=False), f"minRotZLimitEnable").set_value(True)
    api.Attribute(api.Node(f"armFK_{side}002_ctrl", create=False), f"minRotZLimit").set_value(-111.5)
    api.Attribute(api.Node(f"armFK_{side}002_ctrl", create=False), f"maxRotZLimitEnable").set_value(True)
    api.Attribute(api.Node(f"armFK_{side}002_ctrl", create=False), f"maxRotZLimit").set_value(112)

    api.Attribute(api.Node(f"armFK_{side}003_ctrl", create=False), "translateY").locked = True
    api.Attribute(api.Node(f"armFK_{side}003_ctrl", create=False), "translateZ").locked = True
    api.Attribute(api.Node(f"armFK_{side}003_ctrl", create=False), "rotateY").locked = True
    api.Attribute(api.Node(f"armFK_{side}003_ctrl", create=False), "rotateZ").locked = True
    api.Attribute(api.Node(f"armFK_{side}003_ctrl", create=False), "scale").locked = True
    api.Attribute(api.Node(f"armFK_{side}003_ctrl", create=False), f"minTransXLimitEnable").set_value(True)
    api.Attribute(api.Node(f"armFK_{side}003_ctrl", create=False), f"minTransXLimit").set_value(-0.375)
    api.Attribute(api.Node(f"armFK_{side}003_ctrl", create=False), f"maxTransXLimitEnable").set_value(True)
    api.Attribute(api.Node(f"armFK_{side}003_ctrl", create=False), f"maxTransXLimit").set_value(0.3)
    
    api.Attribute(api.Node(f"armTweaks_{side}002_ctrl", create=False), "translate").locked = True
    api.Attribute(api.Node(f"armTweaks_{side}002_ctrl", create=False), "rotateX").locked = True
    api.Attribute(api.Node(f"armTweaks_{side}002_ctrl", create=False), "rotateY").locked = True
    api.Attribute(api.Node(f"armTweaks_{side}002_ctrl", create=False), "scale").locked = True
    for i in (f"armTweaks_{side}001_ctrl", f"armTweaks_{side}003_ctrl", f"armTweaks_{side}004_ctrl", f"armTweaks_{side}005_ctrl"):
        api.Attribute(api.Node(i, create=False), "translate").locked = True
        api.Attribute(api.Node(i, create=False), "rotateY").locked = True
        api.Attribute(api.Node(i, create=False), "rotateZ").locked = True
        api.Attribute(api.Node(i, create=False), "scale").locked = True

    # Set the min distance on the IK arms
    len_attr = api.Attribute(api.Node(f"armIK_{side}_start2EndClamped_len", create=False), "minR")
    len_attr.disconnect_in()
    len_attr.set_value(3.201)
    api.Node(f"armIK_{side}_lowEndBuffer_len", create=False).delete()

    # Connect the tweaks
    cmds.hide(f"armFK_{side}003_ctrl")
    blend_output = api.Node(f"armBlend_{side}_outputs", create=False)
    inverse = api.Node(f"armTweaks_{side}_inverseMtx", "inverseMatrix")
    api.Attribute(blend_output, "outputBlendMatrix001").connect_to(f"{inverse}.inputMatrix")
    mtx, dcm = utilities.rig_utils.mult_matrices(name=f"armTweaks_{side}_elbowLocal", matrix_attrs=(api.Attribute(blend_output, "outputBlendMatrix002"), api.Attribute(inverse, "outputMatrix")), to_srt=True)
    api.Attribute(dcm, "outputRotate").connect_to(f"armTweaks_{side}002_srtBuffer.rotate")
    user_code_nodes += [inverse, mtx, dcm]

# Core IK Modifications ---------------------------------------------------------
api.Attribute(api.Node("coreMechIK_M_end_ctrl", create=False), "translateZ").locked = True
api.Attribute(api.Node("coreMechIK_M_end_ctrl", create=False), "rotate").locked = True
api.Attribute(api.Node("coreMechIK_M_end_ctrl", create=False), "scale").locked = True

# Set the min distance on the core IK
len_attr = api.Attribute(api.Node("coreMechIK_M_start2EndClamped_len", create=False), "minR")
len_attr.disconnect_in()
len_attr.set_value(4.75)
api.Node("coreMechIK_M_lowEndBuffer_len", create=False).delete()

# Modify stretch
api.Attribute(api.Node("coreMechIK_M_end_ctrl", create=False), "stretch").set_value(1)
top_dist_stretch = api.Node("coreMechIK_M_topDistanceStretch_mult", create=False)
api.Attribute(top_dist_stretch, "output").disconnect_out()
top_dist_stretch.delete()
new_mult = api.Node("coreMechIK_M_stretchMult_modify", "multDoubleLinear")
new_pma = api.Node("coreMechIK_M_stretchSubtract_modify", "plusMinusAverage")
stretch_clamp = api.Node("coreMechIK_M_stretchClamp", create=False)
stretch_ratio = api.Node("coreMechIK_M_pop2stretch_ratio", create=False)
api.Attribute(stretch_clamp, "outColorR").connect_to(f"{new_mult}.input1")
api.Attribute(new_mult, "input2").set_value(2)
api.Attribute(new_pma, "operation").set_value(2)
cmds.connectAttr(f"{new_mult}.output", f"{new_pma}.input1D[0]")
cmds.setAttr(f"{new_pma}.input1D[1]", 1)
ratio_attr = api.Attribute(stretch_ratio, "input1")
ratio_attr.disconnect_in()
api.Attribute(new_pma, "output1D").connect_to(ratio_attr)
new_clamp = api.Node("coreMechIK_M_bottomRatio_clampMax", "clamp")
api.Attribute(new_clamp, "maxR").set_value(4.9)
cmds.connectAttr("coreMechIK_M_bottomDistanceStretch_mult.output", f"{new_clamp}.inputR")
cmds.connectAttr(f"{new_clamp}.outputR", "coreMechIK_M_bottomDistanceScale_mult.input1", force=True)
user_code_nodes += [new_mult, new_pma, new_clamp]

api.Attribute(api.Node("coreMechIK_M_end_ctrl", create=False), "popRemoval").delete()
api.Attribute(api.Node("coreMechIK_M_poleVector_ctrl", create=False), "visibility").set_value(False)

# Delete pop_removal and stretch on arms
api.Attribute(api.Node("armIK_L_end_ctrl", create=False), "popRemoval").delete()
api.Attribute(api.Node("armIK_R_end_ctrl", create=False), "popRemoval").delete()
api.Attribute(api.Node("armIK_L_end_ctrl", create=False), "stretch").delete()
api.Attribute(api.Node("armIK_R_end_ctrl", create=False), "stretch").delete()

# IK as default for arms and core
for ctrl_name in ("coreMechIK_M_end_ctrl", "armIK_L_end_ctrl", "armIK_R_end_ctrl"):
    api.Attribute(api.Node(ctrl_name, create=False), "FK_IK_blend").set_value(1)


# Auto neck rotation
auto_rot_attr = api.Attribute(api.Node("neckHead_M003_ctrl", create=False), long_name="auto_neck_rotation", attr_type="boolean", keyable=True, create=True)
auto_rot_attr.set_value(True)
auto_neck_bool = api.Node("autoNeckRotation_bool", "multDoubleLinear")
auto_rot_attr.connect_to(f"{auto_neck_bool}.input1")
api.Attribute(auto_neck_bool, "input2").set_value(-1)
local_rot_mtx, local_rot_dcm = utilities.rig_utils.mult_matrices(
    name="coreEnd2coreIKendRotation",
    matrix_attrs=(api.Attribute(api.Node("coreMechBlend_M_outputs", create=False), "outputBlendMatrix003"), api.Attribute(api.Node("coreMechIK_M_end_ctrl", create=False), "worldInverseMatrix", array=True, logical_index=0)),
    to_srt=True,
)
core_negate_angle = api.Node("coreEndNegate_angle", "multDoubleLinear")
api.Attribute(local_rot_dcm, "outputRotateZ").connect_to(f"{core_negate_angle}.input1")
api.Attribute(auto_neck_bool, "output").connect_to(f"{core_negate_angle}.input2")
clamp2limits = api.Node("neckHead_001_clamp2limits_angle", "clamp")
api.Attribute(clamp2limits, "minR").set_value(-35)
api.Attribute(clamp2limits, "maxR").set_value(35)
api.Attribute(core_negate_angle, "output").connect_to(f"{clamp2limits}.inputR")
remainder_angle = api.Node("neckHead_002_remainder_angle", "plusMinusAverage")
api.Attribute(remainder_angle, "operation").set_value(2)
api.Attribute(core_negate_angle, "output").connect_to(api.Attribute(remainder_angle, "input1D", array=True, logical_index=0))
api.Attribute(clamp2limits, "outputR").connect_to(api.Attribute(remainder_angle, "input1D", array=True, logical_index=1))
output001 = api.Node("neckHead_001_angleAdjust_rot2mtx", "composeMatrix")
api.Attribute(clamp2limits, "outputR").connect_to(f"{output001}.inputRotateY")
api.Attribute(output001, "outputMatrix").connect_to(f"neckHead_M001_ctrl.offsetParentMatrix")
output002 = api.Node("neckHead_002_angleAdjust_rot2mtx", "composeMatrix")
api.Attribute(remainder_angle, "output1D").connect_to(f"{output002}.inputRotateY")
api.Attribute(output002, "outputMatrix").connect_to(f"neckHead_M002_ctrl.offsetParentMatrix")
user_code_nodes += [auto_neck_bool, local_rot_mtx, local_rot_dcm, core_negate_angle, clamp2limits, remainder_angle, output001, output002]


# Gravity footprint
footprint_data = {
    "degree": 1,
    "control_points": [
        [-0.24600968664751985, -8.246546449181656e-18, 0.24600968664751985],
        [-0.7380290599425591, 3.298618579672662e-17, 0.24600968664751985],
        [-0.7380290599425591, 3.298618579672662e-17, -0.24600968664751985],
        [-0.24600968664751985, -8.246546449181656e-18, -0.24600968664751985],
        [-0.24600968664751985, -8.246546449181656e-18, -0.7380290599425591],
        [0.24600968664751985, 8.246546449181656e-18, -0.7380290599425591],
        [0.24600968664751985, 8.246546449181656e-18, -0.24600968664751985],
        [0.7380290599425591, -3.298618579672662e-17, -0.24600968664751985],
        [0.7380290599425591, -3.298618579672662e-17, 0.24600968664751985],
        [0.24600968664751985, 8.246546449181656e-18, 0.24600968664751985],
        [0.24600968664751985, 8.246546449181656e-18, 0.7380290599425591],
        [-0.24600968664751985, -8.246546449181656e-18, 0.7380290599425591],
        [-0.24600968664751985, -8.246546449181656e-18, 0.24600968664751985],
    ],
    "knot_vector": [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0],
    "form": 1,
    "parent": None,
    "colour": {"rgb": False, "index": 14, "colour": [0.0, 0.0, 0.0, 1.0]},
}
head2footprint_data = {"degree": 1, "control_points": [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]], "knot_vector": [0.0, 1.0], "form": 1, "parent": None, "colour": {"rgb": False, "index": 14, "colour": [0.0, 0.0, 0.0, 1.0]}}
gravity_footprint_attr = api.Attribute(api.Node("neckHead_M003_ctrl", create=False), long_name="show_gravity_footprint", attr_type="boolean", keyable=True, create=True)
gravity_footprint_attr.set_value(True)

i = 0
for data in (footprint_data, head2footprint_data):
    crv_data = core.nurbs.NurbsCurve.deserialise_curve(data)
    core.nurbs.NurbsCurve.create_curve_from_data(crv_data)
    crv = api.DagNode("curve1", create=False)
    crv.name = "gravity_footprint_crv" if i == 0 else "head2footprint_crv"
    api.Attribute(crv, "translate").locked = True
    api.Attribute(crv, "rotate").locked = True
    api.Attribute(crv, "scale").locked = True
    gravity_footprint_attr.connect_to(f"{crv}.visibility")
    api.Attribute(crv.shapes[0], "alwaysDrawOnTop").set_value(True)
    user_code_nodes.append(crv)
    i += 1

inverse_global = api.Node("master_M_globalOutput_inverseMtx", "inverseMatrix")
api.Attribute(api.Node("master_M_outputs", create=False), "globalOutput").connect_to(f"{inverse_global}.inputMatrix")
neck003_local_mtx, neck003_local_dcm = utilities.rig_utils.mult_matrices(
    name="neckHead_003_local", matrix_attrs=(api.Attribute(api.Node("neckHead_M_outputs", create=False), "outputMatrix003"), api.Attribute(inverse_global, "outputMatrix")), to_srt=True
)
ground_proj_mtx = api.Node("neckHead_003_groundProjection_mtx", "composeMatrix")
api.Attribute(neck003_local_dcm, "outputTranslateX").connect_to(f"{ground_proj_mtx}.inputTranslateX")
api.Attribute(neck003_local_dcm, "outputTranslateZ").connect_to(f"{ground_proj_mtx}.inputTranslateZ")
proj2global_mtx, proj2global_dcm = utilities.rig_utils.mult_matrices(
    name="groundProjection2globalOutput", matrix_attrs=(api.Attribute(ground_proj_mtx, "outputMatrix"), api.Attribute(api.Node("master_M_outputs", create=False), "globalOutput")), to_srt=True
)
api.Attribute(proj2global_mtx, "matrixSum").connect_to("gravity_footprint_crv.offsetParentMatrix")
neck003_dcm = api.Node("neckHead_003_mtx2srt", "decomposeMatrix")
api.Attribute(api.Node("neckHead_M_outputs", create=False), "outputMatrix003").connect_to(f"{neck003_dcm}.inputMatrix")
head2footprint_crv = api.DagNode("head2footprint_crv", create=False)
api.Attribute(neck003_dcm, "outputTranslate").connect_to(api.Attribute(head2footprint_crv.shapes[0], "controlPoints", array=True, logical_index=0))
api.Attribute(proj2global_dcm, "outputTranslate").connect_to(api.Attribute(head2footprint_crv.shapes[0], "controlPoints", array=True, logical_index=1))
user_code_nodes += [inverse_global, neck003_local_mtx, neck003_local_dcm, ground_proj_mtx, proj2global_mtx, proj2global_dcm, neck003_dcm]


# Spring
spring_end = api.Node("core2springEnd_mtx", "multMatrix")
api.Attribute(spring_end, "matrixIn", array=True, logical_index=0).set_value(om2.MMatrix((1, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 2.283, -0.648, 0, 1)))
api.Attribute(api.Node("coreMechBlend_M_outputs", create=False), "outputBlendMatrix002").connect_to(api.Attribute(spring_end, "matrixIn", array=True, logical_index=1))
for i in ("translate", "rotate", "scale"):
    attr = api.Attribute(api.Node("springHolder_M_end_srtBuffer", create=False), i)
    attr.disconnect_in()
api.DagNode("springHolder_M_end_srtBuffer", create=False).set_matrix_to_identity()
api.Attribute(spring_end, "matrixSum").connect_to("springHolder_M_end_srtBuffer.offsetParentMatrix")
cmds.delete("springHolder_M_endBuffer_mtx", "springHolder_M_endBuffer_mtx2srt")
api.Attribute(api.Node("springHolder_M_end_ctrl", create=False), "stretch").set_value(1)
cmds.hide("springHolder_M_end_ctrl", "springHolder_M_root_ctrl", "suspensionSpringCompressed_M_geo")

distance_comp = api.Node(f"springHolder_end2root_distance", "distanceBetween")
distance2weight = api.Node(f"springHolder_end2root_distance2weight_rmp", "remapValue")
api.Attribute(distance_comp, "distance").connect_to(f"{distance2weight}.inputValue")
api.Attribute(distance2weight, "inputMin").set_value(4.267)
api.Attribute(distance2weight, "inputMax").set_value(1.023)

for attr, name in zip([api.Attribute(api.Node("springHolder_M_outputs", create=False), "rootOutputMatrix"), api.Attribute(api.Node("springHolder_M_outputs", create=False), "endOutputMatrix")], ["root", "end"]):
    mult = api.Node(f"springHolder_{name}ScaleCompensate_mtx", "multMatrix")
    inverse = api.Node(f"springHolder_{name}ScaleInverse_mtx", "inverseMatrix")
    pick = api.Node(f"springHolder_{name}Scale_mtx", "pickMatrix")
    api.Attribute(pick, "useTranslate").set_value(False)
    api.Attribute(pick, "useRotate").set_value(False)
    api.Attribute(pick, "useShear").set_value(False)
    user_code_nodes += [mult, inverse, pick]

    attr.connect_to(f"{pick}.inputMatrix")
    api.Attribute(pick, "outputMatrix").connect_to(f"{inverse}.inputMatrix")
    cmds.connectAttr(str(attr), f"{mult}.matrixIn[0]")
    cmds.connectAttr(f"{inverse}.outputMatrix", f"{mult}.matrixIn[1]")
    if name == "root":
        api.Attribute(mult, "matrixSum").connect_to(f"{distance_comp}.inMatrix1")
    else:
        api.Attribute(mult, "matrixSum").connect_to(f"{distance_comp}.inMatrix2")

spring_bs = cmds.blendShape("suspensionSpringCompressed_M_geo", "suspensionSpring_M_geo", name="springActivation_BS")[0]
cmds.connectAttr(f"{distance2weight}.outValue", f"{spring_bs}.suspensionSpringCompressed_M_geo")
user_code_nodes += [spring_end, distance_comp, distance2weight, api.Node(spring_bs, create=False)]


cmds.container("Robot_RIG", edit=True, addNode=[i.name for i in user_code_nodes])