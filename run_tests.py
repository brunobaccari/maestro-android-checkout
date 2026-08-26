import os
from pathlib import Path
import shutil
import subprocess
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    for name in ['MAESTRO_APP_ID', 'MAESTRO_TEST_USER', 'MAESTRO_TEST_PASSWORD', 'MAESTRO_LOCKED_USER']:
        if not os.environ.get(name):
            raise SystemExit(f'Configure {name} em .env ou no ambiente')
    executable = shutil.which('maestro')
    if not executable:
        raise SystemExit('Maestro CLI não encontrado no PATH')
    Path('results').mkdir(exist_ok=True)
    raise SystemExit(subprocess.run([executable, 'test', '--format', 'junit', '--output',
                                    'results/junit.xml', '--test-output-dir', 'results', 'flows']).returncode)
