import os


print('Process (%s) start...' % os.getpid())
# Only work on Unix/Linux/Mac:
# 會報錯，window系統沒有fork調用
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))