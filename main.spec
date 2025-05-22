# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('BLACK.png', '.'),
        ('BLUE.png', '.'),
        ('GREEN.png', '.'),
        ('RED.png', '.'),
        ('WHITE.png', '.'),
        ('YELLOW.png', '.'),
        ('cat face.png', '.'),
        ('compass icon.png', '.'),
        ('Квадрат.png', '.'),
        ('Линия.png', '.'),
        ('Овал.png', '.'),
        ('Параллелепипед.png', '.'),
        ('Треугольник.png', '.')
    ],
    hiddenimports=['PIL.ImageTk', 'tkinter'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='PHE',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
