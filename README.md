# Faster CPython Benchmark Infrastructure

🔒 [▶️ START A BENCHMARK RUN](https://github.com/faster-cpython/benchmarking/actions/workflows/benchmark.yml)

## Results

Here are some recent and important revisions. 👉 [Complete list of results](RESULTS.md).

<!-- START table -->
## linux x86_64
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-02-20](results/bm-20230220-3.12.0a5%2B-4c82d9e) | iritkatriel | int_freeli | 3.12.0a5+ | 4c82d9e | [1.30x faster](results/bm-20230220-3.12.0a5%2B-4c82d9e/bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5%2B-4c82d9e-vs-3.10.4.md) | [1.04x faster](results/bm-20230220-3.12.0a5%2B-4c82d9e/bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5%2B-4c82d9e-vs-3.11.0.md) | [1.00x faster](results/bm-20230220-3.12.0a5%2B-4c82d9e/bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5%2B-4c82d9e-vs-base.md) |
| [2023-02-18](results/bm-20230218-3.12.0a5%2B-61f1e67) | python | main | 3.12.0a5+ | 61f1e67 | [1.30x faster](results/bm-20230218-3.12.0a5%2B-61f1e67/bm-20230218-linux-x86_64-python-main-3.12.0a5%2B-61f1e67-vs-3.10.4.md) | [1.04x faster](results/bm-20230218-3.12.0a5%2B-61f1e67/bm-20230218-linux-x86_64-python-main-3.12.0a5%2B-61f1e67-vs-3.11.0.md) |  |
| [2023-02-17](results/bm-20230217-3.12.0a5%2B-b560583) | iritkatriel | single_arg | 3.12.0a5+ | b560583 | [1.31x faster](results/bm-20230217-3.12.0a5%2B-b560583/bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5%2B-b560583-vs-3.10.4.md) | [1.04x faster](results/bm-20230217-3.12.0a5%2B-b560583/bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5%2B-b560583-vs-3.11.0.md) | [1.01x faster](results/bm-20230217-3.12.0a5%2B-b560583/bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5%2B-b560583-vs-base.md) |
| [2023-02-17](results/bm-20230217-3.12.0a5%2B-5629a3e) | faster-cpython | pep_669_in | 3.12.0a5+ | 5629a3e | [1.32x faster](results/bm-20230217-3.12.0a5%2B-5629a3e/bm-20230217-linux-x86_64-faster%252dcpython-pep_669_incremental-3.12.0a5%2B-5629a3e-vs-3.10.4.md) | [1.05x faster](results/bm-20230217-3.12.0a5%2B-5629a3e/bm-20230217-linux-x86_64-faster%252dcpython-pep_669_incremental-3.12.0a5%2B-5629a3e-vs-3.11.0.md) | [1.01x faster](results/bm-20230217-3.12.0a5%2B-5629a3e/bm-20230217-linux-x86_64-faster%252dcpython-pep_669_incremental-3.12.0a5%2B-5629a3e-vs-base.md) |
| [2023-02-17](results/bm-20230217-3.12.0a5%2B-072011b) | python | 072011b3c3 | 3.12.0a5+ | 072011b | [1.29x faster](results/bm-20230217-3.12.0a5%2B-072011b/bm-20230217-linux-x86_64-python-072011b3c38f871cdc3a-3.12.0a5%2B-072011b-vs-3.10.4.md) | [1.03x faster](results/bm-20230217-3.12.0a5%2B-072011b/bm-20230217-linux-x86_64-python-072011b3c38f871cdc3a-3.12.0a5%2B-072011b-vs-3.11.0.md) |  |
| [2023-02-17](results/bm-20230217-3.12.0a5%2B-fb5f321) | faster-cpython | restrict_f | 3.12.0a5+ | fb5f321 | [1.30x faster](results/bm-20230217-3.12.0a5%2B-fb5f321/bm-20230217-linux-x86_64-faster%252dcpython-restrict_for_iter_sp-3.12.0a5%2B-fb5f321-vs-3.10.4.md) | [1.04x faster](results/bm-20230217-3.12.0a5%2B-fb5f321/bm-20230217-linux-x86_64-faster%252dcpython-restrict_for_iter_sp-3.12.0a5%2B-fb5f321-vs-3.11.0.md) | [1.00x slower](results/bm-20230217-3.12.0a5%2B-fb5f321/bm-20230217-linux-x86_64-faster%252dcpython-restrict_for_iter_sp-3.12.0a5%2B-fb5f321-vs-base.md) |
| [2023-02-17](results/bm-20230217-3.12.0a5%2B-3c0a31c) | python | 3c0a31cbfd | 3.12.0a5+ | 3c0a31c | [1.30x faster](results/bm-20230217-3.12.0a5%2B-3c0a31c/bm-20230217-linux-x86_64-python-3c0a31cbfd1258bd9615-3.12.0a5%2B-3c0a31c-vs-3.10.4.md) | [1.04x faster](results/bm-20230217-3.12.0a5%2B-3c0a31c/bm-20230217-linux-x86_64-python-3c0a31cbfd1258bd9615-3.12.0a5%2B-3c0a31c-vs-3.11.0.md) |  |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | v3.11.0 | 3.11.0 | deaf509 | [1.25x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.25x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |

## darwin arm64
| date | fork | ref | version | hash | vs. 3.10.4: | vs. 3.11.0: | vs. base: |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| [2023-02-18](results/bm-20230218-3.12.0a5%2B-61f1e67) | python | main | 3.12.0a5+ | 61f1e67 | [1.21x faster \*](results/bm-20230218-3.12.0a5%2B-61f1e67/bm-20230218-darwin-arm64-python-main-3.12.0a5%2B-61f1e67-vs-3.10.4.md) | [1.01x slower \*](results/bm-20230218-3.12.0a5%2B-61f1e67/bm-20230218-darwin-arm64-python-main-3.12.0a5%2B-61f1e67-vs-3.11.0.md) |  |
| [2023-02-11](results/bm-20230211-3.12.0a5%2B-3eb12df) | python | main | 3.12.0a5+ | 3eb12df | [1.24x faster \*](results/bm-20230211-3.12.0a5%2B-3eb12df/bm-20230211-darwin-arm64-python-main-3.12.0a5%2B-3eb12df-vs-3.10.4.md) | [1.02x faster \*](results/bm-20230211-3.12.0a5%2B-3eb12df/bm-20230211-darwin-arm64-python-main-3.12.0a5%2B-3eb12df-vs-3.11.0.md) |  |
| [2023-02-04](results/bm-20230204-3.12.0a4%2B-5a2b984) | python | main | 3.12.0a4+ | 5a2b984 | [1.23x faster \*](results/bm-20230204-3.12.0a4%2B-5a2b984/bm-20230204-darwin-arm64-python-main-3.12.0a4%2B-5a2b984-vs-3.10.4.md) | [1.01x faster \*](results/bm-20230204-3.12.0a4%2B-5a2b984/bm-20230204-darwin-arm64-python-main-3.12.0a4%2B-5a2b984-vs-3.11.0.md) |  |
| [2022-10-24](results/bm-20221024-3.11.0-deaf509) | python | deaf509e8f | 3.11.0 | deaf509 | [1.22x faster](results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509-vs-3.10.4.md) |  |  |
| [2022-03-23](results/bm-20220323-3.10.4-9d38120) | python | v3.10.4 | 3.10.4 | 9d38120 |  | [1.22x slower](results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120-vs-3.11.0.md) |  |


<!-- END table -->

`*` indicates that the exact same versions of pyperformance was not used.

![Longitudinal speed improvement](/longitudinal.png)

## Documentation

### Running benchmarks from the GitHub web UI

Visit the 🔒 [benchmark action](https://github.com/faster-cpython/benchmarking/actions/workflows/benchmark.yml) and click the "Run Workflow" button.

The available parameters are:

- `fork`: The fork of CPython to benchmark.
  If benchmarking a pull request, this would normally be your GitHub username.
- `ref`: The branch, tag or commit SHA to benchmark.
  If a SHA, it must be the full SHA, since finding it by a prefix is not supported.
- `machine`: The machine to run on.
  One of `linux-amd64` (default), `windows-amd64`, `darwin-arm64` or `all`.
- `benchmark_base`: If checked, the base of the selected branch will also be benchmarked.
  The base is determined by running `git merge-base upstream/main $ref`.
- `pystats`: If checked, collect the pystats from running the benchmarks.
- `publish`: If checked, the results will be published in the public [ideas repo](https://github.com/faster-cpython/ideas) upon successful completion.

To watch the progress of the benchmark, select it from the 🔒 [benchmark action page](https://github.com/faster-cpython/benchmarking/actions/workflows/benchmark.yml).
It may be canceled from there as well.
To show only your benchmark workflows, select your GitHub ID from the "Actor" dropdown.

When the benchmarking is complete, the results are published to this repository and will appear in the [master table](results/README.md).
Each set of benchmarks will have:

- The raw `.json` results from pyperformance.
- Comparisons against important reference releases, as well as the merge base of the branch if `benchmark_base` was selected.  These include
  - A markdown table produced by `pyperf compare_to`.
  - A set of "violin" plots showing the distribution of results for each benchmark.

The most convenient way to get results locally is to clone this repo and `git pull` from it.

### Running benchmarks from the GitHub CLI

To automate benchmarking runs, it may be more convenient to use the [GitHub CLI](https://cli.github.com/).
Once you have `gh` installed and configured, you can run benchmarks by cloning this repository and then from inside it:

```bash
$ gh workflow run benchmark.yml -f fork=me -f ref=my_branch
```

Any of the parameters described above are available at the commandline using the `-f key=value` syntax.

### Costs

We are limited to 2,000 compute minutes per month.


| Action | Minutes |
| -- | -- |
| Benchmarks | 7 minutes (most of the time is on self-hosted runners) |
| CI | 10 minutes |

To reduce CI usage, PRs that are only documentation changes should add the `[skip ci]` token to their commit message.

### Analysis changes

This is a changelog of changes that affect the derived data and results:

- 2023-02-09: The plots exclude benchmarks that aren't significant using the same algorithm used by the table results.
  These benchmarks do not contribute to the overall distribution at the top of the plot.

### Developer docs

For documentation about how this works, see the [developer docs](DEVELOPER.md).

