import urllib,json,sys
import wallpaper as w

MARKET = ['IN','US','AU','NZ','CN','GB','ZA']

# Retrive url of image from JSON
def find_image_url():
    for market in MARKET:
        for n in range(0,9):
            JSON_LINK = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n="+str(n+1)+"&mkt=en-"+market
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
                w.download_file(url)

            except Exception as e:
                print str(e)

if __name__ == '__main__':
    w.make_list()
    w.make_directory()
    find_image_url()
