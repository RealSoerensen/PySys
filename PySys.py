import wmi
import psutil

system = wmi.WMI()

class system_info:
    class os:
        def version():
            return system.Win32_OperatingSystem()[0].Caption
        def bit():
            return system.Win32_OperatingSystem()[0].OSArchitecture
        def hostname():
            return system.Win32_OperatingSystem()[0].CSName
        def uuid():
            return system.Win32_OperatingSystem()[0].SerialNumber
        def registered_user():
            return system.Win32_OperatingSystem()[0].RegisteredUser
        def install_location():
            return system.Win32_OperatingSystem()[0].SystemDirectory

    class cpu:
        def name():
            return system.Win32_Processor()[0].Name
        def desc():
            return system.Win32_Processor()[0].Description
        def num_of_Cores():
            return system.Win32_Processor()[0].NumberOfCores
        def threads():
            return system.Win32_Processor()[0].ThreadCount
        def current_clockspeed():
            return system.Win32_Processor()[0].CurrentClockSpeed
        def max_clockspeed():
            return system.Win32_Processor()[0].MaxClockSpeed
        def current_load():
            return str(system.Win32_Processor()[0].LoadPercentage) + "%"
        def current_voltage():
            return system.Win32_Processor()[0].CurrentVoltage

    class gpu:
        def name():
            return system.Win32_VideoController()[0].Name
        def vram():
            return str(system.Win32_VideoController()[0].AdapterRAM / 1048576)
        def refreshrate():
            return str(system.Win32_VideoController()[0].CurrentRefreshRate)
        def max_refreshrate():
            return str(system.Win32_VideoController()[0].MaxRefreshRate)
        def driver_version():
            return str(system.Win32_VideoController()[0].DriverVersion)

    class ram:
        def current_usage():
            return str(psutil.virtual_memory().percent) + "%"
        def size():
            return str(round(psutil.virtual_memory().total/1048576000)) + "GB"
        def used():
            return str(round(psutil.virtual_memory().used/1048576000)) + "GB"
        def available():
            return str(round(psutil.virtual_memory().available/1048576000)) + "GB"

    class disks:
        def disk_counter():
            counter=0
            partitions = psutil.disk_partitions()
            for i in partitions:
                counter+=1
            return counter

        def device(disk):
            return disk.device

        def type(disk):
            return disk.fstype

        def disk_usage(disk):
            obj_disk = psutil.disk_usage(disk.device)
            return str(round(obj_disk.total / (1024.0 ** 3))) + "GB", str(round(obj_disk.used / (1024.0 ** 3))) + "GB", str(round(obj_disk.free / (1024.0 ** 3))) + "GB", str(obj_disk.percent) + "%"

while True:
    print("PySyS by Soerensen\n" + 
    "*"*40 + 
    "\n1. OS: " + system_info.os.version() + 
    "\n2. CPU: " + system_info.cpu.name() + 
    "\n3. GPU: " + system_info.gpu.name() + 
    "\n4. RAM: " + str(system_info.ram.size()) + 
    "\n5. Storage: " + str(system_info.disks.disk_counter()) + " disk(s) connected\n" + 
    "*"*40 + 
    "\nPress one of the numbers (1-5) to get more info")


    flag = True
    while flag:
        choice = input()
        try:
            if int(choice) > 0 and int(choice) <= 5:
                flag = False
        except:
            print("Invalid option")

    if choice == "1":
        print("\n"*10)
        print("OS Information\n" + 
        "*"*40 + 
        "\nHostname: " + system_info.os.hostname() + 
        "\nOS Version: " + system_info.os.version() + 
        "\nBit: " + system_info.os.bit() +
        "\nInstall location: " + system_info.os.install_location() +
        "\nUUID: " + system_info.os.uuid() +
        "\nLicensed to " + str(system_info.os.registered_user()) + "\n" + 
        "*"*40)
        input("Press any key to return")
        print("\n"*10)

    elif choice == "2":
        print("\n"*10)
        print("CPU Information\n" + 
        "*"*40 +
        "\nCPU name: " + system_info.cpu.name() + 
        "\nDescription: " + system_info.cpu.desc() + 
        "\nNum of Cores: " + str(system_info.cpu.num_of_Cores()) + 
        "\nNum of Threads: " + str(system_info.cpu.threads()) + 
        "\nLoad: " + str(system_info.cpu.current_load()) + 
        "\nClock speed: " + str(system_info.cpu.current_clockspeed()) +
        "\nMax clock speed: " + str(system_info.cpu.max_clockspeed()) + 
        "\nVoltage: " + str(system_info.cpu.current_voltage()) + "\n" +
        "*"*40)
        input("Press any key to return")
        print("\n"*10)
    
    elif choice == "3":
        print("\n"*10)
        print("GPU Information\n" + 
        "*"*40 +
        "\nGPU Name: " + system_info.gpu.name() + 
        "\nVRAM: " + system_info.gpu.vram() +
        "\nDriver version: " + system_info.gpu.driver_version() +
        "\nCurrent Refreshrate: " + system_info.gpu.refreshrate() +
        "\nMax refreshrate: " + system_info.gpu.max_refreshrate() + "\n" +
        "*"*40)
        input("Press any key to return")
        print("\n"*10)

    elif choice == "4":
        print("\n"*10)
        print("RAM Information\n" +
        "*"*40 + 
        "\nRAM Usage: " + system_info.ram.current_usage() +
        "\nSize: " + system_info.ram.size() +
        "\nUsed: " + system_info.ram.used() +
        "\nAvailable: " + system_info.ram.available() + "\n" +
        "*"*40)
        input("Press any key to return")
        print("\n"*10)
        
    elif choice == "5":
        print("\n"*10)
        print("Disk Information\n" + 
        "*"*40)
        for disk in psutil.disk_partitions():
            print("Path: " + system_info.disks.device(disk) +
            "\nType: " + system_info.disks.type(disk) + 
            "\nTotal size: " + system_info.disks.disk_usage[0] +
            "\nUsed: " + system_info.disks.disk_usage[1] +
            "\nFree: " + system_info.disks.disk_usage[2] + 
            "\nPercent used: " + system_info.disks.disk_usage[4])
        print("*"*40)
        input("Press any key to return")
        print("\n"*10)
    