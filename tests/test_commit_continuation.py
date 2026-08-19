from javadoc_miner.commit_continuation import _is_metadata_only_commit_message


def test_metadata_only_commit_message_matches_license_header_cleanup():
    assert _is_metadata_only_commit_message("URL Cleanup - license headers - `target` subpackages")
    assert _is_metadata_only_commit_message("Update copyright notice")
    assert _is_metadata_only_commit_message("Polish URL Cleanup\n\nUpdate Apache Headers")
    assert _is_metadata_only_commit_message("URL Cleanup\n\nThis commit updates URLs to prefer the https protocol.")


def test_metadata_only_commit_message_keeps_behavioral_subjects():
    assert not _is_metadata_only_commit_message("Support custom target source lifecycle")
