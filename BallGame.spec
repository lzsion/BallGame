# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['E:\\data\\learn\\pygame\\game_3\\BallGame.py',
            'E:\\data\\learn\\pygame\\game_3\\Board.py',
            'E:\\data\\learn\\pygame\\game_3\\Ball.py',
            'E:\\data\\learn\\pygame\\game_3\\Const.py',
            'E:\\data\\learn\\pygame\\game_3\\Initial.py',
            'E:\\data\\learn\\pygame\\game_3\\Key.py',
            'E:\\data\\learn\\pygame\\game_3\\Display.py'],
             pathex=['E:\\data\\learn\\pygame\\game_3'],
             binaries=[],
             datas=[],
             hiddenimports=['E:\\data\\learn\\pygame\\game_3\\Board.py',
                            'E:\\data\\learn\\pygame\\game_3\\Ball.py',
                            'E:\\data\\learn\\pygame\\game_3\\Const.py',
                            'E:\\data\\learn\\pygame\\game_3\\Initial.py',
                            'E:\\data\\learn\\pygame\\game_3\\Key.py',
                            'E:\\data\\learn\\pygame\\game_3\\Display'],
             hookspath=[],
             hooksconfig={},
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
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='BallGame',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
