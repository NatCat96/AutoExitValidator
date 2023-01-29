import subprocess
import requests
from datetime import datetime, timedelta

days = int("60")

def parse_version(string):
    return string.split("/v")[1].split("/")[0].split("+")[0]

def get_release_date(version):
    #change if not using Teku for consensus client
    response = requests.get(f'https://api.github.com/repos/PegaSysEng/teku/releases/tags/{version}')
    if response.status_code == 200:
        release = response.json()
        return release['published_at'][:10]
    else:
        return None

def get_local_version():
    #update path to consensus client binary
    result = subprocess.run(['/usr/bin/teku/bin/teku', '--version'], stdout=subprocess.PIPE)
    return parse_version(result.stdout.decode().strip())

def get_latest_release_date():
    #change if not using Teku for consensus client
    response = requests.get('https://api.github.com/repos/PegaSysEng/teku/releases/latest')
    latest_release = response.json()
    return datetime.strptime(latest_release['published_at'][:10], "%Y-%m-%d")

print("{}".format(get_local_version()))

local_release_date = datetime.strptime(get_release_date(get_local_version()), "%Y-%m-%d")
latest_release_date = get_latest_release_date()

print("{} local release date".format(local_release_date))
print("{} latest release date".format(latest_release_date))

if local_release_date < latest_release_date - timedelta(days=days):
    print("Your version is more than {} days old. Exiting Validators".format(days))
    #update path to exitedEmail script
    subprocess.run(["/usr/bin/python3.10", "~/exitedEmail.py"])
elif local_release_date == latest_release_date - timedelta(days=0):
    print("You're running the latest version")
else:
    difference_in_days = (latest_release_date - local_release_date).days
    #update path to warningEmail script
    subprocess.run(["/usr/bin/python3.10", "~/warningEmail.py", "-d {}".format(days - difference_in_days), "-s Consensus"])
    print("Your local version is {} days old".format(difference_in_days))
