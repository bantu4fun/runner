# -*- mode: python -*-
a = Analysis(['run.py'],
             pathex=['F:\\python\\simpleApp\\runner'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Runner.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )
