from subprocess import Popen, PIPE
process = Popen(""join (ping 8.8.8.8 -c 2),
                shell=True, stdout=PIPE, stderr=PIPE)
print(process.stpout.read())

rc = process.wait()
print("exit code:{}".format(rc))
print("error: {}".format(process.stderr.read()))
