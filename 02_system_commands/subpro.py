import subprocess

# subprocess.run("ls -l", shell=True)
# result = subprocess.run(["find", "/", "-name", "ls"], universal_newlines=True,
#                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print(result.stdout)
# print(result.stderr[0:200])

# s = subprocess.Popen("ls -l", shell=True)
# s.wait()

p1 = subprocess.Popen(["ls", "-l", "/etc"], stdout=subprocess.PIPE)

p2 = subprocess.Popen(["grep", "sudo"], stdin=p1.stdout)

p1.stdout.close()
p2.communicate()
