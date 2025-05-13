import platform

import sys

from detection_utility import get_macos_gpu_info, get_nvidia_info, get_opencl_info

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QPushButton, QScrollArea
)
from PySide6.QtCore import Qt

def detect_gpus():
    gpus = []
    gpus.extend(get_nvidia_info())
    gpus.extend(get_opencl_info())
    gpus.extend(get_macos_gpu_info())

    lines = [f"System: {platform.system()} {platform.architecture()}\n{'='*40}"]
    if gpus:
        for i, gpu in enumerate(gpus, 1):
            lines.append(f"\nGPU #{i}")
            for key, value in gpu.items():
                lines.append(f"  {key}: {value}")
    else:
        lines.append("No GPUs detected.")
    return "\n".join(lines)

class GPUMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GPU Detector")
        self.setMinimumSize(600, 400)

        self.text_edit = QTextEdit(readOnly=True)
        self.button = QPushButton("Detect GPUs")
        self.button.clicked.connect(self.update_gpu_info)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_gpu_info(self):
        result = detect_gpus()
        self.text_edit.setText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GPUMainWindow()
    window.show()
    sys.exit(app.exec())
