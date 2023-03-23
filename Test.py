import urllib2  # the lib that handles the url stuff

target_url = 'https://drive.google.com/file/d/1b61o6TG2-fvS-V3jHRxMfR2WvaYR_Ez3/view?usp=share_link'
data = urllib2.urlopen(target_url) # it's a file like object and works just like a file
for line in data: # files are iterable
    print line