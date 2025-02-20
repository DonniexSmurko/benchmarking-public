# Various git-related utilities


import datetime
import hashlib
from pathlib import Path
import subprocess
from typing import Iterable, List, Optional


def get_log(
    format: str,
    dirname,
    ref: Optional[str] = None,
    n: int = 1,
    extra: List[str] = [],
) -> str:
    """
    format: The git pretty format string for each log entry
    dirname: Local checkout of the repository
    ref: If provided, the git ref to show
    n: If < 1, show full log, otherwise the number of entries to show
    extra: Extra arguments to pass to `git log`
    """
    if ref is None:
        ref_args = []
    else:
        ref_args = [ref]
    if n < 1:
        n_args = []
    else:
        n_args = ["-n", str(n)]
    return subprocess.check_output(
        ["git", "log", f"--pretty=format:{format}"] + n_args + ref_args + extra,
        encoding="utf-8",
        cwd=dirname,
    ).strip()


def get_git_hash(dirname) -> str:
    return get_log("%h", dirname)


def get_git_commit_date(dirname) -> str:
    return get_log("%cI", dirname)


def remove(repodir, path) -> None:
    subprocess.check_output(
        ["git", "rm", str(path)],
        cwd=repodir,
    )


def get_git_merge_base(dirname) -> Optional[str]:
    # We need to make sure we have commits from main that are old enough to be
    # the base of this branch, but not so old that we waste a ton of bandwidth
    commit_date = datetime.datetime.fromisoformat(get_git_commit_date(dirname))
    commit_date = commit_date - datetime.timedelta(365 * 2)

    subprocess.check_call(
        ["git", "remote", "add", "upstream", "https://github.com/python/cpython.git"],
        cwd=dirname,
    )
    subprocess.check_call(
        [
            "git",
            "fetch",
            "upstream",
            "main",
            "--shallow-since",
            commit_date.isoformat(),
        ],
        cwd=dirname,
    )
    try:
        return subprocess.check_output(
            ["git", "merge-base", "upstream/main", "HEAD"],
            cwd=dirname,
            encoding="utf-8",
        ).strip()
    except subprocess.CalledProcessError:
        print("Failed to get merge base")
        return None


def get_tags(dirname) -> List[str]:
    subprocess.check_call(["git", "fetch", "--tags"], cwd=dirname)
    return subprocess.check_output(
        ["git", "tag"], cwd=dirname, encoding="utf-8"
    ).splitlines()


def generate_combined_hash(dirs: Iterable) -> str:
    hash = hashlib.sha256()
    for dirname in dirs:
        if Path(dirname).is_dir():
            subhash = get_git_hash(dirname)
            hash.update(subhash.encode("ascii"))
    return hash.hexdigest()[:6]


def get_commits_between(dirname: Path, ref1: str, ref2: str) -> List[str]:
    return list(
        subprocess.check_output(
            ["git", "rev-list", "--ancestry-path", f"{ref1}..{ref2}"],
            cwd=dirname,
            encoding="utf-8",
        ).splitlines()
    )


def bisect_commits(dirname: Path, ref1: str, ref2: str) -> str:
    commits = get_commits_between(dirname, ref1, ref2)
    return commits[len(commits) // 2]
