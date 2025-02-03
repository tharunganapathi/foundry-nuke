print '\n'
from hiero.ui.nuke_bridge.FnNsFrameServer import frameServer
s = [worker.address for worker in frameServer.getStatus(1).workerStatus]

# print the workers
for i in s:
  print (i)



# execute
python.exe "C:\Program Files\Nuke12.2v5\pythonextensions\site-packages\foundry\frameserver\nuke\runframeserver.py" --numworkers=2 --nukeworkerthreads=4 --nukeworkermemory=8096 --workerconnecturl=tcp://192.168.5.26:5560 --nukepath=Nuke12.2.exe
