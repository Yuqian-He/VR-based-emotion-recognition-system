import os
import sys
import subprocess

def run_Unreal():
        # import sys
    # import os

    venv_path = os.path.join(os.environ['VIRTUAL_ENV'], 'Lib', 'site-packages')  # Replace 'python3.8' with your Python version
    # print(os.environ['VIRTUAL_ENV'])

    sys.path.append(venv_path)
    sys.path.append(os.getcwd())
    sys.path.append('D:/CAVE/PROJECTS/GROUP_PRJ/UE/AI_INTEGRATION/AI_Script')
    sys.path.append('D:/CAVE/PROJECTS/GROUP_PRJ/UE/AI_INTEGRATION/AI_Script/bin')
    # sys.path.append('D:/CAVE/PROJECTS/GROUP_PRJ/UE/AI_INTEGRATION/AI_Script/env')
    # sys.path.append('D:/CAVE/PROJECTS/GROUP_PRJ/UE/AI_INTEGRATION/AI_Script/bin')

    project_path = "D:/CAVE/PROJECTS/GROUP_PRJ/UE/AI_INTEGRATION/Unreal_project/AI_Integration.uproject"
    unreal_path = "C:/Program Files/Epic Games/UE_5.0/Engine/Binaries/Win64/UnrealEditor-Cmd.exe"

    subprocess.run([ unreal_path, project_path ] , shell=True, check=True)

run_Unreal()