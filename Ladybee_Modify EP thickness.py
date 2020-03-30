#
# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
#
# This file is not part of the original Honeybee


"""
Use this component to modify the thickness of an EP material, which can be plugged into the "Honeybee_EnergyPlus Construction" component.
_
This component requires you to first create an EP material by using the "Honeybee_Energyplus Opaque Material" component.
-
Provided for Honeybee 0.0.65

    Args:
        _name_: An optional text name for the modified EP Material. By default it would be the name of the original EP Material plus the modified thickness
        _material: The EP material to be modified
        _thickness: A number that represents the thickness of the new material in meters (m).
    Returns:
        EPMaterial: An new opaque material that can be plugged into the "Honeybee_EnergyPlus Construction" component.

"""

__author__ = "Alexandre Duverger"

ghenv.Component.Name = "Modify thickness EP Material"
ghenv.Component.NickName = 'ModifyEPMat'
ghenv.Component.Message = 'VER 0.0.65\nFEB_06_2020'
ghenv.Component.IconDisplayMode = ghenv.Component.IconDisplayMode.application
#compatibleHBVersion = VER 0.0.56\nFEB_01_2015
#compatibleLBVersion = VER 0.0.59\nFEB_01_2015
try: ghenv.Component.AdditionalHelpFromDocStrings = "0"
except: pass

import Grasshopper.Kernel as gh
w = gh.GH_RuntimeMessageLevel.Warning


def main(name, material, thickness):
    materialStr = ""

    for cnt, line in enumerate(material.splitlines()):
        if cnt == 1:
            if name == None:
                materialStr += str(line.split(',')[0]) + "_" + str(thickness) + "m,    !Name\n"
            else:
                materialStr += str(name) + ",    !Name\n"
        elif cnt == 3:
            materialStr += str(thickness) + ",    !Thickness {m}\n"
        elif cnt!= len(material.splitlines()) - 1:
            materialStr += line + "\n"
        else:
            materialStr += line

    return materialStr


if _material and _thickness:
    EPMaterial = main(_name_, _material, _thickness)
