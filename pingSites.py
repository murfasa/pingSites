from icmplib import ping, traceroute

site = input("Enter sites to ping (If more than one, split using commas): ") # Asks user for input
site.replace(" ", "") # Removes spaces from input
sites = site.split(",") # Splits input into a list

if site == "": # If user does not enter anything, it will default to the sites below
  sites = ["murfasa.com", "sakinabox.com", "google.com"]
  print("Defaulting to your hard-coded sites")
  print(sites)


print("1 for Ping")
print("2 for Traceroute")
while True:
  try:
    chooseMethod = int(input("Ping or Traceroute? (1/2): "))
    break
  except:
    print("Please enter a valid option (1 or 2)")


chooseCount = input("Do you want to specify the number of packets to send? (y/n): ") # Asks user for input
packetCount = 4 # Default number of packets to send
if chooseCount == "y" or chooseCount == "Y":
  while True: # Loops until user enters a valid input
    try:
      packetCount = int(input("Enter number of packets to send: ")) # Asks user for input. If input is not an integer, it will throw an error
      break
    except:
      print("Please enter a valid number of packets to send")
elif chooseCount == "n" or chooseCount == "N":
  packetCount = 4
  print("Defaulting to 4 packets")
else:
  print("Please enter a valid option")


def pingSite(domain, packetCount): # Function to ping a site
  print("*"*20)
  print("Pinging " + domain)
  print(ping(domain, packetCount))
  print("*"*20)


def traceSite(domain, packetCount): # Function to trace a site
  print("*"*20)
  print("Tracing " + domain)
  print(traceroute(domain, packetCount))
  print("*"*20)

for domain in sites:
  if chooseMethod == 1:
    pingSite(domain, packetCount)
  elif chooseMethod == 2:
    traceSite(domain, packetCount)
