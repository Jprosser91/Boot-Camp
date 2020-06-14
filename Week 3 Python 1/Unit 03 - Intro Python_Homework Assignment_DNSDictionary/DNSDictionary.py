# Here is a list of providers
providers = ["Level3", "Verisign", "Google", "Quad9", "DNS.WATCH",
             "Comodo Secure DNS", "OpenDNS Home", "Norton ConnectSafe",
             "GreenTeamDNS", "SafeDNS", "OpenNIC", "SmartViper", "Dyn",
             "FreeDNS", "Alternate DNS", "Yandex.DNS", "UncensoredDNS",
             "Hurricane Electric", "puntCAT", "Neustar", "Cloudflare",
             "Fourth Estate"]
# Here is a list of ip's
ips = ["209.244.0.3", "64.6.64.6", "8.8.8.8", "9.9.9.9", "84.200.69.80",
       "8.26.56.26", "208.67.222.222", "199.85.126.10", "81.218.119.11",
       "195.46.39.39", "69.195.152.204", "208.76.50.50", "216.146.35.35",
       "37.235.1.174", "198.101.242.72", "77.88.8.8", "91.239.100.100",
       "74.82.42.42", "109.69.8.51", "156.154.70.1", "1.1.1.1", "45.77.165.194"]


####################################
### Part 1 - Provider Dictionary ###
####################################
# Print ----------PART 1!!! to help seperate the outputs
print ("--------PART 1!!!--------")
# Create a new dictionary called DNS_dictionary
DNS_dictionary = {}

# Use a for loop to create a dictionary mapping the provider names to their IPs. expected output: {'Level3': '209.244.0.3', ...}
# Set DNS_dictionary equal to provider:ip with a for loop of provider, ip inside of the providers, ips lists using the zip command
DNS_dictionary = {provider:ip for provider,ip in zip(providers, ips)}
# Print "Dns Dictionary:" followed by the DNS_dictionary and then seperate that entry with "-------------""
print("DNS Dictionary: ", DNS_dictionary) 
print("--------")

# Use the dictionary to print Hurricane Electric's IP
# Set data equal to DNS_dictionary["Hurricane Electric"] to pull the IP Address attached to that entry
data = DNS_dictionary["Hurricane Electric"]
#print "Hurricane Electic's IP is: " + the IPaddress that we just got from data and then seperate that entry with "----------"
print("Hurricane Electric's IP is: " + data)
print("--------")

##################################
### Part 2 - List of Providers ###
##################################
# Print ----------PART 2!!! to help seperate the outputs
print ("--------PART 2!!!--------")
# Create a list called DNS_dictionaries where we can nest dictionaries into a list
DNS_dictionaries = []

# Use a for loop to create a list of dictionaries with the associated information. expected output: [{'provider_name': 'Level3', 'primary_server': '209.244.0.3'}, ...]
# Create a for loop of provider, ip inside of the providers, ips lists using the zip command
for provider, ip in zip(providers,ips):
       #Extrend DNS_Dictionaries with {"Provider name" : provider} and {"Primary server" : ip} to store all the data into the correct position
       DNS_dictionaries.extend([{"Provider name": provider} , {"Primary server" : ip}])
#Print "DNS Dictionary: " and the DNS Dictionaries and then seperate that entry with "------------"
print("DNS Dictionary: ", DNS_dictionaries)
print("--------")

# Use the list to print the total number of providers
# print "Number of providers: " with the lengh of the providers list (I am trying to figure out how to pull the provider info from DNS_dictionaries)
print("Number of providers: " , len(providers))
# Print ----------END!!!-------- to signify the end of the code
print ("--------END!!!--------")
# End of code