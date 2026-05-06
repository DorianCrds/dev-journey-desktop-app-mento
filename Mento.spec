# Mento.spec
# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

project_root = Path.cwd()

block_cipher = None


a = Analysis(
    ["run_mento.py"],
    pathex=[str(project_root)],
    binaries=[],
    datas=[
        ("qute/themes", "qute/themes"),
        ("qute/styles", "qute/styles"),
        ("qute/assets/fonts", "qute/assets/fonts"),
        ("assets", "assets"),
        ("database", "database"),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher,
)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="Mento",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon="assets/logo/brain.ico",
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="Mento",
)