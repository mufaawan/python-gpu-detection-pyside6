Got it! Here's the cleaned-up version of your README without the `.env` setup section:

---

**🚧 Under Development 🚧**

## 🔍 GPU Detection Utility (Script + PySide6 UI)

A sleek, cross-platform GPU detection utility that works both as a command-line script and a desktop UI application built with **PySide6**.
Whether you're using **Windows**, **Linux**, or **macOS** _(experimental)_, this tool helps you identify both **NVIDIA** and **AMD** GPUs effortlessly.

### ✅ Features

- 🚀 Cross-platform support:

  - **Windows**
  - **Linux**
  - **macOS** _(experimental – limited GPU support due to macOS hardware constraints)_

- 🖥️ Detects **both NVIDIA and AMD GPUs**
- 🛠️ Use as either:

  - CLI script for quick diagnostics
  - GUI app for a visual overview

- 📊 Clean and responsive interface built with PySide6

### 🧩 Powered by

- [`GPUUtil`](https://pypi.org/project/gpuutil/)
- [`pyopencl`](https://pypi.org/project/pyopencl/)

---

### ⚙️ Setup Instructions

#### 1. Clone the Repository

```bash
git clone https://github.com/mufaawan/python-gpu-detection-pyside6.git
cd python-gpu-detection-pyside6
```

#### 2. Create a Virtual Environment (Recommended)

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Run the Application

##### 4.1 UI

```bash
python main-ui.py
```

##### 4.1 CLI

```bash
python main-cli.py
```

---

### 📁 Repository

GitHub: [https://github.com/mufaawan/python-gpu-detection-pyside6](https://github.com/mufaawan/python-gpu-detection-pyside6)
