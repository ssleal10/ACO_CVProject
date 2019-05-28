import urllib.request

print('Beginning file download with urllib2...')

url = 'https://www.dropbox.com/s/qqwi0df9g90bsmc/imagesxc.zip?dl=1'  
urllib.request.urlretrieve(url, '/home/ssleal10/ACO/syndata-generation/imagesxc.zip') 