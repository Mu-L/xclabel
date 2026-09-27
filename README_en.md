# xclabel

**Language / 语言：** [简体中文](README.md) | [English](README_en.md)

**License:** MIT License, free for commercial use. See `LICENSE` for details.

- Website: https://www.yuturuishi.com
- WeChat: yuturuishi
- Gitee: https://gitee.com/yuturuishi/xclabel
- GitHub: https://github.com/beixiaocai/xclabel

- xclabel is an open-source image annotation and model training tool built with Python + Flask, cross-platform on Windows / Linux / Mac. It supports multiple annotation types, AI-assisted auto-labeling, and the full YOLO training pipeline.

---

## Features

- Annotation: multiple annotation types (rectangle, polygon, etc.); import images, videos, and LabelMe datasets
- AI auto-labeling: large models (LMStudio, vLLM, ollama, Alibaba Cloud) for auto-labeling images and videos
- Model training: full YOLO pipeline — dataset upload, training, resume-from-checkpoint, testing, parameter view and download
- Datasets: export to YOLO format with a customizable train / val / test split
- File management: built-in file manager with browse, upload, and download
- Deployment: all static assets localized, supports offline deployment

---

## Screenshots

<img width="720" alt="1" src="https://raw.giteeusercontent.com/yuturuishi/images/raw/master/xclabel/v3.0/1.png">
<img width="720" alt="2" src="https://raw.giteeusercontent.com/yuturuishi/images/raw/master/xclabel/v3.0/2.png">
<img width="720" alt="3" src="https://raw.giteeusercontent.com/yuturuishi/images/raw/master/xclabel/v3.0/3.png">
<img width="720" alt="4" src="https://raw.giteeusercontent.com/yuturuishi/images/raw/master/xclabel/v3.0/4.png">
<img width="720" alt="5" src="https://raw.giteeusercontent.com/yuturuishi/images/raw/master/xclabel/v3.0/5.png">
<img width="720" alt="6" src="https://raw.giteeusercontent.com/yuturuishi/images/raw/master/xclabel/v3.0/6.png">

---

## Requirements

- Python 3.8+
- Dependencies in `requirements.txt`
- Training requires Ultralytics / PyTorch (CPU or CUDA build)
- A modern web browser

---

## Quick Start

```bash
# Create and activate a virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate

# Install base dependencies
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

Start the server:

```bash
python app.py --host 0.0.0.0 --port 9924
```

Open `http://127.0.0.1:9924` in your browser.

---

## Usage

1. **Install dependencies**: see Quick Start. Training requires additional installs:
   ```bash
   pip install ultralytics==8.3.1 -i https://pypi.tuna.tsinghua.edu.cn/simple
   pip install numpy==1.26.4 -i https://pypi.tuna.tsinghua.edu.cn/simple
   # CPU build of torch
   pip install torch==2.1.2 torchvision==0.16.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
   # CUDA build of torch
   pip install torch==2.1.0 torchaudio==2.1.0 torchvision==0.16.0 --index-url https://download.pytorch.org/whl/cu121
   ```
2. **Start server**: `python app.py --host 0.0.0.0 --port 9924`
3. **Open**: browser to http://127.0.0.1:9924
4. **Training**: visit http://127.0.0.1:9924/training — upload dataset → choose model → start training → test / download

---

## Project Structure

```
xclabel/
├── app.py                    # Main application
├── AiUtils.py                # AI auto-labeling utility class
├── requirements.txt          # Dependency list
├── static/                   # Static assets (icons, styles, scripts, local Socket.IO)
├── templates/                # Page templates
│   ├── index.html            # Annotation home
│   ├── training.html         # Training panel
│   ├── ai_config.html        # AI configuration
│   └── file_manager.html     # File manager
├── pre_models/               # Pretrained models (.pt files)
├── uploads/                  # Upload storage (created at runtime)
│   ├── annotations/          # Annotation data
│   ├── config/               # Config files
│   ├── samples/              # Annotation images
│   └── training_datasets/    # Training datasets
├── runs/                     # Training output (created at runtime)
└── tmp/                      # Training temp files (created at runtime)
```

---

## Shortcuts

- **Ctrl+S**: save annotations
- **Ctrl+Shift+D**: clear annotations

---

## Tech Stack

Flask + Flask-SocketIO | HTML/CSS/JS | OpenCV/PIL | Ultralytics YOLO11 | Socket.IO

---

## Changelog

Full changelog: [CHANGELOG.md](CHANGELOG.md)

---

## License

The project's own code is released under the MIT License; keep the copyright notice to use it freely. Third-party libraries are subject to their respective licenses.
