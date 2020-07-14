from pathlib import Path
path = Path ("ecommerce")
print(path.exists())

from pathlib import Path
path = Path ("ecommerce")
print(path.mkdir())

from pathlib import Path
path = Path ("ecommerce")
print(path.rmdir())

from pathlib import Path
path = Path ("ecommerce")
print(path.glob("*.py"))
