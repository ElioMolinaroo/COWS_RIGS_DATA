# Add the proxy attribute of the foot roll onto the controls
controls_map = [
    {
        "source_attrs": (
            api.Attribute(
                api.Node("Farmer_footIK_L_inputs", create=False), "footRoll"
            ),
            api.Attribute(api.Node("Farmer_footIK_L_inputs", create=False), "bank"),
            api.Attribute(
                api.Node("Farmer_footIK_L_inputs", create=False), "heelTwist"
            ),
            api.Attribute(
                api.Node("Farmer_footIK_L_inputs", create=False), "tipTwist"
            ),
            api.Attribute(
                api.Node("Farmer_footIK_L_inputs", create=False),
                "tweaks_visibility",
            ),
        ),
        "target_ctrls": (
            api.Node("Farmer_legIK_L_root_ctrl", create=False),
            api.Node("Farmer_legIK_L_end_ctrl", create=False),
            api.Node("Farmer_legIK_L_poleVector_ctrl", create=False),
        ),
    },
    {
        "source_attrs": (
            api.Attribute(
                api.Node("Farmer_footIK_R_inputs", create=False), "footRoll"
            ),
            api.Attribute(api.Node("Farmer_footIK_R_inputs", create=False), "bank"),
            api.Attribute(
                api.Node("Farmer_footIK_R_inputs", create=False), "heelTwist"
            ),
            api.Attribute(
                api.Node("Farmer_footIK_R_inputs", create=False), "tipTwist"
            ),
            api.Attribute(
                api.Node("Farmer_footIK_R_inputs", create=False),
                "tweaks_visibility",
            ),
        ),
        "target_ctrls": (
            api.Node("Farmer_legIK_R_root_ctrl", create=False),
            api.Node("Farmer_legIK_R_end_ctrl", create=False),
            api.Node("Farmer_legIK_R_poleVector_ctrl", create=False),
        ),
    },
]
for data in controls_map:
    for attr in data["source_attrs"]:
        for ctrl in data["target_ctrls"]:
            attr.create_proxy(ctrl)
