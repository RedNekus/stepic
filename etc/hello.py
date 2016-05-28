CONFIG = {
  'mode': 'wsgi',
  'python': '/usr/bin/python3',
  'working_dir': '/media/sf_web',
  'args': (
    '--bind=0.0.0.0:8000',
    '--workers=2',
    '--timeout=15',
    '--log-level=debug',
    'hello:app',
  ),
}