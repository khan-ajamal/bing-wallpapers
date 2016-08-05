import os,urllib

DIR = os.path.join(os.path.expanduser('~'),'Desktop/Bing Wallpaper/')

#Make a Directory if Bing Wallpaper does not exists
def make_directory():
    if os.path.exists(DIR):
        pass
    else:
        print "Creating a Directory",DIR,'for wallpaper...'
        os.mkdir(DIR)


# Download Wallpaper
def download_file(url):
    file_name = url.split('/')[-1]
    os.chdir(DIR)
    if os.path.isfile(file_name):
        print "Wallpaper", file_name,'already exists..'
    else:
        pic = urllib.urlopen(url)
        with open(file_name,'w') as f:
            f.write(pic.read())
        print file_name,"downloaded..."
        print "Check",DIR
