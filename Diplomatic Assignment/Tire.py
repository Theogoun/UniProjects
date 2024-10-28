import bpy

# Define the target object name
object_names = ["TireF", "TireB"]

# Target size for the Z-axis
target_z_size = 0.3

for name in object_names:
    #Get the target object
    obj = bpy.data.objects[name]

    # Get the current dimensions of the object
    current_dimensions = obj.dimensions

    # Calculate the scale factor for the Z-axis
    z_scale_factor = target_z_size / current_dimensions.z

    # Set the new scale for the object
    obj.scale.z = z_scale_factor * obj.scale.z  # Update the Z scale based on the current scale

    # Apply the scale to make the changes permanent
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

# Reset the Z dimension
obj.dimensions.z = target_z_size
