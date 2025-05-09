# Lock attributes on the bucket control
bucket_ctrl = api.DagNode("Bucket_bucket_M_ctrl", create=False)
api.Attribute(bucket_ctrl, "translate").locked = True
api.Attribute(bucket_ctrl, "rotateY").locked = True
api.Attribute(bucket_ctrl, "rotateZ").locked = True
api.Attribute(bucket_ctrl, "scale").locked = True

# Create the space switch between the handle and the bucket
parents = [api.DagNode("Bucket_handle_M_ctrl", create=False), api.DagNode("Bucket_master_M_offset001_ctrl", create=False)]
spaces_names = [i.name.removeprefix("Bucket_").removesuffix("_ctrl") for i in parents]
nodes = walrus.connectors.space_switch(child=bucket_ctrl, parents=parents, spaces_names=spaces_names, base_name="rigSwitch")
cmds.container("Bucket_RIG", edit=True, addNode=[i.name for i in nodes])

# Delete the unwanted attributes
api.Attribute(bucket_ctrl, "space").delete()
api.Attribute(bucket_ctrl, "useTranslate").delete()
api.Attribute(bucket_ctrl, "useScale").delete()