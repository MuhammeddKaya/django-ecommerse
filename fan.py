import os
import psutil
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSlider, QVBoxLayout
from PyQt5.QtCore import Qt

class FanController(QWidget):
    def __init__(self):
        super().__init__()

        # Fan kontrolünü etkinleştir
        os.system('sudo sensors-config --fan-ctrl 1')

        # Fan hızını oku
        sensors_data = psutil.sensors_fans()
        self.fan_speed = sensors_data[0][1]

        # Arayüz bileşenlerini oluştur
        self.title = QLabel('Fan Kontrolü')
        self.speed_label = QLabel(f'Hız: {self.fan_speed} RPM')
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(self.fan_speed)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(10)
        self.slider.valueChanged.connect(self.set_fan_speed)

        # Arayüzü düzenle
        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.speed_label)
        layout.addWidget(self.slider)
        self.setLayout(layout)

        # Arayüzü göster
        self.show()

    def set_fan_speed(self, value):
        # Fan hızını ayarla
        os.system(f'sudo fancontrol --set-fan1 {value}')

        # Yeni fan hızını oku
        sensors_data = psutil.sensors_fans()
        self.fan_speed = sensors_data[0][1]

        # Hızı güncelle
        self.speed_label.setText(f'Hız: {self.fan_speed} RPM')

if __name__ == '__main__':
    app = QApplication([])
    fan_controller = FanController()
    app.exec_()
