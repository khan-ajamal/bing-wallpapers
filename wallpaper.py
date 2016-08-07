import os,urllib

DIR = os.path.join(os.path.expanduser('~'),'Pictures/Bing Wallpaper/')
wallpapers = []
#Make a Directory if Bing Wallpaper does not exists
def make_directory():
    if os.path.exists(DIR):
        pass
    else:
        print "Creating a Directory",DIR,'for wallpaper...'
        os.mkdir(DIR)

#Make list of all wallpapers
def make_list():
    os.chdir(DIR)
    if os.path.isfile('list_of_wallpaper.txt'):
        pass
    else:
        ls = os.listdir(DIR)
        for i in ls:
            if i.startswith("."):
                continue
            else:
                a = i.split("_")
                wallpapers.append(a[0])
        f = open("list_of_wallpaper.txt",'w')
        for w in wallpapers:
            f.write(w+' ')
        f.close()

def appendToList(image):
    with open('list_of_wallpaper.txt','a') as f:
        f.write(image+' ')


def check_list(name):
    with open('list_of_wallpaper.txt','r') as f:
        l = f.read().split()
    if name in l:
        return True
    return False


# Download Wallpaper
def download_file(url):
    file_name = url.split('/')[-1]
    image = file_name.split("_")[0]

    print "Accessing Archieve..."
    #Check wheather the wallpaper already in Bing Wallpaper Directory
    if check_list(image):
        return 0

    #appending to List
    appendToList(image)

    os.chdir(DIR)
    print "Downloading...."
    pic = urllib.urlopen(url)
    with open(file_name,'w') as f:
        f.write(pic.read())
    print file_name,'downloaded.'
    return 1
