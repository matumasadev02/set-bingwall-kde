import json
import requests
import os
from PIL import Image
import io


def main():

    data = json.loads(requests.get(
        'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1').text)

    img_url = 'https://www.bing.com{}'.format(data.get('images')[0].get('url'))

    img_name = data.get('images')[0].get('title') + '.jpg'

    current_dir = os.path.dirname(os.path.abspath(__file__))

    img_path = os.path.join(current_dir, 'images', img_name)

    if os.path.exists(os.path.join(current_dir, 'images')):
        pass
    else:
        os.mkdir(os.path.join(current_dir, 'images'))

    if os.path.exists(img_path):
        pass

    else:
        img = Image.open(io.BytesIO(requests.get(img_url).content))
        img.save(img_path)

    print(img_url + ' was saved as ' + img_path)

    os.system(
        'qdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript \'var allDesktops = desktops();print (allDesktops);for (i=0;i<allDesktops.length;i++) {d = allDesktops[i];d.wallpaperPlugin = \"org.kde.image\";d.currentConfigGroup = Array(\"Wallpaper\", \"org.kde.image\", \"General\");d.writeConfig(\"Image\", \"' + img_path + '\")}\'')

    print(
        'qdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript \'var allDesktops = desktops();print (allDesktops);for (i=0;i<allDesktops.length;i++) {d = allDesktops[i];d.wallpaperPlugin = \"org.kde.image\";d.currentConfigGroup = Array(\"Wallpaper\", \"org.kde.image\", \"General\");d.writeConfig(\"Image\", \"' + img_path + '\")}\'')


if __name__ == '__main__':
    main()
