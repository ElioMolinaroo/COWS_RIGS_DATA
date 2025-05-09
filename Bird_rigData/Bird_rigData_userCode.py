# Create the space switches
switches = (
    ("Bird_legFK_L001_ctrl", ("Bird_body_M_ctrl", "Bird_master_M_offset001_ctrl")),
    ("Bird_legFK_R001_ctrl", ("Bird_body_M_ctrl", "Bird_master_M_offset001_ctrl")),
)
for data in switches:
    child = api.DagNode(data[0], create=False)
    parents = [api.DagNode(i, create=False) for i in data[1]]

    spaces_names = [i.name.removeprefix("Bird_").removesuffix("_ctrl") for i in parents]
    nodes = walrus.connectors.space_switch(child=child, parents=parents, spaces_names=spaces_names, base_name="rigSwitch")
    cmds.container("Bird_RIG", edit=True, addNode=[i.name for i in nodes])