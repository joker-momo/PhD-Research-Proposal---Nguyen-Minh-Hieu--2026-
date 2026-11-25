"""Portable path handling for the frozen 46-report screening corpus."""

from pathlib import Path


def _within(root: Path, candidate: Path) -> Path:
    root = root.resolve()
    candidate = candidate.resolve()
    try:
        candidate.relative_to(root)
    except ValueError as error:
        raise ValueError(f"screening path escapes {root}: {candidate}") from error
    return candidate


def resolve_screening_path(screening_root: Path, locator: str) -> Path:
    """Resolve a manifest locator while retaining legacy absolute-path reads."""
    path = Path(locator)
    if path.is_absolute():
        return path.resolve()
    return _within(screening_root, screening_root / path)


def to_screening_locator(screening_root: Path, path: Path) -> str:
    """Return a POSIX locator for a path contained by ``screening_root``."""
    contained = _within(screening_root, path)
    return contained.relative_to(screening_root.resolve()).as_posix()
