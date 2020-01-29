from subprocess import Popen, PIPE

# execute command
process = Popen(" ".join(['ping', '-c5', '8.8.8.8']),
                shell=True, stdout=PIPE, stderr=PIPE)

# read STDOUT
print(process.stdout.read())

# wait for child process to terminate.
rc = process.wait()
print("exit code: {}".format(rc))

# read STDERR
print("error: {}".format(process.stderr.read()))
