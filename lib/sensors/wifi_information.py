import subprocess

def get_internet_connection_info():
    try:
        iwconfig_output = subprocess.check_output(["iwconfig"]).decode("utf-8")

        if "ESSID" in iwconfig_output:
            wifi_name = iwconfig_output.split("ESSID:")[1].split('"')[1]
            signal_strength = iwconfig_output.split("Signal level=")[1].split("dBm")[0]
            status = {"WiFi 명": wifi_name, "신호 강도(dBm)": signal_strength}
            return status
        else:
            status = {"WiFi 명": "LAN_Connection", "신호 강도(dBm)": 0}
            return status

    except subprocess.CalledProcessError:
        return "Error Appeared."