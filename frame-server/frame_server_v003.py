from hiero.ui.nuke_bridge import FnNsFrameServer
#FnNsFrameServer.renderScript('C:/Users/DELL/Desktop/1.nk')
FnNsFrameServer.renderFrames('C:/Users/DELL/Desktop/1.nk', "1-10", nuke.selectedNode().name(),'')
