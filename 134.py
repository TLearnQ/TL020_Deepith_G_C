import random
log = []
def api():
    return random.choice(["OK", "FAIL"])

def send_request():
    for i in range(6):
        r = api()
        log.append(f"Try {i+1}: {r}")

        if r == "OK":
            log.append("Finished")
            return "Success"

    log.append("Stopped")
    return "Failed"


print(send_request())
print(log)

