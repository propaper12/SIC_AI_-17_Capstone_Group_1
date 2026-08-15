import subprocess
import os

cwd = r'C:\Users\omerc\Desktop\ai-personal-coach'

def run(cmd):
    print(f"Running: {cmd}")
    res = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)
    return res

run("git init")
run("git remote remove origin") # Ignore error if doesn't exist
run("git remote add origin https://github.com/edasaruhan/SIC_AI_-17_Capstone_Group_1.git")
run("git checkout -b feat/data-research-k3")
run("git add .")
run("git commit -m \"feat(data-research): Kişi 3 EDA dokümanı, oulad_eda notebook ve grafikleri eklendi\"")
run("git push -u origin feat/data-research-k3")
