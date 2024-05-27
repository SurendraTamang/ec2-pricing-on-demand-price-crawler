import requests
import pandas as pd
from datetime import datetime

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://c0.b0.p.awsstatic.com',
    'priority': 'u=1, i',
    'referer': 'https://c0.b0.p.awsstatic.com/',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}


# put the timestamp here
timestamp = datetime.now().timestamp()

params = {
    'timestamp': timestamp,
}


region_name = "US East (Ohio)"
instance_type = "Linux"
region_name_coded = region_name.replace(" ", "%20")

response = requests.get(
    f'https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-ondemand-without-sec-sel/{region_name_coded}/{instance_type}/index.json',
    params=params,
    headers=headers,
)

response_json = response.json()
print(len(response_json.get('regions').get(region_name)))
instances = response_json.get('regions').get(region_name)
instances_list = []
for k_, v_ in instances.items():
    instances_list.append(v_)

df = pd.DataFrame(instances_list)
df.to_csv(f"{region_name}_instances.csv", index=False)