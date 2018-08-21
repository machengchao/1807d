import os
pid = os.fork()
print(pid)
if pid ==0:
	print("子进程%d,父进程%d"%(os.getpid(),os.getppid()))
else:
	print("父进程%d,父父进程%d"%(os.getpid(),os.getppid()))




