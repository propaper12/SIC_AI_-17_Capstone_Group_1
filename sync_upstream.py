import subprocess
import os

cwd = r'C:\Users\omerc\Desktop\ai-personal-coach'

def run(cmd):
    print(f"Running: {cmd}")
    res = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)
    return res

run("git remote remove upstream")
run("git remote add upstream https://github.com/edasaruhan/SIC_AI_-17_Capstone_Group_1.git")
run("git fetch upstream")
run("git checkout feat/data-research-k3")
run("git merge upstream/main --allow-unrelated-histories -m \"merge: sync with upstream main\"")
run("git push origin feat/data-research-k3")
