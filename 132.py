config = {"TunnelName": "OfficeVPN", "Region": "India","IdentificationCode":431,"Subscription":True}

clean = {}

for k, v in config.items():
    clean[k.lower()] = v

print(clean)

