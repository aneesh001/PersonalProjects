import sys
import time
from datetime import datetime as dt

hosts_temp = r"hosts"
hosts_path = r"/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

def blocker():
	while True:
		start = dt(dt.now().year, dt.now().month, dt.now().day, 12)
		end = dt(dt.now().year, dt.now().month, dt.now().day, 14)

		if start > end:
			print("Invalid time range.")
			sys.exit(0)

		if start < dt.now() < end:
			print("blocked")
			with open(hosts_temp, "r+") as hfile:
				content = hfile.read()

				for website in website_list:
					if website not in content:
						hfile.write(redirect + " " + website + "\n")
		else:
			print("unblocked")
			with open(hosts_temp, "r+") as hfile:
				content = hfile.readlines()

				hfile.seek(0)
				
				for line in content:
					if not any(website in line for website in website_list):
						hfile.write(line)

				hfile.truncate()

		time.sleep(5)

if __name__ == "__main__":
	blocker()
