
# Results vs. 3.10.4

- fork: python
- ref: 728e42fcf51cbb2108ca
- machine: darwin-arm64
- commit hash: 728e42f
- commit date: 2022-11-06
- overall geometric mean: 1.18x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 187 ms: 1.07x faster                                                   |
| chameleon      | 5.79 ms                                                | 5.13 ms: 1.13x faster                                                  |
| docutils       | 1.78 sec                                               | 1.50 sec: 1.19x faster                                                 |
| html5lib       | 44.2 ms                                                | 37.5 ms: 1.18x faster                                                  |
| tornado_http   | 91.5 ms                                                | 70.1 ms: 1.31x faster                                                  |
| Geometric mean | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 65.9 ms: 1.42x faster                                                  |
| float          | 72.4 ms                                                | 57.3 ms: 1.26x faster                                                  |
| Geometric mean | (ref)                                                  | 1.21x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 77.7 ms: 1.24x faster                                                  |
| regex_v8       | 17.6 ms                                                | 16.1 ms: 1.09x faster                                                  |
| regex_dna      | 162 ms                                                 | 149 ms: 1.09x faster                                                   |
| regex_effbot   | 2.46 ms                                                | 2.63 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 8.40 ms                                                | 6.15 ms: 1.36x faster                                                  |
| pickle_pure_python   | 283 us                                                 | 222 us: 1.27x faster                                                   |
| unpickle_pure_python | 203 us                                                 | 167 us: 1.22x faster                                                   |
| xml_etree_process    | 44.8 ms                                                | 36.8 ms: 1.22x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 93.3 ms: 1.14x faster                                                  |
| xml_etree_iterparse  | 72.3 ms                                                | 65.0 ms: 1.11x faster                                                  |
| xml_etree_generate   | 54.2 ms                                                | 50.5 ms: 1.07x faster                                                  |
| unpickle_list        | 2.69 us                                                | 2.60 us: 1.03x faster                                                  |
| json_loads           | 16.9 us                                                | 16.4 us: 1.03x faster                                                  |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.00x slower                                                  |
| pickle               | 7.35 us                                                | 7.55 us: 1.03x slower                                                  |
| pickle_list          | 2.80 us                                                | 2.88 us: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 9.32 ms: 1.28x faster                                                  |
| python_startup_no_site | 8.88 ms                                                | 7.38 ms: 1.20x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.24x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 27.3 ms                                                | 22.2 ms: 1.23x faster                                                  |
| mako            | 10.5 ms                                                | 8.59 ms: 1.22x faster                                                  |
| genshi_xml      | 37.2 ms                                                | 32.4 ms: 1.15x faster                                                  |
| genshi_text     | 18.4 ms                                                | 16.2 ms: 1.13x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.18x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| logging_silent          | 119 ns                                                 | 65.6 ns: 1.82x faster                                                  |
| deltablue               | 5.14 ms                                                | 2.85 ms: 1.80x faster                                                  |
| richards                | 51.4 ms                                                | 32.0 ms: 1.60x faster                                                  |
| scimark_lu              | 109 ms                                                 | 71.2 ms: 1.53x faster                                                  |
| raytrace                | 325 ms                                                 | 215 ms: 1.52x faster                                                   |
| crypto_pyaes            | 78.1 ms                                                | 51.7 ms: 1.51x faster                                                  |
| async_tree_memoization  | 490 ms                                                 | 335 ms: 1.47x faster                                                   |
| nbody                   | 93.3 ms                                                | 65.9 ms: 1.42x faster                                                  |
| pathlib                 | 28.8 ms                                                | 20.8 ms: 1.39x faster                                                  |
| async_tree_io           | 1.02 sec                                               | 736 ms: 1.38x faster                                                   |
| go                      | 165 ms                                                 | 121 ms: 1.37x faster                                                   |
| json_dumps              | 8.40 ms                                                | 6.15 ms: 1.36x faster                                                  |
| async_tree_none         | 400 ms                                                 | 294 ms: 1.36x faster                                                   |
| sqlglot_parse           | 1.37 ms                                                | 1.01 ms: 1.35x faster                                                  |
| spectral_norm           | 95.8 ms                                                | 71.9 ms: 1.33x faster                                                  |
| sqlglot_transpile       | 1.57 ms                                                | 1.19 ms: 1.33x faster                                                  |
| scimark_monte_carlo     | 72.5 ms                                                | 54.9 ms: 1.32x faster                                                  |
| thrift                  | 580 us                                                 | 443 us: 1.31x faster                                                   |
| tornado_http            | 91.5 ms                                                | 70.1 ms: 1.31x faster                                                  |
| chaos                   | 66.7 ms                                                | 51.6 ms: 1.29x faster                                                  |
| pycparser               | 916 ms                                                 | 711 ms: 1.29x faster                                                   |
| hexiom                  | 6.32 ms                                                | 4.91 ms: 1.29x faster                                                  |
| python_startup          | 11.9 ms                                                | 9.32 ms: 1.28x faster                                                  |
| pyflate                 | 453 ms                                                 | 355 ms: 1.28x faster                                                   |
| pickle_pure_python      | 283 us                                                 | 222 us: 1.27x faster                                                   |
| float                   | 72.4 ms                                                | 57.3 ms: 1.26x faster                                                  |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.76 ms: 1.25x faster                                                  |
| dulwich_log             | 37.1 ms                                                | 29.7 ms: 1.25x faster                                                  |
| regex_compile           | 96.4 ms                                                | 77.7 ms: 1.24x faster                                                  |
| django_template         | 27.3 ms                                                | 22.2 ms: 1.23x faster                                                  |
| logging_simple          | 4.63 us                                                | 3.77 us: 1.23x faster                                                  |
| scimark_sor             | 126 ms                                                 | 103 ms: 1.22x faster                                                   |
| async_tree_cpu_io_mixed | 669 ms                                                 | 547 ms: 1.22x faster                                                   |
| mako                    | 10.5 ms                                                | 8.59 ms: 1.22x faster                                                  |
| unpickle_pure_python    | 203 us                                                 | 167 us: 1.22x faster                                                   |
| xml_etree_process       | 44.8 ms                                                | 36.8 ms: 1.22x faster                                                  |
| logging_format          | 4.97 us                                                | 4.09 us: 1.21x faster                                                  |
| python_startup_no_site  | 8.88 ms                                                | 7.38 ms: 1.20x faster                                                  |
| pylint                  | 307 ms                                                 | 257 ms: 1.20x faster                                                   |
| docutils                | 1.78 sec                                               | 1.50 sec: 1.19x faster                                                 |
| sqlglot_optimize        | 38.0 ms                                                | 32.0 ms: 1.18x faster                                                  |
| html5lib                | 44.2 ms                                                | 37.5 ms: 1.18x faster                                                  |
| bench_thread_pool       | 546 us                                                 | 463 us: 1.18x faster                                                   |
| pprint_safe_repr        | 606 ms                                                 | 514 ms: 1.18x faster                                                   |
| fannkuch                | 317 ms                                                 | 270 ms: 1.17x faster                                                   |
| pprint_pformat          | 1.23 sec                                               | 1.05 sec: 1.17x faster                                                 |
| generators              | 32.7 ms                                                | 28.1 ms: 1.17x faster                                                  |
| async_generators        | 234 ms                                                 | 202 ms: 1.16x faster                                                   |
| scimark_fft             | 230 ms                                                 | 200 ms: 1.15x faster                                                   |
| nqueens                 | 68.2 ms                                                | 59.3 ms: 1.15x faster                                                  |
| genshi_xml              | 37.2 ms                                                | 32.4 ms: 1.15x faster                                                  |
| xml_etree_parse         | 106 ms                                                 | 93.3 ms: 1.14x faster                                                  |
| genshi_text             | 18.4 ms                                                | 16.2 ms: 1.13x faster                                                  |
| chameleon               | 5.79 ms                                                | 5.13 ms: 1.13x faster                                                  |
| sqlglot_normalize       | 196 ms                                                 | 175 ms: 1.12x faster                                                   |
| xml_etree_iterparse     | 72.3 ms                                                | 65.0 ms: 1.11x faster                                                  |
| sympy_integrate         | 13.3 ms                                                | 12.1 ms: 1.10x faster                                                  |
| regex_v8                | 17.6 ms                                                | 16.1 ms: 1.09x faster                                                  |
| regex_dna               | 162 ms                                                 | 149 ms: 1.09x faster                                                   |
| sympy_expand            | 275 ms                                                 | 255 ms: 1.08x faster                                                   |
| json                    | 3.08 ms                                                | 2.86 ms: 1.08x faster                                                  |
| deepcopy_memo           | 34.4 us                                                | 32.1 us: 1.07x faster                                                  |
| 2to3                    | 201 ms                                                 | 187 ms: 1.07x faster                                                   |
| xml_etree_generate      | 54.2 ms                                                | 50.5 ms: 1.07x faster                                                  |
| deepcopy                | 281 us                                                 | 263 us: 1.07x faster                                                   |
| mdp                     | 1.66 sec                                               | 1.55 sec: 1.07x faster                                                 |
| sympy_str               | 169 ms                                                 | 159 ms: 1.07x faster                                                   |
| sympy_sum               | 93.6 ms                                                | 88.0 ms: 1.06x faster                                                  |
| coroutines              | 20.2 ms                                                | 19.1 ms: 1.06x faster                                                  |
| telco                   | 3.63 ms                                                | 3.44 ms: 1.06x faster                                                  |
| deepcopy_reduce         | 2.37 us                                                | 2.28 us: 1.04x faster                                                  |
| unpickle_list           | 2.69 us                                                | 2.60 us: 1.03x faster                                                  |
| json_loads              | 16.9 us                                                | 16.4 us: 1.03x faster                                                  |
| sqlite_synth            | 1.47 us                                                | 1.45 us: 1.02x faster                                                  |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.00x slower                                                  |
| pickle                  | 7.35 us                                                | 7.55 us: 1.03x slower                                                  |
| pickle_list             | 2.80 us                                                | 2.88 us: 1.03x slower                                                  |
| meteor_contest          | 78.1 ms                                                | 80.5 ms: 1.03x slower                                                  |
| regex_effbot            | 2.46 ms                                                | 2.63 ms: 1.07x slower                                                  |
| bench_mp_pool           | 39.7 ms                                                | 42.8 ms: 1.08x slower                                                  |
| coverage                | 42.0 ms                                                | 53.1 ms: 1.26x slower                                                  |
| unpack_sequence         | 37.4 ns                                                | 52.1 ns: 1.39x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.18x faster                                                           |

Benchmark hidden because not significant (2): unpickle, pidigits
Ignored benchmarks (11) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221106-3.12.0a1+-728e42f/bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f.json: mypy
