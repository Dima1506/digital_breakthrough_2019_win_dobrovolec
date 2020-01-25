from auth import authenticate
import time
from instabot import Bot
import os

from datetime import datetime

client = authenticate()
album = None # You can also enter an album ID here
bot = Bot()
bot.login(username='dmitryichyotkin', password='cxzaq15061999')

def upload_kitten(client,image_path):
	config = {
		'album': album,
		'name':  'ok',
		'title': 'ok',
		'description': 'Cute kitten being cute on {0}'.format(datetime.now())
	}

	image = client.upload_from_path(image_path, config=config, anon=False)

	return image


# If you want to run this as a standalone script
if __name__ == "__main__":
	while 1:
		medias = bot.get_total_hashtag_medias('dobronews2019', amount=4, filtration=False)
		print(medias)
		bot.download_photos(medias)

		f = open('data2.txt','r')
		imgs = eval(f.read())
		f.close()
		path = "./photos"
		valid_images = [".jpg"]
		f = open('data3.txt','r')
		data = eval(f.read())
		f.close()
		cnt = 0
		for f in os.listdir(path):
			ext = os.path.splitext(f)[1]
			if ext.lower() not in valid_images:
				continue
			if f not in data:
				image = upload_kitten(client,path+'/'+f)
				imgs.append(image['link'])
				data.append(f)
			cnt += 1
		print(imgs)
		f = open('data3.txt','w')
		f.write(str(data))
		f.close()
		f = open('data2.txt','w')
		f.write(str(imgs))
		f.close()
		time.sleep(30)
#https://api.imgur.com/oauth2/authorize?client_id=7a6e8b6f5d26e41&response_type=pin

