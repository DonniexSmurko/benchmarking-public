
# Results vs. 3.10.4

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: 866c937
- commit date: 2023-02-01
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 251 ms: 1.33x faster                                                       |
| chameleon      | 8.86 ms                                                | 6.41 ms: 1.38x faster                                                      |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                     |
| html5lib       | 85.8 ms                                                | 60.1 ms: 1.43x faster                                                      |
| tornado_http   | 128 ms                                                 | 94.5 ms: 1.36x faster                                                      |
| Geometric mean | (ref)                                                  | 1.35x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 108 ms                                                 | 74.2 ms: 1.45x faster                                                      |
| nbody          | 136 ms                                                 | 94.9 ms: 1.44x faster                                                      |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.26x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 128 ms: 1.36x faster                                                       |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.11x faster                                                      |
| regex_dna      | 214 ms                                                 | 217 ms: 1.02x slower                                                       |
| regex_effbot   | 3.21 ms                                                | 3.76 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 283 us: 1.60x faster                                                       |
| unpickle_pure_python | 297 us                                                 | 200 us: 1.49x faster                                                       |
| json_dumps           | 13.5 ms                                                | 9.46 ms: 1.43x faster                                                      |
| xml_etree_process    | 74.5 ms                                                | 53.7 ms: 1.39x faster                                                      |
| xml_etree_generate   | 93.3 ms                                                | 78.0 ms: 1.20x faster                                                      |
| json_loads           | 28.9 us                                                | 24.3 us: 1.19x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                       |
| unpickle             | 14.3 us                                                | 13.3 us: 1.08x faster                                                      |
| xml_etree_iterparse  | 110 ms                                                 | 103 ms: 1.07x faster                                                       |
| pickle_list          | 4.50 us                                                | 4.25 us: 1.06x faster                                                      |
| unpickle_list        | 4.99 us                                                | 5.04 us: 1.01x slower                                                      |
| pickle               | 10.1 us                                                | 10.3 us: 1.01x slower                                                      |
| pickle_dict          | 28.3 us                                                | 32.4 us: 1.14x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.74 ms: 1.59x faster                                                      |
| python_startup_no_site | 5.76 ms                                                | 6.27 ms: 1.09x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.21x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.7 ms: 1.48x faster                                                      |
| mako            | 14.3 ms                                                | 9.85 ms: 1.45x faster                                                      |
| django_template | 46.3 ms                                                | 33.0 ms: 1.40x faster                                                      |
| genshi_xml      | 63.6 ms                                                | 46.8 ms: 1.36x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.18 ms: 2.33x faster                                                      |
| logging_silent          | 173 ns                                                 | 90.6 ns: 1.91x faster                                                      |
| scimark_sor             | 193 ms                                                 | 106 ms: 1.83x faster                                                       |
| richards                | 71.4 ms                                                | 41.9 ms: 1.70x faster                                                      |
| go                      | 226 ms                                                 | 133 ms: 1.70x faster                                                       |
| pyflate                 | 675 ms                                                 | 402 ms: 1.68x faster                                                       |
| raytrace                | 461 ms                                                 | 283 ms: 1.63x faster                                                       |
| chaos                   | 104 ms                                                 | 64.8 ms: 1.61x faster                                                      |
| scimark_monte_carlo     | 105 ms                                                 | 65.5 ms: 1.60x faster                                                      |
| pickle_pure_python      | 453 us                                                 | 283 us: 1.60x faster                                                       |
| python_startup          | 13.9 ms                                                | 8.74 ms: 1.59x faster                                                      |
| crypto_pyaes            | 118 ms                                                 | 74.2 ms: 1.58x faster                                                      |
| hexiom                  | 9.42 ms                                                | 5.96 ms: 1.58x faster                                                      |
| spectral_norm           | 148 ms                                                 | 96.9 ms: 1.53x faster                                                      |
| scimark_lu              | 158 ms                                                 | 106 ms: 1.50x faster                                                       |
| unpickle_pure_python    | 297 us                                                 | 200 us: 1.49x faster                                                       |
| genshi_text             | 30.6 ms                                                | 20.7 ms: 1.48x faster                                                      |
| deepcopy_memo           | 50.0 us                                                | 34.3 us: 1.46x faster                                                      |
| float                   | 108 ms                                                 | 74.2 ms: 1.45x faster                                                      |
| mako                    | 14.3 ms                                                | 9.85 ms: 1.45x faster                                                      |
| nbody                   | 136 ms                                                 | 94.9 ms: 1.44x faster                                                      |
| sqlglot_parse           | 2.04 ms                                                | 1.42 ms: 1.43x faster                                                      |
| html5lib                | 85.8 ms                                                | 60.1 ms: 1.43x faster                                                      |
| pprint_pformat          | 1.97 sec                                               | 1.38 sec: 1.43x faster                                                     |
| json_dumps              | 13.5 ms                                                | 9.46 ms: 1.43x faster                                                      |
| logging_format          | 8.92 us                                                | 6.32 us: 1.41x faster                                                      |
| sqlglot_transpile       | 2.42 ms                                                | 1.71 ms: 1.41x faster                                                      |
| pprint_safe_repr        | 943 ms                                                 | 670 ms: 1.41x faster                                                       |
| logging_simple          | 8.06 us                                                | 5.74 us: 1.40x faster                                                      |
| django_template         | 46.3 ms                                                | 33.0 ms: 1.40x faster                                                      |
| unpack_sequence         | 59.5 ns                                                | 42.6 ns: 1.40x faster                                                      |
| xml_etree_process       | 74.5 ms                                                | 53.7 ms: 1.39x faster                                                      |
| chameleon               | 8.86 ms                                                | 6.41 ms: 1.38x faster                                                      |
| thrift                  | 1.03 ms                                                | 750 us: 1.37x faster                                                       |
| regex_compile           | 174 ms                                                 | 128 ms: 1.36x faster                                                       |
| tornado_http            | 128 ms                                                 | 94.5 ms: 1.36x faster                                                      |
| genshi_xml              | 63.6 ms                                                | 46.8 ms: 1.36x faster                                                      |
| async_tree_none         | 713 ms                                                 | 526 ms: 1.36x faster                                                       |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.05 ms: 1.35x faster                                                      |
| scimark_fft             | 414 ms                                                 | 307 ms: 1.35x faster                                                       |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                                      |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.34x faster                                                     |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.33x faster                                                      |
| 2to3                    | 332 ms                                                 | 251 ms: 1.33x faster                                                       |
| deepcopy                | 429 us                                                 | 326 us: 1.32x faster                                                       |
| fannkuch                | 477 ms                                                 | 362 ms: 1.32x faster                                                       |
| pycparser               | 1.51 sec                                               | 1.16 sec: 1.30x faster                                                     |
| deepcopy_reduce         | 3.75 us                                                | 2.90 us: 1.29x faster                                                      |
| async_tree_memoization  | 854 ms                                                 | 661 ms: 1.29x faster                                                       |
| nqueens                 | 99.3 ms                                                | 76.9 ms: 1.29x faster                                                      |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.27x faster                                                       |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                     |
| sqlglot_optimize        | 65.3 ms                                                | 51.5 ms: 1.27x faster                                                      |
| mypy                    | 1.01 sec                                               | 807 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed | 949 ms                                                 | 758 ms: 1.25x faster                                                       |
| sympy_integrate         | 23.9 ms                                                | 19.6 ms: 1.22x faster                                                      |
| async_generators        | 428 ms                                                 | 353 ms: 1.21x faster                                                       |
| coroutines              | 31.7 ms                                                | 26.2 ms: 1.21x faster                                                      |
| sympy_str               | 324 ms                                                 | 269 ms: 1.20x faster                                                       |
| bench_thread_pool       | 943 us                                                 | 785 us: 1.20x faster                                                       |
| dulwich_log             | 75.5 ms                                                | 62.8 ms: 1.20x faster                                                      |
| xml_etree_generate      | 93.3 ms                                                | 78.0 ms: 1.20x faster                                                      |
| json_loads              | 28.9 us                                                | 24.3 us: 1.19x faster                                                      |
| sympy_expand            | 537 ms                                                 | 452 ms: 1.19x faster                                                       |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.19x faster                                                       |
| json                    | 5.35 ms                                                | 4.69 ms: 1.14x faster                                                      |
| sqlite_synth            | 2.90 us                                                | 2.58 us: 1.13x faster                                                      |
| mdp                     | 2.82 sec                                               | 2.51 sec: 1.13x faster                                                     |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.12x faster                                                      |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.11x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                       |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.08x faster                                                       |
| unpickle                | 14.3 us                                                | 13.3 us: 1.08x faster                                                      |
| xml_etree_iterparse     | 110 ms                                                 | 103 ms: 1.07x faster                                                       |
| pickle_list             | 4.50 us                                                | 4.25 us: 1.06x faster                                                      |
| telco                   | 6.68 ms                                                | 6.55 ms: 1.02x faster                                                      |
| generators              | 75.8 ms                                                | 76.0 ms: 1.00x slower                                                      |
| unpickle_list           | 4.99 us                                                | 5.04 us: 1.01x slower                                                      |
| pickle                  | 10.1 us                                                | 10.3 us: 1.01x slower                                                      |
| regex_dna               | 214 ms                                                 | 217 ms: 1.02x slower                                                       |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                       |
| python_startup_no_site  | 5.76 ms                                                | 6.27 ms: 1.09x slower                                                      |
| pickle_dict             | 28.3 us                                                | 32.4 us: 1.14x slower                                                      |
| regex_effbot            | 3.21 ms                                                | 3.76 ms: 1.17x slower                                                      |
| coverage                | 75.3 ms                                                | 100 ms: 1.33x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                               |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230201-3.12.0a4+-866c937/bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal