import bpy
import json
import random

def deleteAllObjects():
    """
    Deletes all objects in the current scene
    """
    deleteListObjects = ['MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'HAIR', 'POINTCLOUD', 'VOLUME', 'GPENCIL',
                     'ARMATURE', 'LATTICE', 'EMPTY', 'LIGHT', 'LIGHT_PROBE', 'CAMERA', 'SPEAKER']

    # Select all objects in the scene to be deleted:

    for o in bpy.context.scene.objects:
        for i in deleteListObjects:
            if o.type == i:
                o.select_set(False)
            else:
                o.select_set(True)
    # Deletes all selected objects in the scene:

    bpy.ops.object.delete() 

def creatorFunction(num):
    deleteAllObjects()
    
    max_room_size = 30
    min_room_size = 10
    big_size = 10
    room_size = [None, None, None]
    min_size = 1
    room_bounds = 2
    
    big_size = random.randint(10, max_room_size)

    small_cube_no = random.randint(3, 20)
    small_cubes = []
    
    def makeBigSize():
        room_size = [random.randint(min_room_size, max_room_size), random.randint(min_room_size, max_room_size), random.randint(min_room_size, max_room_size)]
        return room_size


    def makeSmallSize():
        return random.randint(min_size, 5)

    def getLoc():
        x = random.randint(0, big_size) - (big_size / 2)
        return x

    # Create a large cube
    bpy.ops.mesh.primitive_cube_add(size=1, scale=(makeBigSize()))  # Adjust the size as needed
    large_cube = bpy.context.object
    large_cube.location = (0, 0, (big_size / 2))

    # Create smaller cubes
    for i in range(small_cube_no):
        bpy.ops.mesh.primitive_cube_add(size=1)  # Adjust the size of smaller cubes
        small_cube = bpy.context.object
        small_cube.location = (getLoc(), getLoc(), 0.5)  # Position the smaller cubes
        small_cubes.append(small_cube)



    j = {
        "large_cube_location": str(large_cube.location),
        "large_cube_size": str(large_cube.dimensions)
    }

    for id, x in enumerate(small_cubes):
        j["Object" + str(id) + "_location"] = str(x.location)
        j["Object" + str(id) + "_size"] = str(x.dimensions)

    print(json.dumps(j, indent=4))
    
    with open("export_data/data" + str(num) + ".json", "w") as outfile:
        json.dump(j, outfile, indent=4)

    """
    bpy.ops.wm.collada_export( \
    filepath="export_data/" + str(num) + ".dae", \
    include_children=True, triangulate=True)
    """

for i in range(5):
    creatorFunction(i)
