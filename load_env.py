import os
import ast
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

PORT = ast.literal_eval(os.environ.get('PORT', 8000))
