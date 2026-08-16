import subprocess

cwd = r'C:\Users\omerc\Desktop\ai-personal-coach'

def run(cmd):
    print(f"Running: {cmd}")
    res = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)
    return res

run("git add .")
run("git commit -m \"merge: sync with upstream main and resolve references.bib\"")
run("git push origin feat/data-research-k3")
