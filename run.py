import sys
import os
import bpy

blend_dir = os.path.dirname(bpy.data.filepath)
if blend_dir not in sys.path:
   sys.path.append(blend_dir)

#import multy_file_addon
import single_file_addon
import imp
#imp.reload(multy_file_addon)
imp.reload(single_file_addon)
#multy_file_addon.register()
single_file_addon.register()
