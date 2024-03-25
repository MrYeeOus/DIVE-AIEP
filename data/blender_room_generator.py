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
    global room_size
    min_size = 1
    room_bounds = 2
    
    big_size = random.randint(10, max_room_size)

    small_cube_no = random.randint(3, 20)
    small_cubes = []
    
    def makeBigSize():
        global room_size
        room_size = [random.randint(min_room_size, max_room_size), random.randint(min_room_size, max_room_size), random.randint(min_room_size, max_room_size)]


    def makeSmallSize():
        return random.randint(min_size, 5)

    def getLocX():
        global room_size
        x = random.randint(0, room_size[0] - 2) - ((room_size[0] - 2) / 2)
        return x
    def getLocY():
        global room_size
        x = random.randint(0, room_size[1] - 2) - ((room_size[1] - 2)/ 2)
        return x

    # Create a large cube
    makeBigSize()
    bpy.ops.mesh.primitive_cube_add(size=1, scale=(room_size[0], room_size[1], room_size[2]))  # Adjust the size as needed
    large_cube = bpy.context.object
    #print("Roomsize = " + str(room_size))
    large_cube.location = (0, 0, (room_size[2] / 2))

    # Create smaller cubes
    for i in range(small_cube_no):
        bpy.ops.mesh.primitive_cube_add(size=1)  # Adjust the size of smaller cubes
        small_cube = bpy.context.object
        small_cube.location = (getLocX(), getLocY(), 0.5)  # Position the smaller cubes
        small_cubes.append(small_cube)
        
    # Set room as parent
    for i in small_cubes:
        i.parent = large_cube
        i.matrix_parent_inverse = large_cube.matrix_world.inverted()



    j = {
        "large_cube_location": str(large_cube.location),
        "large_cube_size": str(large_cube.dimensions)
    }

    for id, x in enumerate(small_cubes):
        j["Object" + str(id) + "_location"] = str(x.location)
        j["Object" + str(id) + "_size"] = str(x.dimensions)

    #print(json.dumps(j, indent=4))
    
    with open("export_data/data" + str(num) + ".json", "w") as outfile:
        json.dump(j, outfile)
        print()

    
    bpy.ops.wm.collada_export( \
    filepath="export_data/" + str(num) + ".dae", \
    include_children=True, triangulate=True)
    

for i in range(1000):
    creatorFunction(i)
