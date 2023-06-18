logurl = "https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/apache_logs/apache_logs"
# from the above apache logs, the exercise is to find the IP adress with the most 404 requests
import urllib.request
import re
import collections


# Read the log file and split into lines
logfile = urllib.request.urlopen(logurl).read().decode("utf8")
lines = logfile.splitlines()


# transform each line into (IP address, status code) pair
def ip_and_code(logline):
    """
    Uses regular expression to extract IP and status code from a logged line
    """
    m = re.match(r'([\d\.]+) .*?".*?" (\d+) ', logline)
    return (m.group(1), m.group(2))


ip_code_pairs = map(ip_and_code, lines)

# keep only those with status code 404
pairs_with_404 = filter(lambda ip_code_pair: ip_code_pair[1] == "404", ip_code_pairs)


# extract the IP address part from each pair
def getIP(pair):
    return pair[0]


ip404 = map(getIP, pairs_with_404)

# count the occurrences, the result is a dictionary of IP addresses map to the count
ip_count = collections.Counter(ip404)


# convert the (IP address, count) tuple into (count, IP address) order
def count_ip(count_item):
    ip, count = count_item
    return (count, ip)


count_ip = map(count_ip, ip_count.items())


# find the tuple with the maximum on the count
print(max(count_ip))
