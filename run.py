import sys
import os
import bpy

blend_dir = os.path.dirname(bpy.data.filepath)
if blend_dir not in sys.path:
   sys.path.append(blend_dir)

import boilerplate
#import single_file_addon
import imp
imp.reload(boilerplate)
#imp.reload(single_file_addon)
boilerplate.register()
#single_file_addon.register()
