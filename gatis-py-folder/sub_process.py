from subprocess import Popen, PIPE

ipaddr = '8.8.8.8'
my_string = " ".join(['ping', str(ipaddr), '-c', '2'])
print ("Executing command: %s \n" % my_string)

process = Popen(my_string, shell=True, stdout=PIPE, stderr=PIPE)
rc = process.wait()

print (process.stdout.read())
print ("exit code: {}".format(rc))
print ("error: {}".format(process.stderr.read()))
