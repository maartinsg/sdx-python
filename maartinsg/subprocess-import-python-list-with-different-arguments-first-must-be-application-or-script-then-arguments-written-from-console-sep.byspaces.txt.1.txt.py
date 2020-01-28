from subprocess import Popen, PIPE

# command processed
process = Popen(" ".join(['ping', '-c', '2', '127.0.0.1']), shell=True, stdout=PIPE, stderr=PIPE)

#read STDOUT
print(process.stdout.read())

#wait for the subprocess to finish?
rc = process.wait()
print("exit code: {}".format(rc))

#read STDERR
print("error: {}".format(process.stderr.read()))
