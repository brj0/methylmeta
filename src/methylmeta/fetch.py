from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path

from mepylome.dtypes.beads import idat_basepaths
from mepylome.utils.downloader import download_idats

from methylmeta.merger import find_metadata_file

logger = logging.getLogger(__name__)


@dataclass
class DatasetStatus:
    """Local on-disk availability of one dataset."""

    dataset_id: str
    has_metadata: bool
    has_idat: bool | None  # None if IDATs weren't checked

    @property
    def is_complete(self) -> bool:
        return self.has_metadata and self.has_idat is not False

    def __str__(self) -> str:
        parts = [f"metadata={'yes' if self.has_metadata else 'MISSING'}"]
        if self.has_idat is not None:
            parts.append(f"idat={'yes' if self.has_idat else 'MISSING'}")
        return f"{self.dataset_id}: {', '.join(parts)}"


def check_datasets(
    dataset_ids: list[str],
    dataset_dir: str | Path,
    check_idat: bool = False,
) -> list[DatasetStatus]:
    """Check which dataset_ids already have metadata (and idat) on disk."""
    dataset_dir = Path(dataset_dir)
    statuses = []

    for dataset_id in dataset_ids:
        data_path = dataset_dir / dataset_id

        has_metadata = False
        if data_path.is_dir():
            try:
                find_metadata_file(data_path)
                has_metadata = True
            except ValueError:
                has_metadata = False

        has_idat = None
        if check_idat:
            has_idat = bool(
                data_path.is_dir()
                and idat_basepaths(data_path, only_valid=True)
            )

        statuses.append(
            DatasetStatus(
                dataset_id=dataset_id,
                has_metadata=has_metadata,
                has_idat=has_idat,
            )
        )

    return statuses


def download_missing(
    statuses: list[DatasetStatus],
    dataset_dir: str | Path,
) -> None:
    """Download metadata/IDAT for any dataset missing on disk.

    Requests only the piece(s) actually missing per dataset, so a dataset
    that's missing IDATs but already has metadata won't re-download the
    metadata (and vice versa). Saves into `dataset_dir/<dataset_id>/`,
    matching the layout `MetadataMerger` already expects.
    """
    dataset_dir = Path(dataset_dir)

    for status in statuses:
        want_metadata = not status.has_metadata
        want_idat = status.has_idat is False

        if not (want_metadata or want_idat):
            continue

        logger.info(
            "Downloading %s (metadata=%s, idat=%s)",
            status.dataset_id,
            want_metadata,
            want_idat,
        )
        try:
            download_idats(
                dataset=status.dataset_id,
                save_dir=dataset_dir,
                idat=want_idat,
                metadata=want_metadata,
            )
        except Exception as exc:
            logger.warning("Download failed: %s (%s)", status.dataset_id, exc)
