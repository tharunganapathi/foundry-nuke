print '\n'
from hiero.ui.nuke_bridge.FnNsFrameServer import frameServer
s = [worker.address for worker in frameServer.getStatus(1).workerStatus]


for i in s:
print i




python.exe "C:\Program Files\Nuke12.2v5\pythonextensions\site-packages\foundry\frameserver\nuke\runframeserver.py" --numworkers=2 --nukeworkerthreads=4 --nukeworkermemory=8096 --workerconnecturl=tcp://192.168.5.67:4101 --nukepath=Nuke12.2.exe







from hiero.ui.nuke_bridge import FnNsFrameServer

#Queue background render of all the frames for a script
FnNsFrameServer.renderScript("C:/temp/test.nk")

#Queue background render of a range of frames for a script
FnNsFrameServer.renderFrames("C:/temp/test.nk", "1-10", "Write1", ["main"]
from hiero.ui.nuke_bridge import FnNsFrameServer



#Queue background render of all the frames for a script

FnNsFrameServer.renderScript('//liv1/shows/ORI/SAB2_202_016_0100_MP01/mid/paint/TharunG/workfile/nuke/SAB2_202_016_0100_MP01_pipeline_start_b001_v001.nk')

FnNsFrameServer.renderFrames('Write2')



#Queue background render of a range of frames for a script

FnNsFrameServer.renderFrames("C:/temp/test.nk", "1-10", "Write1", ["main"])





FnNsFrameServer.renderFrames()
