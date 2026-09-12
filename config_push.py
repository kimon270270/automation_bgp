# importing library
from netmiko import ConnectHandler
from dotenv import load_dotenv
import os

load_dotenv(override=True)
SSH_USERNAME=os.getenv('SSH_USERNAME')
SSH_PASSWORD=os.getenv('SSH_PASSWORD')
ENABLE_SECRET=os.getenv('ENABLE_SECRET')


# connecting to the devices
# list of devices (ip addresses)
devices = [
    {
        "device_type":"arista_eos",
        "host": "172.20.20.2",
        "username":SSH_USERNAME,
        "password":SSH_PASSWORD,
        "secret":ENABLE_SECRET
    },
    {
        "device_type":"arista_eos",
        "host": "172.20.20.3",
        "username":SSH_USERNAME,
        "password":SSH_PASSWORD,
        "secret":ENABLE_SECRET
    },
    {
        "device_type":"arista_eos",
        "host": "172.20.20.4",
        "username":SSH_USERNAME,
        "password":SSH_PASSWORD,
        "secret":ENABLE_SECRET
    },
    {
        "device_type":"arista_eos",
        "host": "172.20.20.5",
        "username":SSH_USERNAME,
        "password":SSH_PASSWORD,
        "secret":ENABLE_SECRET
    },
    {
        "device_type":"arista_eos",
        "host": "172.20.20.6",
        "username":SSH_USERNAME,
        "password":SSH_PASSWORD,
        "secret":ENABLE_SECRET
    },
    {
        "device_type":"arista_eos",
        "host": "172.20.20.7",
        "username":SSH_USERNAME,
        "password":SSH_PASSWORD,
        "secret":ENABLE_SECRET
    },
    {
        "device_type":"arista_eos",
        "host": "172.20.20.8",
        "username":SSH_USERNAME,
        "password":SSH_PASSWORD,
        "secret":ENABLE_SECRET
    },
    {
        "device_type":"arista_eos",
        "host": "172.20.20.9",
        "username":SSH_USERNAME,
        "password":SSH_PASSWORD,
        "secret":ENABLE_SECRET
    },
    {
        "device_type":"arista_eos",
        "host": "172.20.20.10",
        "username":SSH_USERNAME,
        "password":SSH_PASSWORD,
        "secret":ENABLE_SECRET
    },
    {
        "device_type":"arista_eos",
        "host": "172.20.20.11",
        "username":SSH_USERNAME,
        "password":SSH_PASSWORD,
        "secret":ENABLE_SECRET
    }
]

# 1:1 host_name and device maangement ip mapping
# please change depending on management ip address
host_name = ["Edge-Router", "Router4", "Transit-Router", "Router1", "Router3", "Internet", "ISP1", "Router2", "Router5", "ISP2"]


# list of path to yml file
txt_dir = "./device_configs"
txt_paths = os.listdir(txt_dir)

# getting full path
paths = []
for path in txt_paths:
    paths.append(os.path.join(txt_dir, path))

# pushing config to the devices
for i, device in enumerate(devices):
    with ConnectHandler(**device) as connection:
        # privilege escalation
        connection.enable()

        # getting the name of device which we are connecting to at the moment
        device_name = host_name[i]
        
        # getting and loading the config file for the specific device
        for path in paths:
            splitted_path = path.replace("/", ".").split(".")

            if (device_name in splitted_path):
                connection.send_config_from_file(path)
                connection.save_config()

                print(f"{device_name} configured successfully!!\n")
                break
   