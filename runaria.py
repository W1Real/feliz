import pickle, subprocess

with open('/content/arialist.pkl', 'rb') as f:
    arialines = pickle.load(f)
    
for line in arialines:
  if not '4x-UltraSharp.pth' in line:
    ariaexecline = line[2:].replace('\\n",', '').replace('/content/stable-diffusion-webui', '/content/volatile-concentration-localux')
    try:
      subprocess.run(ariaexecline, shell=True, check=True)
    except Exception as e:
        print("Exception: " + str(e))