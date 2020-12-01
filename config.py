import os
import random

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY") or "".join(
        [chr(random.randint(65, 92)) for _ in range(50)]
    )