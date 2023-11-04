import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QTextEdit, QWidget
from gtts import gTTS
# import PyPDF


class PdfToAudioConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('PDF to Audio Converter')
        self.setGeometry(100, 100, 600, 400)

        self.text_edit = QTextEdit(self)
        self.text_edit.setPlaceholderText('Paste or type your text here')
        
        self.convert_button = QPushButton('Convert to Audio', self)
        self.convert_button.clicked.connect(self.convert_to_audio)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.convert_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def convert_to_audio(self):
        text = self.text_edit.toPlainText()
        if text:
            tts = gTTS(text)
            tts.save('output.mp3')
            print('Conversion completed. Saved as "output.mp3".')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PdfToAudioConverter()
    window.show()
    sys.exit(app.exec_())
