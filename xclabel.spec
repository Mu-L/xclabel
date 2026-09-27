# -*- mode: python ; coding: utf-8 -*-
# PyInstaller 打包配置：仅视频标注核心功能，不打包 ultralytics/torch

block_cipher = None

# 只读资源：打进 exe 内部，运行时从 _MEIPASS 读取
datas = [
    ('templates', 'templates'),
    ('static', 'static'),
    ('pre_models', 'pre_models'),
]

# 动态导入的依赖，PyInstaller 静态分析容易漏掉，显式声明
hiddenimports = [
    'flask_socketio',
    'simple_websocket',
    'engineio.async_drivers.threading',
    'socketio.async_drivers.threading',
    'flask_cors',
    'engineio',
    'socketio',
]

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    runtimehooks=[],
    # 明确排除训练相关重型依赖，防止意外打入导致 exe 巨大
    excludes=['ultralytics', 'torch', 'torchvision', 'matplotlib', 'pandas', 'scipy', 'tqdm', 'yaml'],
    noarchive=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='xclabel',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    # 保留控制台窗口：用户双击 exe 能看到服务器运行日志和访问地址
    console=True,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
