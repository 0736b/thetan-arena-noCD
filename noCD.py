from time import sleep
from utils.mem import *

def main():
    while True:
        try:
            pm = pymem.Pymem("Thetan Arena.exe")
            print("Process ID:",pm.process_id, "Game found!")
            sleep(1)
            break
        except:
            print("Please run Thetan Arena, waiting for game...")
            sleep(1)
    
    skill_cd_pattern = b"\\x48\\x89\\x77\\x04\\x75.\\x48\\x8B\\x57\\x24\\x45\\x33\\xC0\\x48\\x8B\\xCD\\xE8....\\x48\\x85\\xC0"
    no_cd_patchbytes = b"\xC7\x47\x04\x00\x00\x00\x00\x90\x90\x90"
    isFound = False

    while True:
        try:
            print("AOB scanning")
            skill_cd_addrs = pattern_scan_all(pm.process_handle, skill_cd_pattern, return_multiple=True)
            print("found")
            for addr in skill_cd_addrs:
                print(hex(addr), pymem.memory.read_bytes(pm.process_handle,addr,10))
            isFound = True
            break
        except:
            print("not found, need to update pattern")
            sleep(1)

    if isFound:
        for addr in skill_cd_addrs:
            pymem.memory.write_bytes(pm.process_handle, addr, no_cd_patchbytes, 10)
        print("patched")
    
if __name__ == "__main__":
    main()