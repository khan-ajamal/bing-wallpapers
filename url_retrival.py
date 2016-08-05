import urllib,json,sys
import save_wallpaper as sw

# Retrive url of image from JSON
def find_image_url():
    JSON_LINK = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=8&mkt=en-IN"
    try:
        data = urllib.urlopen(JSON_LINK)
        json_data = json.load(data)
        if "images" in json_data:
            images = json_data["images"]
        else:
            sys.exit('JSON error. Please try again later....')
        print('Downloading...')
        for i in range(len(images)):
            url = 'http://www.bing.com' + images[i]['url']
        sw.download_file(url)

    except Exception as e:
        print str(e)

if __name__ == '__main__':
    sw.make_directory()
    find_image_url()
