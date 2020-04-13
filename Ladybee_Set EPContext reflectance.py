#
# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
#
# This file is not part of the original Honeybee


"""
Use this component to set the reflectance of an EP context.
-
Provided for Honeybee 0.0.65

    Args:
        _names: Names of the HBcontext:Surface to be modified. Use "Honeybee_Get or Set HB Obect Name" to get the name of an HBContext.
        unglazedRef_: The diffuse solar reflectance of the unglazed part of the shading surface (default = 0.2).
        glazedRef_: The diffuse visible reflectance of the unglazed part of the shading surface (default = 0.2).
        WWR_: The fraction of the area of the shading surface that consists of windows (default = 0.0).
        glazingConstr: The name of the construction of the windows on the shading surface. Required if WWR is greater than 0.0.
    Returns:
        ref: idf to be linked in additionalStrings_ of the "Honeybee_Export to OpenStudio" component.

"""

ghenv.Component.Name = "Set EP context reflectance"
ghenv.Component.NickName = 'SetEPContRef'
ghenv.Component.Message = 'VER 0.0.65\nFEB_06_2020'
ghenv.Component.IconDisplayMode = ghenv.Component.IconDisplayMode.application
ghenv.Component.Category = 'LadyBee'
ghenv.Component.SubCategory = "10 | Energy | Energy"
#compatibleHBVersion = VER 0.0.56\nFEB_01_2015
#compatibleLBVersion = VER 0.0.59\nFEB_01_2015
try: ghenv.Component.AdditionalHelpFromDocStrings = "0"
except: pass


def createEPRef(name, unglazedRef, glazedRef, WWR, glazingConstr):
    if unglazedRef == None: unglazedRef = 0.2
    if glazedRef == None: unglazedRef = 0.2
    if WWR == None:
        WWR = 0
        glazingConstr = ""
    return "ShadingProperty:Reflectance,\n" \
        "{}, !- Name of Surface:Shading Object\n" \
        "{},  !- Diffuse Solar Reflectance of Unglazed Part of Shading Surface\n" \
        "{},  !- Diffuse Visible Reflectance of Unglazed Part of Shading Surface\n" \
        "{},  !- Fraction of Shading Surface That Is Glazed\n" \
        "{}; !- Name of Glazing Construction\n".format(
        name + "_0", unglazedRef, glazedRef, WWR, glazingConstr
        )


reflectances = (createEPRef(name, unglazedRef_, glazedRef_, WWR_, glazingConstr) \
               for name in _names)

ref = "\n".join(reflectances)
    
