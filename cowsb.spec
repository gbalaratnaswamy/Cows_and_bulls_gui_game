# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['cowsb.py'],
             pathex=['C:\\Users\\gangi\\PycharmProjects\\desktopapp'],
             binaries=[],
             datas=[('Cows and bulls.ico', '.'),('fullmatrix.txt', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Cows and Bulls',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          icon='Cows and bulls.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='cowsb')
