if nuke.NUKE_VERSION_MAJOR <= 12:
    nuke.pluginAddPath('nuke_12')
else:
    nuke.pluginAddPath('nuke13')





import recent_files