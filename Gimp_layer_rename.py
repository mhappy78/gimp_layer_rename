#!/usr/bin/env python
'''
rename layers to rename + numbering
This script renames all layers in the image with a base name and numbering.

To install, place this file in: *install*/lib/gimp/*version*/plug-ins/
Where *install* is the GIMP installation folder and *version* is the GIMP version.

To run, in GIMP choose: Layer -> Rename Layers... 

Original hosting location:
git@github.com:mhappy78/gimp_layer_rename.git
'''

from gimpfu import *

def rename_layers(image, drawable, base_name):
    # Get the layers
    layers = image.layers
    # check layers number
    if len(layers) == 0:
        gimp.message("No layers found")
        return
    else:
        num_layers = len(layers)

    # Rename the layers: base_name + _ + number
    for i in range(num_layers):
        layer = layers[i]
        layer.name = base_name + "_" + str(i)
    
    # image update
    gimp.displays_flush()

register(
    "python_fu_rename_layers",
    "Rename layers with base name and numbering",
    "Renames all layers in the image with a base name and numbering",
    "Lee Dong Lak",
    "Lee Dong Lak",
    "2024",
    "<Image>/Layer/Rename Layers...",
    "*",
    [
        (PF_STRING, "base_name", "Base name for layers", "Layer")
    ],
    [],
    rename_layers)

main()