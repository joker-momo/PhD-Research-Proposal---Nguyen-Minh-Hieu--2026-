"""Safely validate the frozen pack and refresh only undispatched briefs."""

try:
    from .screening_refresh import (
        main,
        publish_refresh_metadata,
        validate_and_publish_staged_texts,
        write_pending_briefs,
    )
except ImportError:  # Direct execution: python3 scripts/prepare_46screening.py
    from screening_refresh import (
        main,
        publish_refresh_metadata,
        validate_and_publish_staged_texts,
        write_pending_briefs,
    )


if __name__ == "__main__":
    main()
