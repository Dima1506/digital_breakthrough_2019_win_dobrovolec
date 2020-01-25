from subprocess import PIPE, Popen
import os, os.path
from moviepy.editor import *
from moviepy.video.tools.drawing import color_split
from PIL import Image
from gtts import gTTS
from googletrans import Translator
from random import choice
translator = Translator()

imgs = []
path = "./photos"
valid_images = [".jpg"]
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        continue
    imgs.append(path+'/'+f)
texts = []
snd = AudioFileClip("snd.wav")
clips = [VideoFileClip('compas.mp4').subclip(0,snd.duration).set_audio(snd)]
tts = gTTS(text='Добрейший вечерочек, сегодня я сделала подборку историй обычных людей которые меняют этот мир к лучшему', lang='ru')
tts.save('good.mp3')
snd = AudioFileClip("good.mp3")
clips.append(VideoFileClip('start.mp4').subclip(0,snd.duration).set_audio(snd))
max_razm = 0
razm = []

phrases = ['На первой картинке мы можем видеть ', 'На второй картинке ']
rand = ['Здесь мы видим ','Тут ', 'Ну просто офигеть, вы посмотрите ', 'Как же я люблю бтс, вот они справа налево. А нет. Это другая фотография ']
finish = [' Пожелаем удачи', ' этот нигер даже не представляет насколько он крут', ' рил ток', ' просто пушка', ' велкам ту зе клаб, бади']

cnt = 0
for x in imgs:
    p = Popen(['curl','-X','POST',"http://max-image-caption-generator.max.us-south.containers.appdomain.cloud/model/predict",'-H',"accept: application/json",'-H',"Content-Type: multipart/form-data",'-F',"image=@"+x+";type=image/jpg"],stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate(b"input data that is passed to subprocess' stdin") 
    im = Image.open(x)
    width, height = im.size
    if width+height > max_razm:
        max_razm = width+height
        razm = [height,width]
    texts.append(eval(output)['predictions'][0]['caption'])
    if cnt < 2:
        tts = gTTS(text=phrases[cnt]+translator.translate(eval(output)['predictions'][0]['caption'],dest='ru').text, lang='ru')
    else:
        tts = gTTS(text=choice(rand)+translator.translate(eval(output)['predictions'][0]['caption'],dest='ru').text+choice(finish), lang='ru')
    tts.save('good.mp3')
    snd = AudioFileClip("good.mp3").set_start(1)
    clip = ImageClip(x).set_duration(snd.duration+2).resize(height=720,width=480).set_audio(snd)
    clips.append(clip)
    cnt += 1

tts = gTTS(text=' Давайте пожелаем удачи всем участникам нашего обзора. Ставьте каналы, подписывайтесь на лайк', lang='ru')
tts.save('good.mp3')
snd = AudioFileClip("good.mp3")
clips.append(VideoFileClip('finish.mp4').subclip(0,snd.duration).set_audio(snd))

print(texts)
final_clip = concatenate_videoclips(clips,method='compose')
final_clip.write_videofile("my_concatenation.mp4",fps=24)
#505d11ee-e5ee-4c11-b0a9-e551748e9f5f
#curl -F 'text=Today I clean the national park of the town where I live' -H 'api-key:505d11ee-e5ee-4c11-b0a9-e551748e9f5f' https://api.deepai.org/api/text-generator 