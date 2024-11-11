import os
import sys
import PIL
from os import listdir
from os.path import isfile, join
from flask import Flask,render_template,request,send_from_directory
import argparse
from PIL import Image

os.makedirs("./templates",exist_ok=True)
os.makedirs("./static/images",exist_ok=True)

parser = argparse.ArgumentParser()
parser.add_argument('-d',help='Directory to use',default="/data/bik/train/2010/2010-10-30")
parser.add_argument('-p',default=8088)
args = parser.parse_args()

print(args)
port = args.p
dirpath = args.d

pathIds = [ dirpath+'/'+f for f in listdir(dirpath) if isfile(join(dirpath, f)) and f.upper().endswith('JPG') ]
fileNames= [ f for f in listdir(dirpath) if isfile(join(dirpath, f)) and f.upper().endswith('JPG') ]

def generateThumbnail(filePath):
	im = Image.open(filePath)
	im.thumbnail((120,120))
	thumbFilename = 'thumb_'+filePath.replace('/','%')
	im.save('./static/images/'+thumbFilename)
	return thumbFilename

thumbFileNames = []
for f in pathIds:
	print(f"Generate thumbnail for {f}")
	thumbFileNames.append(generateThumbnail(f))

app = Flask(__name__)

@app.route('/')
def imgview():
    return render_template('index.html',pathIds=pathIds,fileNames=fileNames,currentImage=currentImage,thumbFileNames=thumbFileNames,dirpath=dirpath)

@app.route('/image',methods=['GET','POST'])
def get_image():
    filePath = request.args.get('id')
    print(f"File requested: {filePath}")
    return send_from_directory(dirpath,filePath,as_attachment=True)

if __name__ == '__main__':

	# just set initial image
	currentImage = fileNames[0]

	app.run(host="0.0.0.0", port=port, debug=True)

