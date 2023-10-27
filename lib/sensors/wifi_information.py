import subprocess

def get_internet_connection_info():
    try:
        iwconfig_output = subprocess.check_output(["iwconfig"]).decode("utf-8")

        if "ESSID" in iwconfig_output:
            wifi_name = iwconfig_output.split("ESSID:")[1].split('"')[1]
            signal_strength = iwconfig_output.split("Signal level=")[1].split("dBm")[0]
            status = {"name": wifi_name, "dB": signal_strength}
            return status
        else:
            status = {"name": "LAN_Connection", "dB": 0}
            return status

    except:
        status = {"name": "can't find", "dB": 0}
        return status
