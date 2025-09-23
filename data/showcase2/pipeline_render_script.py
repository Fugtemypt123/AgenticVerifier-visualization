import bpy
import random
import json
import os
import sys
from sys import platform

if __name__ == "__main__":

    code_fpath = sys.argv[6]  # Path to the code file
    rendering_dir = sys.argv[7] # Path to save the rendering from camera1
    if len(sys.argv) > 8:
        save_blend = sys.argv[8] # Path to save the blend file
    else:
        save_blend = None

    # Enable GPU rendering
    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.preferences.addons['cycles'].preferences.compute_device_type = 'CUDA'  # or 'OPTIX' if your GPU supports it
    bpy.context.preferences.addons['cycles'].preferences.get_devices()

    # Check and select the GPUs
    for device in bpy.context.preferences.addons['cycles'].preferences.devices:
        if device.type == 'GPU' and not device.use:
            device.use = True

    # Set the rendering device to GPU
    bpy.context.scene.cycles.device = 'GPU'

    # Setting up rendering resolution
    bpy.context.scene.render.resolution_x = 512
    bpy.context.scene.render.resolution_y = 512

    # Set max samples to 1024
    bpy.context.scene.cycles.samples = 512

    # Set color mode to RGB
    bpy.context.scene.render.image_settings.color_mode = 'RGB'

    # Read and execute the code from the specified file
    with open(code_fpath, "r") as f:
        code = f.read()
    try:
        exec(code)
    except:
        raise ValueError

    # Print current scene object information
    # print("\n=== Scene Objects Summary ===")
    # try:
    #     count = 0
    #     for obj in bpy.data.objects:
    #         count += 1
    #         loc = tuple(round(v, 4) for v in obj.location[:]) if hasattr(obj, 'location') else (0.0, 0.0, 0.0)
    #         dims = tuple(round(v, 4) for v in getattr(obj, 'dimensions', (0.0, 0.0, 0.0)))
    #         print(f"- {obj.name} | type={obj.type} | loc={loc} | dims={dims}")
    #     print(f"Total objects: {count}")
    # except Exception as e:
    #     print(f"[Warn] Failed to list scene objects: {e}")
        
    # # print all object information
    # for obj in bpy.data.objects:
    #     print("Name: ", obj.name)
    #     print("Type: ", obj.type)
    #     print("Location: ", obj.location)
    #     print("Rotation: ", obj.rotation_euler)
    #     print("Scale: ", obj.scale)
    #     print("--------------------------------")
        
    # 将物体重新命名：
    # model.002 -> lounge
    # model.009 -> snowman
    # model.008 -> tree
    # model.005 -> box_in
    # model -> box_out
    # model.006 -> tree_in
    # model.001 -> tree_out
    # model.004 -> clock
    # model.007 -> fireplace
    # model.003 -> bell
    # for obj in bpy.data.objects:
    #     if obj.name == 'model.002':
    #         obj.name = obj.name.replace('model.002', 'lounge_area')
    #     elif obj.name == 'model.009':
    #         obj.name = obj.name.replace('model.009', 'snowman')
    #     elif obj.name == 'model.008':
    #         obj.name = obj.name.replace('model.008', 'christmas_tree')
    #     elif obj.name == 'model.005':
    #         obj.name = obj.name.replace('model.005', 'box_inside')
    #     elif obj.name == 'model':
    #         obj.name = obj.name.replace('model', 'box_outside')
    #     elif obj.name == 'model.006':
    #         obj.name = obj.name.replace('model.006', 'tree_decoration_inside')
    #     elif obj.name == 'model.001':
    #         obj.name = obj.name.replace('model.001', 'tree_decoration_outside')
    #     elif obj.name == 'model.004':   
    #         obj.name = obj.name.replace('model.004', 'clock')
    #     elif obj.name == 'model.007':
    #         obj.name = obj.name.replace('model.007', 'fireplace')
    #     elif obj.name == 'model.003':
    #         obj.name = obj.name.replace('model.003', 'bell')
    
    # Remove all the lights
    # for light in bpy.data.lights:
    #     bpy.data.lights.remove(light)

    # Render from camera1
    if 'Camera1' in bpy.data.objects:
        #  <Vector (6.7303, -4.8700, 3.7385)>; Rotation: <Euler (x=1.5149, y=-0.0000, z=0.9215)
        # Location: <Vector (6.3806, -5.1588, 3.9730)>; Rotation: <Euler (x=1.2636, y=-0.0000, z=0.8866)
        # bpy.data.objects['Camera1'].location = (6.3806, -5.1588, 3.9730)
        # bpy.data.objects['Camera1'].rotation_euler = (1.2636, -0.0000, 0.8866)
        bpy.context.scene.camera = bpy.data.objects['Camera1']
        bpy.context.scene.render.image_settings.file_format = 'PNG'
        bpy.context.scene.render.filepath = os.path.join(rendering_dir, 'render1.png')
        bpy.ops.render.render(write_still=True)
        
    # print(f"Camera1 location: {bpy.data.objects['Camera1'].location}")
    # print(f"Camera1 rotation: {bpy.data.objects['Camera1'].rotation_euler}")
    # print(f"Camera1 lens: {bpy.data.objects['Camera1'].data.lens}")

    # Render from camera2 (not used in hard tasks)
    # if 'Camera2' in bpy.data.objects:
    #     bpy.context.scene.camera = bpy.data.objects['Camera2']
    #     bpy.context.scene.render.image_settings.file_format = 'PNG'
    #     bpy.context.scene.render.filepath = os.path.join(rendering_dir, 'render1.png')
    #     bpy.ops.render.render(write_still=True)

    # Save the blend file
    if save_blend:
        # Set the save version to 0
        bpy.context.preferences.filepaths.save_version = 0
        # Save the blend file
        bpy.ops.wm.save_as_mainfile(filepath=save_blend)



"""
model.002 lounge
model.008 tree
model.009 snowman
model.005 box_in
model box_out
model.006 tree_in
model.001 tree_out
model.004 clock
model.007 fireplace
model.003 bell
"""