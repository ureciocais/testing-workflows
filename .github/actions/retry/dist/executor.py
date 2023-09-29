import subprocess
import sys
print(sys.argv)
subprocess.run([sys.argv[1]], shell=sys.argv[2])