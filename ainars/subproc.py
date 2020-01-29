from subprocess import Popen, PIPE
# execute command
process = Popen("ping 8.8.8.8 -c 2", shell=True, stdout=PIPE, stderr=PIPE)
# " ".join([list]) --> joins together list in string with spaces in between

# read STDOUT
print(process.stdout.read())

# wait for child process to terminate
rc = process.wait()
print("exit code: {}".format(rc))

#read STRERR
print("error: {}".format(process.stderr.read()))
