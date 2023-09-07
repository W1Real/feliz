import subprocess

repo_path = '/content/drive/mydrive/feliz/volatile-concentration-localux'

codetorun = """
!git clone https://github.com/camenduru/stable-diffusion-webui-colab /content/drive/mydrive/feliz/camendurus
"""

lines = codetorun.splitlines()

def rulesbroken(codetoexecute, cwd=''):
    for line in lines:
        line = line.strip()
        if line.startswith('!'):
            line = line[1:]
        if not line == '':
            try:
                if cwd:
                    subprocess.run(line, shell=True, check=True, cwd=repo_path)
                else:
                    subprocess.run(line, shell=True, check=True)
            except Exception as e:
                print("Exception: " + str(e))

rulesbroken(lines)
