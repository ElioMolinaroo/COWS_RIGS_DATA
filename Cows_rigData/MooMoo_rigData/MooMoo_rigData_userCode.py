user_code_nodes = []


# Finalise the components blends
blends_data = [
    {
        "blend_attr": api.Attribute(
            api.Node("MooMoo_spineBlend_M_inputs", create=False), "spineBlend"
        ),
        "cmpt01_controls": (
            api.DagNode("MooMoo_spineFK_M001_ctrl", create=False),
            api.DagNode("MooMoo_spineFK_M002_ctrl", create=False),
            api.DagNode("MooMoo_spineFK_M003_ctrl", create=False),
            api.DagNode("MooMoo_spineFK_M004_ctrl", create=False),
            api.DagNode("MooMoo_spineFK_M005_ctrl", create=False),
        ),
        "cmpt02_controls": (
            api.DagNode("MooMoo_spineIK_M_backCOG_ctrl", create=False),
            api.DagNode("MooMoo_spineIK_M_backIK_ctrl", create=False),
            api.DagNode("MooMoo_spineIK_M_midCOG_ctrl", create=False),
            api.DagNode("MooMoo_spineIK_M_midIK_ctrl", create=False),
            api.DagNode("MooMoo_spineIK_M_chestCOG_ctrl", create=False),
            api.DagNode("MooMoo_spineIK_M_chestIK_ctrl", create=False),
            api.DagNode("MooMoo_spineIK_M_tweak001_ctrl", create=False),
            api.DagNode("MooMoo_spineIK_M_tweak002_ctrl", create=False),
            api.DagNode("MooMoo_spineIK_M_tweak003_ctrl", create=False),
            api.DagNode("MooMoo_spineIK_M_tweak004_ctrl", create=False),
            api.DagNode("MooMoo_spineIK_M_tweak005_ctrl", create=False),
        ),
    },
    {
        "blend_attr": api.Attribute(
            api.Node("MooMoo_frontLegBlend_L_inputs", create=False), "FK_IK_blend"
        ),
        "cmpt01_controls": (
            api.DagNode("MooMoo_frontLegFK_L001_ctrl", create=False),
            api.DagNode("MooMoo_frontLegFK_L002_ctrl", create=False),
            api.DagNode("MooMoo_frontLegFK_L003_ctrl", create=False),
        ),
        "cmpt02_controls": (
            api.DagNode("MooMoo_frontLegIK_L_end_ctrl", create=False),
            api.DagNode("MooMoo_frontLegIK_L_poleVector_ctrl", create=False),
            api.DagNode("MooMoo_frontLegIK_L_root_ctrl", create=False)
        ),
    },
    {
        "blend_attr": api.Attribute(
            api.Node("MooMoo_frontLegBlend_R_inputs", create=False), "FK_IK_blend"
        ),
        "cmpt01_controls": (
            api.DagNode("MooMoo_frontLegFK_R001_ctrl", create=False),
            api.DagNode("MooMoo_frontLegFK_R002_ctrl", create=False),
            api.DagNode("MooMoo_frontLegFK_R003_ctrl", create=False),
        ),
        "cmpt02_controls": (
            api.DagNode("MooMoo_frontLegIK_R_end_ctrl", create=False),
            api.DagNode("MooMoo_frontLegIK_R_poleVector_ctrl", create=False),
            api.DagNode("MooMoo_frontLegIK_R_root_ctrl", create=False)
        ),
    },
    {
        "blend_attr": api.Attribute(
            api.Node("MooMoo_backLegBlend_L_inputs", create=False), "FK_IK_blend"
        ),
        "cmpt01_controls": (
            api.DagNode("MooMoo_backLegFK_L001_ctrl", create=False),
            api.DagNode("MooMoo_backLegFK_L002_ctrl", create=False),
            api.DagNode("MooMoo_backLegFK_L003_ctrl", create=False),
            api.DagNode("MooMoo_backLegFK_L004_ctrl", create=False),
        ),
        "cmpt02_controls": (
            api.DagNode("MooMoo_backLegIK_L_femurIK_end_ctrl", create=False),
            api.DagNode("MooMoo_backLegIK_L_femurIK_root_ctrl", create=False),
            api.DagNode("MooMoo_backLegIK_L_knee2ankleIK_end_ctrl", create=False),
            api.DagNode("MooMoo_backLegIK_L_knee2ankleIK_poleVector_ctrl", create=False),
            api.DagNode("MooMoo_backLegIK_L_master_ctrl", create=False),
            api.DagNode("MooMoo_backFootIK_L_ankleTweak_ctrl", create=False),
        ),
    },
    {
        "blend_attr": api.Attribute(
            api.Node("MooMoo_backLegBlend_R_inputs", create=False), "FK_IK_blend"
        ),
        "cmpt01_controls": (
            api.DagNode("MooMoo_backLegFK_R001_ctrl", create=False),
            api.DagNode("MooMoo_backLegFK_R002_ctrl", create=False),
            api.DagNode("MooMoo_backLegFK_R003_ctrl", create=False),
            api.DagNode("MooMoo_backLegFK_R004_ctrl", create=False),
        ),
        "cmpt02_controls": (
            api.DagNode("MooMoo_backLegIK_R_femurIK_end_ctrl", create=False),
            api.DagNode("MooMoo_backLegIK_R_femurIK_root_ctrl", create=False),
            api.DagNode("MooMoo_backLegIK_R_knee2ankleIK_end_ctrl", create=False),
            api.DagNode("MooMoo_backLegIK_R_knee2ankleIK_poleVector_ctrl", create=False),
            api.DagNode("MooMoo_backLegIK_R_master_ctrl", create=False),
            api.DagNode("MooMoo_backFootIK_R_ankleTweak_ctrl", create=False),
        ),
    },
]
for data in blends_data:
    # Finalise the blends on all
    rev_node = utilities.rig_utils.finalise_components_blend(data["blend_attr"], data["cmpt01_controls"], data["cmpt02_controls"])
    user_code_nodes.append(rev_node)

# Add the proxy attribute of the foot roll onto the controls
controls_map = [
    {
        "source_attrs": (
            api.Attribute(
                api.Node("MooMoo_backFootIK_L_inputs", create=False), "footRoll"
            ),
            api.Attribute(api.Node("MooMoo_backFootIK_L_inputs", create=False), "bank"),
            api.Attribute(
                api.Node("MooMoo_backFootIK_L_inputs", create=False), "heelTwist"
            ),
            api.Attribute(
                api.Node("MooMoo_backFootIK_L_inputs", create=False), "tipTwist"
            ),
            api.Attribute(
                api.Node("MooMoo_backFootIK_L_inputs", create=False),
                "tweaks_visibility",
            ),
        ),
        "target_ctrls": (
            api.Node("MooMoo_backLegIK_L_master_ctrl", create=False),
            api.Node("MooMoo_backLegIK_L_knee2ankleIK_end_ctrl", create=False),
            api.Node("MooMoo_backFootIK_L_ankleTweak_ctrl", create=False),
        ),
    },
    {
        "source_attrs": (
            api.Attribute(
                api.Node("MooMoo_backFootIK_R_inputs", create=False), "footRoll"
            ),
            api.Attribute(api.Node("MooMoo_backFootIK_R_inputs", create=False), "bank"),
            api.Attribute(
                api.Node("MooMoo_backFootIK_R_inputs", create=False), "heelTwist"
            ),
            api.Attribute(
                api.Node("MooMoo_backFootIK_R_inputs", create=False), "tipTwist"
            ),
            api.Attribute(
                api.Node("MooMoo_backFootIK_R_inputs", create=False),
                "tweaks_visibility",
            ),
        ),
        "target_ctrls": (
            api.Node("MooMoo_backLegIK_R_master_ctrl", create=False),
            api.Node("MooMoo_backLegIK_R_knee2ankleIK_end_ctrl", create=False),
            api.Node("MooMoo_backFootIK_R_ankleTweak_ctrl", create=False),
        ),
    },
    {
        "source_attrs": (
            api.Attribute(
                api.Node("MooMoo_frontFootIK_L_inputs", create=False), "footRoll"
            ),
            api.Attribute(
                api.Node("MooMoo_frontFootIK_L_inputs", create=False), "bank"
            ),
            api.Attribute(
                api.Node("MooMoo_frontFootIK_L_inputs", create=False), "heelTwist"
            ),
            api.Attribute(
                api.Node("MooMoo_frontFootIK_L_inputs", create=False), "tipTwist"
            ),
            api.Attribute(
                api.Node("MooMoo_frontFootIK_L_inputs", create=False),
                "tweaks_visibility",
            ),
        ),
        "target_ctrls": (
            api.Node("MooMoo_frontLegIK_L_end_ctrl", create=False),
            api.Node("MooMoo_frontFootIK_L_ankleTweak_ctrl", create=False),
        ),
    },
    {
        "source_attrs": (
            api.Attribute(
                api.Node("MooMoo_frontFootIK_R_inputs", create=False), "footRoll"
            ),
            api.Attribute(
                api.Node("MooMoo_frontFootIK_R_inputs", create=False), "bank"
            ),
            api.Attribute(
                api.Node("MooMoo_frontFootIK_R_inputs", create=False), "heelTwist"
            ),
            api.Attribute(
                api.Node("MooMoo_frontFootIK_R_inputs", create=False), "tipTwist"
            ),
            api.Attribute(
                api.Node("MooMoo_frontFootIK_R_inputs", create=False),
                "tweaks_visibility",
            ),
        ),
        "target_ctrls": (
            api.Node("MooMoo_frontLegIK_R_end_ctrl", create=False),
            api.Node("MooMoo_frontFootIK_R_ankleTweak_ctrl", create=False),
        ),
    },
]
for data in controls_map:
    for attr in data["source_attrs"]:
        for ctrl in data["target_ctrls"]:
            attr.create_proxy(ctrl)

# Connect the tweaks visibility of the foot roll to the leg tweaks
tweaks_attrs = [
                (api.Attribute(api.Node("MooMoo_frontLeg_topTwist_L_inputs", create=False), "tweaks_visibility"),
                api.Attribute(api.Node("MooMoo_frontLeg_bottomTwist_L_inputs", create=False), "tweaks_visibility")),

                (api.Attribute(api.Node("MooMoo_frontLeg_topTwist_R_inputs", create=False), "tweaks_visibility"),
                api.Attribute(api.Node("MooMoo_frontLeg_bottomTwist_R_inputs", create=False), "tweaks_visibility")),

                (api.Attribute(api.Node("MooMoo_backLeg_topTwist_L_inputs", create=False), "tweaks_visibility"),
                api.Attribute(api.Node("MooMoo_backLeg_midTwist_L_inputs", create=False), "tweaks_visibility"),
                api.Attribute(api.Node("MooMoo_backLeg_bottomTwist_L_inputs", create=False), "tweaks_visibility")),

                (api.Attribute(api.Node("MooMoo_backLeg_topTwist_R_inputs", create=False), "tweaks_visibility"),
                api.Attribute(api.Node("MooMoo_backLeg_midTwist_R_inputs", create=False), "tweaks_visibility"),
                api.Attribute(api.Node("MooMoo_backLeg_bottomTwist_R_inputs", create=False), "tweaks_visibility")),
]
controls = (
            api.DagNode("MooMoo_frontLegIK_L_end_ctrl", create=False),
            api.DagNode("MooMoo_frontLegIK_R_end_ctrl", create=False),
            api.DagNode("MooMoo_backLegIK_L_master_ctrl", create=False),
            api.DagNode("MooMoo_backLegIK_R_master_ctrl", create=False)
)
for ctrl, attrs in zip(controls, tweaks_attrs):
    for attr in attrs:
        api.Attribute(ctrl, "tweaks_visibility").connect_to(attr)

# Connect the neck tweaks visibility to the neck controls
tweaks_attr = api.Attribute(api.Node("MooMoo_neckTwist_M_inputs", create=False), "tweaks_visibility")
controls = (
            api.DagNode("MooMoo_neck_M001_ctrl", create=False),
            api.DagNode("MooMoo_neck_M002_ctrl", create=False),
            api.DagNode("MooMoo_head_M_ctrl", create=False)
)
for ctrl in controls:
    tweaks_attr.create_proxy(ctrl)


# Create the space switches
switches = (
    ("MooMoo_head_M_ctrl", ("MooMoo_neck_M002_ctrl", "MooMoo_global_M_offset001_ctrl")),
    (
        "MooMoo_frontLegIK_L_poleVector_ctrl",
        (
            "MooMoo_frontLegIK_L_end_ctrl",
            "MooMoo_frontLegIK_L_root_ctrl",
            "MooMoo_global_M_offset001_ctrl",
        ),
    ),
    (
        "MooMoo_frontLegIK_R_poleVector_ctrl",
        (
            "MooMoo_frontLegIK_R_end_ctrl",
            "MooMoo_frontLegIK_R_root_ctrl",
            "MooMoo_global_M_offset001_ctrl",
        ),
    ),
)
for data in switches:
    child = api.DagNode(data[0], create=False)
    parents = [api.DagNode(i, create=False) for i in data[1]]

    spaces_names = [
        i.name.removeprefix("MooMoo_").removesuffix("_ctrl") for i in parents
    ]
    nodes = walrus.connectors.space_switch(
        child=child, parents=parents, spaces_names=spaces_names, base_name="rigSwitch"
    )
    user_code_nodes += nodes


# Change the legs blends to default to IK
for i in (
    "MooMoo_frontLegFK_L001_ctrl",
    "MooMoo_frontLegFK_R001_ctrl",
    "MooMoo_backLegFK_L001_ctrl",
    "MooMoo_backLegFK_R001_ctrl",
):
    node = api.Node(i, create=False)
    api.Attribute(node, "FK_IK_blend").set_value(1)

# Change the spine blend to default to IK
node = api.Node("MooMoo_spineIK_M_midCOG_ctrl", create=False)
api.Attribute(node, "spineBlend").set_value(1)


# Bake the offset in the shoulder pivots
target = om2.MMatrix()
target.setElement(3, 2, 7.5)
api.Attribute(api.DagNode("MooMoo_shoulder_L_pivot_ctrl", create=False), "offsetParentMatrix").set_value(target)
api.Attribute(api.DagNode("MooMoo_shoulder_R_pivot_ctrl", create=False), "offsetParentMatrix").set_value(target)



# FACIAL -------------------------------------------------------------------------
# Import the facial rig scene
facial_path = "//storage/esma/3D4/cows/04_asset/01_character/MooMoo/maya/scenes/rig/publish/MooMoo_facial_rig_P.ma"
facial_nodes = cmds.file(facial_path, i=True, ignoreVersion=True, returnNewNodes=True)

# Create the blendshapes on all the meshes
original_facial_geos = (
                        api.Node("MooMoo_body_geo", create=False),
                        api.Node("MooMoo_mouthPiece_geo", create=False),                  
                        api.Node("MooMoo_tongue_geo", create=False),
                        api.Node("MooMoo_eyelid_TR_geo", create=False),                          
                        api.Node("MooMoo_eyelid_TL_geo", create=False),                         
                        api.Node("MooMoo_eyelid_BoL_geo", create=False),                 
                        api.Node("MooMoo_eyelid_BoR_geo", create=False),    
                        api.Node("MooMoo_eyeSclera_R_geo", create=False),  
                        api.Node("MooMoo_eyePupil_R_geo", create=False),
                        api.Node("MooMoo_eyeSclera_L_geo", create=False),
                        api.Node("MooMoo_eyePupil_L_geo", create=False),
                        api.Node("MooMoo_horn_L_geo", create=False),
                        api.Node("MooMoo_horn_R_geo", create=False),
)
for geo in original_facial_geos:
    if geo.name == "MooMoo_body_geo":
        # This is processed later with the correctives
        continue
    else:
        facial_geo = api.Node(geo.name.replace("_geo", "_facial_geo"), create=False)
    bs = cmds.blendShape(facial_geo.name, geo.name, topologyCheck=False, frontOfChain=True, weight=(0, 1), name=f"MooMoo_{facial_geo.name.removesuffix('_geo')}_BS")[0]
    facial_nodes.append(bs)

# Drive the facial controls with the head control
facial_vis_attr = api.Attribute(api.Node("MooMoo_head_M_ctrl", create=False), "facial_visibility", attr_type="boolean", keyable=True, create=True)
facial_vis_attr.connect_to(f"FACIAL_CTRLS.visibility")
facial_vis_attr.set_value(True)

bs_vis_attr = api.Attribute(api.Node("MooMoo_head_M_ctrl", create=False), "BS_ctrls_visibility", attr_type="boolean", keyable=True, create=True)
bs_vis_attr.connect_to(f"BS_CTRLS.visibility")

jnt_vis_attr = api.Attribute(api.Node("MooMoo_head_M_ctrl", create=False), "joints_ctrls_visibility", attr_type="boolean", keyable=True, create=True)
jnt_vis_attr.connect_to(f"JNT_CTRLS.visibility")

tweaks_vis_attr = api.Attribute(api.Node("MooMoo_head_M_ctrl", create=False), "head_lattice_visibility", attr_type="boolean", keyable=True, create=True)
tweaks_vis_attr.connect_to(f"MooMoo_facial_tweaks_controls_grp.visibility")

parent_cstrn = cmds.parentConstraint("MooMoo_head_M_ctrl", "FACIAL_CTRLS", maintainOffset=True)
scale_cstrn = cmds.scaleConstraint("MooMoo_head_M_ctrl", "FACIAL_CTRLS", maintainOffset=True)
facial_nodes == [parent_cstrn, scale_cstrn]

# Connect the visibility attribute on the eyes and tongue controls to the meshes
api.Attribute(api.Node("mouthMaster_M_BS_ctrl", create=False), "tongue_visibility").connect_to(f"MooMoo_tongue_geo.visibility")
api.Attribute(api.Node("eye_L_ctrl", create=False), "topEyelid_visibility").connect_to(f"MooMoo_eyelid_TL_geo.visibility")
api.Attribute(api.Node("eye_L_ctrl", create=False), "bottomEyelid_visibility").connect_to(f"MooMoo_eyelid_BoL_geo.visibility")
api.Attribute(api.Node("eye_R_ctrl", create=False), "topEyelid_visibility").connect_to(f"MooMoo_eyelid_TR_geo.visibility")
api.Attribute(api.Node("eye_R_ctrl", create=False), "bottomEyelid_visibility").connect_to(f"MooMoo_eyelid_BoR_geo.visibility")

# Cleanup
api.Attribute(api.Node("FACIAL_GEO", create=False), "visibility").set_value(False)
api.Attribute(api.Node("FACIAL_JNTS", create=False), "visibility").set_value(False)
api.Attribute(api.Node("FACIAL_DEFORMERS", create=False), "visibility").set_value(False)
cmds.container("MooMoo_RIG", edit=True, addNode=facial_nodes)


# Space switch on eyes control
data = ("eyesFollowMaster_M_ctrl", ("MooMoo_head_M_ctrl", "MooMoo_global_M_offset001_ctrl"))
child = api.DagNode(data[0], create=False)
parents = [api.DagNode(i, create=False) for i in data[1]]

spaces_names = [
    i.name.removeprefix("MooMoo_").removesuffix("_ctrl") for i in parents
]
nodes = walrus.connectors.space_switch(
    child=child, parents=parents, spaces_names=spaces_names, base_name="rigSwitch"
)
user_code_nodes += nodes


# GRAZE MODE ---------------------------------------------------------------
graze_attr = api.Attribute(api.Node("MooMoo_spineIK_M_midCOG_ctrl", create=False), "grazeMode", attr_type="double", keyable=True, create=True)
graze_attr.min = 0
graze_attr.max = 1
ctrl1_blend = api.Node("MooMoo_neck_M001_grazeOffset_mtx", "blendMatrix")
ctrl2_blend = api.Node("MooMoo_neck_M002_grazeOffset_mtx", "blendMatrix")
user_code_nodes += [ctrl1_blend, ctrl2_blend]
cmds.connectAttr(str(graze_attr), f"{ctrl1_blend}.target[0].weight")
cmds.connectAttr(str(graze_attr), f"{ctrl2_blend}.target[0].weight")
ctrl1_offset_mtx = om2.MMatrix((0.214, -0.977, 0, 0, 0.977, 0.214, 0, 0, 0, 0, 1, 0, -0.873, -0.740, 0, 1))
ctrl2_offset_mtx = om2.MMatrix((1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, -0.293, -0.581, 0, 1))
cmds.setAttr(f"{ctrl1_blend}.target[0].targetMatrix", ctrl1_offset_mtx, type="matrix")
cmds.setAttr(f"{ctrl2_blend}.target[0].targetMatrix", ctrl2_offset_mtx, type="matrix")
api.Attribute(ctrl1_blend, "outputMatrix").connect_to("MooMoo_neck_M001_ctrl.offsetParentMatrix")
api.Attribute(ctrl2_blend, "outputMatrix").connect_to("MooMoo_neck_M002_ctrl.offsetParentMatrix")
graze_bs = cmds.blendShape("MooMoo_headPiece_facial_geo", "MooMoo_grazeCorrective_geo", "MooMoo_body_geo", topologyCheck=False, frontOfChain=True, weight=[(0, 1), (1, 1)], name="MooMoo_grazeCorrective_BS")[0]
user_code_nodes.append(api.Node(graze_bs, create=False))
cmds.connectAttr(str(graze_attr), f"{graze_bs}.MooMoo_grazeCorrective_geo")


# LEG CORRECTIVES ---------------------------------------------------------
source = api.DagNode("MooMoo_body_geo", create=False)
target = api.DagNode("MooMoo_frontLeg_L_corrective_geo", create=False)
driver = api.DagNode("MooMoo_frontLeg_bottomTwist_L_point001_jnt", create=False)
driver_parent = api.DagNode("MooMoo_frontLeg_topTwist_L_point002_jnt", create=False)
nodes = utilities.rig_utils.corrective_from_angle(source=source, corrective_multiplier=1.2, corrective_shape=target, driver=driver, driver_parent=driver_parent, name="MooMoo_leg", min_angle=0, max_angle=-90, axis="z")
user_code_nodes += nodes

target = api.DagNode("MooMoo_frontLeg_R_corrective_geo", create=False)
driver = api.DagNode("MooMoo_frontLeg_bottomTwist_R_point001_jnt", create=False)
driver_parent = api.DagNode("MooMoo_frontLeg_topTwist_R_point002_jnt", create=False)
nodes = utilities.rig_utils.corrective_from_angle(source=source, corrective_multiplier=1.2, corrective_shape=target, driver=driver, driver_parent=driver_parent, blendshape_node=nodes[0], min_angle=0, max_angle=-90, axis="z")
user_code_nodes += nodes

# Add all the created nodes to the rig container
cmds.container("MooMoo_RIG", edit=True, addNode=[i.name for i in user_code_nodes])


# GEO CLEANUP ----------------------------------------------------------------------
for geo in api.DagNode("FACIAL", create=False).children + api.DagNode("BODY", create=False).children:
    shape_origs = geo.shapes[1:]
    for shape in shape_origs:
        mfn_mesh = om2.MFnMesh(shape._mfn_node.object())
        mfn_mesh.unlockVertexNormals(mfn_mesh.getVertices()[1])
        cmds.polySetToFaceNormal(shape.unique_name)
        cmds.polySoftEdge(shape.unique_name, angle=180, constructionHistory=False)
        cmds.bakePartialHistory(shape.unique_name, prePostDeformers=True)