import json
from pathlib import Path
from typing import List


MEMORY_DIRECTORY = Path("memory/data")
MEMORY_FILE = MEMORY_DIRECTORY / "memory.json"


def _ensure_storage() -> None:
    """
    Create the memory directory and file if necessary.
    """

    MEMORY_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True
    )

    if not MEMORY_FILE.exists():

        MEMORY_FILE.write_text(
            "[]",
            encoding="utf-8"
        )


def load_memory() -> List[str]:
    """
    Load persistent Fenix memory.
    """

    _ensure_storage()

    try:

        content = MEMORY_FILE.read_text(
            encoding="utf-8"
        )

        data = json.loads(content)

        if not isinstance(data, list):
            return []

        return [
            str(item)
            for item in data
        ]

    except (
        OSError,
        json.JSONDecodeError
    ):

        return []


def save_memory(memory: str) -> bool:
    """
    Add one item to persistent memory.
    """

    if not memory or not memory.strip():
        return False

    memories = load_memory()

    memories.append(
        memory.strip()
    )

    try:

        _ensure_storage()

        MEMORY_FILE.write_text(
            json.dumps(
                memories,
                ensure_ascii=False,
                indent=2
            ),
            encoding="utf-8"
        )

        return True

    except OSError:

        return False


def clear_memory() -> bool:
    """
    Delete all persistent Fenix memory.
    """

    try:

        _ensure_storage()

        MEMORY_FILE.write_text(
            "[]",
            encoding="utf-8"
        )

        return True

    except OSError:

        return False
