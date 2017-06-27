 import os, os.path
 path = os.path.expanduser('~') + "/.matplotlib"
 if not os.path.exists(path): os.mkdir(path)
 with open(path + "/matplotlibrc", "w") as f:
  f.write("font.family : IPAexGothic\n")
 print("ok")
