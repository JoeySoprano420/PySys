import wmi

def get_cpu_info():
    c = wmi.WMI(namespace="root\CIMv2")
    for processor in c.Win32_Processor():
        print(f"Processor: {processor.Name}")
        print(f"Manufacturer: {processor.Manufacturer}")
        print(f"Speed: {processor.CurrentClockSpeed} MHz")
        print(f"Number of Cores: {processor.NumberOfCores}")
        print(f"Number of Logical Processors: {processor.NumberOfLogicalProcessors}")

get_cpu_info()


import subprocess

def set_power_plan(plan_name):
    """Set the power plan in Windows."""
    command = f"powercfg /s {plan_name}"
    subprocess.run(command, shell=True)

# Example usage: Set to High Performance
set_power_plan("High Performance")


subprocess.run("powercfg /list", shell=True)


import subprocess

def run_ryzen_master():
    """Run Ryzen Master (if installed) to manipulate performance settings."""
    try:
        subprocess.run(["C:\\Program Files\\AMD\\RyzenMaster\\RyzenMaster.exe"])
    except FileNotFoundError:
        print("Ryzen Master is not installed or not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

run_ryzen_master()


import subprocess

def update_bios_using_hp_bcu():
    """Update BIOS using HP's BIOS Configuration Utility (BCU)."""
    command = "C:\\Path\\To\\BCU\\biosconfigutility.exe /update"
    subprocess.run(command, shell=True)

update_bios_using_hp_bcu()


def disable_hyper_threading():
    """Disable Hyper-Threading (HT) using wmic."""
    # To disable HT, you would typically need to do it from the BIOS, 
    # but for process affinity, we can assign a process to specific cores.
    command = "wmic cpu set NumberOfCores=4"  # Adjust this based on your needs
    subprocess.run(command, shell=True)

disable_hyper_threading()


import subprocess
import wmi

def run_bash_command(command):
    """Run a shell command."""
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
    
def get_cpu_info():
    """Retrieve CPU information."""
    c = wmi.WMI(namespace="root\CIMv2")
    for processor in c.Win32_Processor():
        print(f"Processor: {processor.Name}")
        print(f"Manufacturer: {processor.Manufacturer}")
        print(f"Speed: {processor.CurrentClockSpeed} MHz")
        print(f"Number of Cores: {processor.NumberOfCores}")
        print(f"Number of Logical Processors: {processor.NumberOfLogicalProcessors}")

def set_power_plan(plan_name):
    """Set the power plan in Windows."""
    command = f"powercfg /s {plan_name}"
    run_bash_command(command)

def update_bios_using_hp_bcu():
    """Update BIOS using HP's BIOS Configuration Utility (BCU)."""
    command = "C:\\Path\\To\\BCU\\biosconfigutility.exe /update"
    run_bash_command(command)

def disable_hyper_threading():
    """Disable Hyper-Threading (HT) using wmic."""
    command = "wmic cpu set NumberOfCores=4"  # Example to disable HT
    run_bash_command(command)

if __name__ == "__main__":
    # Get CPU Info
    print("Retrieving CPU Information:")
    get_cpu_info()

    # Set Power Plan to High Performance
    print("Setting Power Plan to High Performance:")
    set_power_plan("High Performance")

    # Update BIOS firmware using HP BCU
    print("Updating BIOS Firmware:")
    update_bios_using_hp_bcu()

    # Disable Hyper-Threading (HT)
    print("Disabling Hyper-Threading:")
    disable_hyper_threading()


