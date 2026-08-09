

import json
from pathlib import Path


# ---------------------------------------------------------
# FENIX MEMORY MANAGER
# ---------------------------------------------------------

MEMORY_FILE = Path("data/memory.json")


def _ensure_memory_file() -> None:
    """
    Make sure the memory directory and file exist.
    """

    MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not MEMORY_FILE.exists():
        MEMORY_FILE.write_text(
            "[]",
            encoding="utf-8"
        )


def load_memory() -> list:
    """
    Load all saved memories from disk.
    """

    _ensure_memory_file()

    try:
        content = MEMORY_FILE.read_text(
            encoding="utf-8"
        )

        memory = json.loads(content)

        if not isinstance(memory, list):
            return []

        return memory

    except (json.JSONDecodeError, OSError):
        return []


def save_memory(memory: str) -> bool:
    """
    Save a new memory.

    Returns True if the memory was saved successfully.
    """

    if not isinstance(memory, str):
        return False

    memory = memory.strip()

    if not memory:
        return False

    memories = load_memory()

    memories.append(memory)

    try:
        MEMORY_FILE.write_text(
            json.dumps(
                memories,
                ensure_ascii=False,
                indent=4
            ),
            encoding="utf-8"
        )

        return True

    except OSError:
        return False


def delete_memory(memory: str) -> bool:
    """
    Delete a specific memory.

    Returns True if the memory was removed.
    """

    memories = load_memory()

    if memory not in memories:
        return False

    memories.remove(memory)

    try:
        MEMORY_FILE.write_text(
            json.dumps(
                memories,
                ensure_ascii=False,
                indent=4
            ),
            encoding="utf-8"
        )

        return True

    except OSError:
        return False


def clear_memory() -> bool:
    """
    Delete all saved memories.
    """

    try:
        MEMORY_FILE.write_text(
            "[]",
            encoding="utf-8"
        )

        return True

    except OSError:
        return False
