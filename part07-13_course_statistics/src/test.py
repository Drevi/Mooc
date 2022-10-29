import urllib.request

my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")



test = my_request.read()

print(test[0]["week"])