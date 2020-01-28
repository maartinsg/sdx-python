from subprocess import Popen, PIPE

print(" ".join(['ping', '8.8.8.8', '-c', '2']))
process = Popen(" ".join(['ping', '8.8.8.8', '-c', '2']), shell=True, stdout=PIPE, stderr=PIPE)

print(process.stdout.read())

rc = process.wait()
print ("exit code: {}".format(rc))

print ("error: {}".format(process.stderr.read()))
