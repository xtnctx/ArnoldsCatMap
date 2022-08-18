"""
   Copyright 2022 Ryan Christopher D. Bahillo

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

"""

from PyQt5 import QtGui, QtWidgets
from GUI import Ui_MainWindow
from natsort import natsorted
from threading import Thread
from PIL import Image
from utils import *
import subprocess
import winsound
import sys, os
import shutil


images_path = 'data/'

class Window(Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.images_path = 'data/'
        self.temp_img = 'selected_image.png'

        if not os.path.isdir(self.images_path): # checks if the dir exists
            os.mkdir(self.images_path)
        
        self.arnold_cats = list()
        self.selected_image = ''

        self.iteration = 0

        self.horizontalSlider.valueChanged.connect(self.show_cats)
        self.actionOpen_image.triggered.connect(self.set_img)
        self.actionOpen_pdf.triggered.connect(self.open_pdf)
        self.start.clicked.connect(self.start_ACM)
        self.next.clicked.connect(self.next_img)
        self.prev.clicked.connect(self.prev_img)
    
    def cattify(self, input_img):

        file_name = os.path.basename(input_img)
        img = Image.open(input_img)

        img = self.resize_img(img)

        namex = os.path.splitext(file_name)[0]

        img.save(self.images_path + f'ACM-{namex}-0.png')

        done = False
        while not done:
            canvas = Image.new(img.mode, (img.width, img.height))
            for x in range(canvas.width):
                for y in range(canvas.height):
                    nx = (2 * x + y) % canvas.width
                    ny = (x + y) % canvas.height

                    canvas.putpixel((nx, canvas.height-ny-1), img.getpixel((x, canvas.height-y-1)))
            self.iteration += 1

            new_image = self.images_path + f'ACM-{namex}-{self.iteration}.png'
            canvas.save(new_image)
            img = Image.open(new_image)
            
            
            if images_the_same(self.images_path + f'ACM-{namex}-0.png', new_image):
                done = True

        self.arnold_cats = natsorted(self.get_cat_list(self.images_path))

        self.horizontalSlider.setMaximum(len(self.arnold_cats)-1)
        
        
    def getFileDir(self):
        file_filter = "Images (*.png *.jpg)"
        return QtWidgets.QFileDialog.getOpenFileName(
            parent = QtWidgets.QWidget(),
            caption = 'Select an image',
            directory = os.getcwd() + '/SAMPLE_IMAGES',
            filter = file_filter)[0]

    def get_cat_list(self, path) -> list:
        return os.listdir(path)
    
    def show_cats(self, value):
        self.iter_text.setText(f'Iter = {value}')
        self.image.setPixmap(QtGui.QPixmap(self.images_path + self.arnold_cats[value]))
        self.statusBar.clearMessage()

    def resize_img(self, img) -> Image:
        min_size = min(img.size)
        imageBoxSize = 200 # maximum width of image placeholder

        if min_size >= imageBoxSize:
            resized_im = img.resize((imageBoxSize,imageBoxSize)) # arnold's cat map must be square
        else:
            resized_im = img.resize((min_size,min_size))
        
        return resized_im
    
    def set_img(self):
        x = self.getFileDir()
        if x != '':
            self.selected_image = x
        if self.selected_image != '':
            img = self.resize_img(Image.open(self.selected_image))
            img.save(self.temp_img)

            self.image.setPixmap(QtGui.QPixmap(self.temp_img))

            self.start.setEnabled(True)
    
    def open_pdf(self):
        file = "document.pdf"
        subprocess.Popen([file], shell=True)

    def func(self):
        self.setFocus()
        self.start.setDisabled(True)

        self.reset()

        self.statusBar.showMessage('Cattifying image, please wait ...')
        self.progressBar.show()

        self.cattify(self.selected_image)
        
        self.statusBar.showMessage('Done!')

        self.progressBar.hide()
        os.remove(self.temp_img)

        self.prev.setEnabled(True)
        self.next.setEnabled(True)
        self.horizontalSlider.setEnabled(True)
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

    def start_ACM(self):
        self.process = Thread(target=self.func)
        self.process.start()

    def reset(self):
        self.iteration = 0

        dir = self.images_path
        for files in os.listdir(dir):
            path = os.path.join(dir, files)
            try:
                shutil.rmtree(path)
            except OSError:
                os.remove(path)
    
    def next_img(self):
        self.horizontalSlider.setValue(self.horizontalSlider.value()+1)

    def prev_img(self):
        self.horizontalSlider.setValue(self.horizontalSlider.value()-1)
    
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())
