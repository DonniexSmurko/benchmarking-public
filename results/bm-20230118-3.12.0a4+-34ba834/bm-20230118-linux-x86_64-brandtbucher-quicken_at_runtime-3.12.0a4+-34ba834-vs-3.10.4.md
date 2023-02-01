
# Results vs. 3.10.4

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: 34ba834
- commit date: 2023-01-18
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 256 ms: 1.30x faster                                                       |
| chameleon      | 8.86 ms                                                | 6.56 ms: 1.35x faster                                                      |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                     |
| html5lib       | 85.8 ms                                                | 61.4 ms: 1.40x faster                                                      |
| tornado_http   | 128 ms                                                 | 94.7 ms: 1.35x faster                                                      |
| Geometric mean | (ref)                                                  | 1.33x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 136 ms                                                 | 92.5 ms: 1.47x faster                                                      |
| float          | 108 ms                                                 | 74.3 ms: 1.45x faster                                                      |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.27x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 130 ms: 1.34x faster                                                       |
| regex_v8       | 25.0 ms                                                | 21.1 ms: 1.18x faster                                                      |
| regex_dna      | 214 ms                                                 | 201 ms: 1.06x faster                                                       |
| regex_effbot   | 3.21 ms                                                | 3.44 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                  | 1.12x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 290 us: 1.56x faster                                                       |
| unpickle_pure_python | 297 us                                                 | 209 us: 1.42x faster                                                       |
| json_dumps           | 13.5 ms                                                | 9.55 ms: 1.41x faster                                                      |
| xml_etree_process    | 74.5 ms                                                | 53.5 ms: 1.39x faster                                                      |
| xml_etree_generate   | 93.3 ms                                                | 77.2 ms: 1.21x faster                                                      |
| json_loads           | 28.9 us                                                | 24.4 us: 1.19x faster                                                      |
| pickle_list          | 4.50 us                                                | 4.02 us: 1.12x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                 | 102 ms: 1.08x faster                                                       |
| unpickle             | 14.3 us                                                | 13.3 us: 1.07x faster                                                      |
| pickle               | 10.1 us                                                | 10.0 us: 1.01x faster                                                      |
| pickle_dict          | 28.3 us                                                | 30.6 us: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                               |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.72 ms: 1.60x faster                                                      |
| python_startup_no_site | 5.76 ms                                                | 6.25 ms: 1.08x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.21x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.5 ms: 1.49x faster                                                      |
| mako            | 14.3 ms                                                | 9.57 ms: 1.49x faster                                                      |
| django_template | 46.3 ms                                                | 32.7 ms: 1.42x faster                                                      |
| genshi_xml      | 63.6 ms                                                | 48.1 ms: 1.32x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.32 ms: 2.23x faster                                                      |
| logging_silent          | 173 ns                                                 | 92.3 ns: 1.88x faster                                                      |
| raytrace                | 461 ms                                                 | 282 ms: 1.64x faster                                                       |
| go                      | 226 ms                                                 | 139 ms: 1.63x faster                                                       |
| richards                | 71.4 ms                                                | 43.8 ms: 1.63x faster                                                      |
| crypto_pyaes            | 118 ms                                                 | 72.8 ms: 1.61x faster                                                      |
| pyflate                 | 675 ms                                                 | 421 ms: 1.60x faster                                                       |
| python_startup          | 13.9 ms                                                | 8.72 ms: 1.60x faster                                                      |
| scimark_sor             | 193 ms                                                 | 121 ms: 1.59x faster                                                       |
| chaos                   | 104 ms                                                 | 65.3 ms: 1.59x faster                                                      |
| pickle_pure_python      | 453 us                                                 | 290 us: 1.56x faster                                                       |
| spectral_norm           | 148 ms                                                 | 95.4 ms: 1.55x faster                                                      |
| scimark_monte_carlo     | 105 ms                                                 | 67.6 ms: 1.55x faster                                                      |
| hexiom                  | 9.42 ms                                                | 6.12 ms: 1.54x faster                                                      |
| genshi_text             | 30.6 ms                                                | 20.5 ms: 1.49x faster                                                      |
| mako                    | 14.3 ms                                                | 9.57 ms: 1.49x faster                                                      |
| scimark_lu              | 158 ms                                                 | 107 ms: 1.48x faster                                                       |
| nbody                   | 136 ms                                                 | 92.5 ms: 1.47x faster                                                      |
| deepcopy_memo           | 50.0 us                                                | 34.0 us: 1.47x faster                                                      |
| float                   | 108 ms                                                 | 74.3 ms: 1.45x faster                                                      |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.45x faster                                                      |
| pprint_pformat          | 1.97 sec                                               | 1.38 sec: 1.43x faster                                                     |
| sqlglot_transpile       | 2.42 ms                                                | 1.70 ms: 1.42x faster                                                      |
| unpickle_pure_python    | 297 us                                                 | 209 us: 1.42x faster                                                       |
| django_template         | 46.3 ms                                                | 32.7 ms: 1.42x faster                                                      |
| json_dumps              | 13.5 ms                                                | 9.55 ms: 1.41x faster                                                      |
| html5lib                | 85.8 ms                                                | 61.4 ms: 1.40x faster                                                      |
| xml_etree_process       | 74.5 ms                                                | 53.5 ms: 1.39x faster                                                      |
| pprint_safe_repr        | 943 ms                                                 | 677 ms: 1.39x faster                                                       |
| thrift                  | 1.03 ms                                                | 741 us: 1.39x faster                                                       |
| logging_format          | 8.92 us                                                | 6.42 us: 1.39x faster                                                      |
| logging_simple          | 8.06 us                                                | 5.85 us: 1.38x faster                                                      |
| unpack_sequence         | 59.5 ns                                                | 43.3 ns: 1.37x faster                                                      |
| pycparser               | 1.51 sec                                               | 1.11 sec: 1.36x faster                                                     |
| scimark_fft             | 414 ms                                                 | 305 ms: 1.36x faster                                                       |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.36x faster                                                     |
| async_tree_none         | 713 ms                                                 | 526 ms: 1.35x faster                                                       |
| tornado_http            | 128 ms                                                 | 94.7 ms: 1.35x faster                                                      |
| chameleon               | 8.86 ms                                                | 6.56 ms: 1.35x faster                                                      |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                                      |
| regex_compile           | 174 ms                                                 | 130 ms: 1.34x faster                                                       |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.33x faster                                                      |
| genshi_xml              | 63.6 ms                                                | 48.1 ms: 1.32x faster                                                      |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.16 ms: 1.32x faster                                                      |
| deepcopy                | 429 us                                                 | 329 us: 1.30x faster                                                       |
| 2to3                    | 332 ms                                                 | 256 ms: 1.30x faster                                                       |
| async_tree_memoization  | 854 ms                                                 | 659 ms: 1.30x faster                                                       |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                       |
| sqlglot_optimize        | 65.3 ms                                                | 50.8 ms: 1.28x faster                                                      |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                     |
| deepcopy_reduce         | 3.75 us                                                | 2.96 us: 1.27x faster                                                      |
| fannkuch                | 477 ms                                                 | 378 ms: 1.26x faster                                                       |
| nqueens                 | 99.3 ms                                                | 78.7 ms: 1.26x faster                                                      |
| mypy                    | 1.01 sec                                               | 806 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed | 949 ms                                                 | 756 ms: 1.25x faster                                                       |
| coroutines              | 31.7 ms                                                | 25.8 ms: 1.23x faster                                                      |
| xml_etree_generate      | 93.3 ms                                                | 77.2 ms: 1.21x faster                                                      |
| dulwich_log             | 75.5 ms                                                | 62.9 ms: 1.20x faster                                                      |
| sympy_integrate         | 23.9 ms                                                | 20.0 ms: 1.20x faster                                                      |
| sympy_str               | 324 ms                                                 | 271 ms: 1.20x faster                                                       |
| bench_thread_pool       | 943 us                                                 | 791 us: 1.19x faster                                                       |
| async_generators        | 428 ms                                                 | 359 ms: 1.19x faster                                                       |
| json_loads              | 28.9 us                                                | 24.4 us: 1.19x faster                                                      |
| regex_v8                | 25.0 ms                                                | 21.1 ms: 1.18x faster                                                      |
| sympy_expand            | 537 ms                                                 | 455 ms: 1.18x faster                                                       |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.18x faster                                                       |
| json                    | 5.35 ms                                                | 4.67 ms: 1.15x faster                                                      |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.13x faster                                                      |
| pickle_list             | 4.50 us                                                | 4.02 us: 1.12x faster                                                      |
| sqlite_synth            | 2.90 us                                                | 2.61 us: 1.11x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                       |
| mdp                     | 2.82 sec                                               | 2.60 sec: 1.08x faster                                                     |
| xml_etree_iterparse     | 110 ms                                                 | 102 ms: 1.08x faster                                                       |
| meteor_contest          | 114 ms                                                 | 106 ms: 1.08x faster                                                       |
| unpickle                | 14.3 us                                                | 13.3 us: 1.07x faster                                                      |
| regex_dna               | 214 ms                                                 | 201 ms: 1.06x faster                                                       |
| telco                   | 6.68 ms                                                | 6.44 ms: 1.04x faster                                                      |
| pickle                  | 10.1 us                                                | 10.0 us: 1.01x faster                                                      |
| generators              | 75.8 ms                                                | 76.3 ms: 1.01x slower                                                      |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                       |
| regex_effbot            | 3.21 ms                                                | 3.44 ms: 1.07x slower                                                      |
| pickle_dict             | 28.3 us                                                | 30.6 us: 1.08x slower                                                      |
| python_startup_no_site  | 5.76 ms                                                | 6.25 ms: 1.08x slower                                                      |
| coverage                | 75.3 ms                                                | 102 ms: 1.35x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                               |

Benchmark hidden because not significant (2): bench_mp_pool, unpickle_list
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230118-3.12.0a4+-34ba834/bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal