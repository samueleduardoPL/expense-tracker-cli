from pathlib import Path
import json
from collections import defaultdict


def idgenerator(path : Path) -> int:
    """
    Generate and persist an incremental ID.

    If the file does not exist or is empty, it is initialized with currentid = 1.
    Otherwise, the stored ID is incremented and saved back to the file.

    Args:
        path: Path to the file used to store the current ID.

    Returns:
        int: The newly generated ID.

    Raises:
        ValueError: If the ID storage file is corrupted.
    """
    
    try:
        if not path.exists() or path.stat().st_size == 0:
            with open(path, "w") as f:
                newId = {"currentid" : 1}
                json.dump(newId, f)

            return newId["currentid"]
        else:
            with open(path) as f:
                nextId = json.load(f)

            nextId["currentid"] += 1

            with open(path, "w") as f:
                json.dump(nextId, f)

            return nextId["currentid"]
    except json.JSONDecodeError:
        raise ValueError(f"Your id storage file '{path}' is corrupted")

    



        
    
    
