# imgview
Simple Py Web Image Viewer

Simple script once pointed to a directory of images will start a webeserver and
will present the array of JPG images in that directory.

Step 1
-------
It's recommended however not absolutly required that you use Miniconda.  Using
Conda allows for better isolation and management of dependencies for developing and
running Python applications.

conda create -n <name>  python
conda activate <name>


Step 2
-------
Install required libraries:
pip install -r requirements.txt


Step 3
-------
Run server by specifying target folder:
python  ./imgview.py -d /mnt/data/pics/20240304

By default this will start a webserver on port 8088 and will present a page
with thumbnails of the images in the specified folder.

http://servername.domain.com:8088

