# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['E:\\data\\learn\\pygame\\BallGame\\main.py',
            'E:\\data\\learn\\pygame\\BallGame\\Ball.py',
            'E:\\data\\learn\\pygame\\BallGame\\BallGame.py',
            'E:\\data\\learn\\pygame\\BallGame\\Board.py',
            'E:\\data\\learn\\pygame\\BallGame\\Const.py',
            'E:\\data\\learn\\pygame\\BallGame\\Display.py',
            'E:\\data\\learn\\pygame\\BallGame\\Initial.py',
            'E:\\data\\learn\\pygame\\BallGame\\Key.py',
            'E:\\data\\learn\\pygame\\BallGame\\SelectPlayer.py'],
             pathex=['E:\\data\\learn\\pygame\\BallGame'],
             binaries=[],
             datas=[('E:\\data\\learn\\pygame\\BallGame\\font','font')],
             hiddenimports=[
                'E:\\data\\learn\\pygame\\BallGame\\Ball.py',
                'E:\\data\\learn\\pygame\\BallGame\\BallGame.py',
                'E:\\data\\learn\\pygame\\BallGame\\Board.py',
                'E:\\data\\learn\\pygame\\BallGame\\Const.py',
                'E:\\data\\learn\\pygame\\BallGame\\Display.py',
                'E:\\data\\learn\\pygame\\BallGame\\Initial.py',
                'E:\\data\\learn\\pygame\\BallGame\\Key.py',
                'E:\\data\\learn\\pygame\\BallGame\\SelectPlayer.py'],
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
          [],
          exclude_binaries=True,
          name='BallGame',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
