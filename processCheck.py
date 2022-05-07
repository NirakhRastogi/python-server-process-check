from cmath import pi
from os import system
import platform
import psutil
import os

def check_running_process(pid: int, process_name: str, skip_check_pid:bool):
    print("Currently running OS -", platform.system(), ", version-", platform.release())
    print(f"Skip check pid is set to {skip_check_pid}")
    processes = [p for p in psutil.process_iter()]
    processFoundRunning:bool = False
    for process in processes:
        if process.name() == process_name:
            print(f'Found a process with name `{process_name}`')
            if skip_check_pid or process.pid == pid:
                print(f'PID of the process is `{pid}` ~ matched')
                if process.is_running:
                    print(f'Processing with pid {pid} and process_name {process_name} is running.')
                    processFoundRunning = True
                    break
                else:
                    print(f'Processing with pid {pid} and process_name {process_name} is not running.')
            else:
                print(f'PID of the process is `{pid}` ~ not matched')
    return processFoundRunning

def check_file_exists_at_location(filename:str, absolute_path:str):
    file_path = absolute_path+"/"+filename
    print(f'Checking for file with name `{filename}` at path `{absolute_path}`, combined path formed is `{file_path}`')
    if os.path.exists(file_path):
        print(f'File `{filename}` exists at path `{absolute_path}`')
        return True
    else:
        print(f'File `{filename}` does not exists at path `{absolute_path}`')
        return False