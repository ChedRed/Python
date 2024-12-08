from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QFileDialog, QWidget
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QEvent

class ImageViewer(QMainWindow):
  def __init__(self):
    super().__init__()
    self.image_path = None
    self.open_image_dialog()

  def setup_ui(self):
    self.setWindowTitle("Image Viewer")
    self.layout = QVBoxLayout()

    self.image_label = QLabel()
    self.image_label.setFixedSize(400, 400)  # Adjust size as needed
    self.image_label.installEventFilter(self)  # Install event filter
    self.layout.addWidget(self.image_label)

    self.setCentralWidget(QWidget(self))
    self.centralWidget().setLayout(self.layout)

  def open_image_dialog(self):
    self.image_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg)")
    if self.image_path:
      self.setup_ui()
      self.image_label.setPixmap(QPixmap(self.image_path))
      self.show()

  def eventFilter(self, obj, event):
    if obj is self.image_label and event.type() == Qt.MouseEventSource.:  # Corrected event type
      if event.button() == Qt.LeftButton:  # Check for left click only
        self.save_image_dialog()
    return super().eventFilter(obj, event)

  def save_image_dialog(self):
    if not self.image_path:
      return  # No image loaded

    save_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "Image Files (*.png *.jpg *.jpeg)")
    if save_path:
      self.image_label.pixmap().save(save_path)  # Save the displayed image

if __name__ == "__main__":
  app = QApplication([])
  window = ImageViewer()
  app.exec()
