
# Results vs. 3.11.0

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: fa5965d
- commit date: 2023-02-02
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 251 ms: 1.03x faster                                                       |
| chameleon      | 6.41 ms                                                | 6.26 ms: 1.02x faster                                                      |
| docutils       | 2.60 sec                                               | 2.49 sec: 1.04x faster                                                     |
| html5lib       | 63.2 ms                                                | 60.1 ms: 1.05x faster                                                      |
| tornado_http   | 96.6 ms                                                | 94.3 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 71.9 ms: 1.06x faster                                                      |
| pidigits       | 199 ms                                                 | 198 ms: 1.01x faster                                                       |
| nbody          | 95.0 ms                                                | 98.9 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.07x faster                                                       |
| regex_v8       | 22.3 ms                                                | 21.7 ms: 1.03x faster                                                      |
| regex_effbot   | 3.36 ms                                                | 3.40 ms: 1.01x slower                                                      |
| regex_dna      | 203 ms                                                 | 210 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.40 ms: 1.35x faster                                                      |
| unpickle_pure_python | 225 us                                                 | 198 us: 1.14x faster                                                       |
| json_loads           | 26.2 us                                                | 23.9 us: 1.10x faster                                                      |
| pickle_pure_python   | 304 us                                                 | 285 us: 1.07x faster                                                       |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                                       |
| pickle_dict          | 31.4 us                                                | 31.0 us: 1.01x faster                                                      |
| xml_etree_process    | 53.8 ms                                                | 53.1 ms: 1.01x faster                                                      |
| xml_etree_iterparse  | 103 ms                                                 | 102 ms: 1.01x faster                                                       |
| pickle_list          | 4.17 us                                                | 4.15 us: 1.01x faster                                                      |
| xml_etree_generate   | 76.2 ms                                                | 76.7 ms: 1.01x slower                                                      |
| unpickle_list        | 4.95 us                                                | 5.07 us: 1.02x slower                                                      |
| pickle               | 9.79 us                                                | 10.3 us: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                               |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.72 ms: 1.04x slower                                                      |
| python_startup_no_site | 5.96 ms                                                | 6.25 ms: 1.05x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 47.8 ms: 1.09x faster                                                      |
| genshi_text     | 22.1 ms                                                | 21.3 ms: 1.04x faster                                                      |
| mako            | 9.85 ms                                                | 9.53 ms: 1.03x faster                                                      |
| django_template | 32.5 ms                                                | 32.9 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.40 ms: 1.35x faster                                                      |
| unpickle_pure_python    | 225 us                                                 | 198 us: 1.14x faster                                                       |
| deltablue               | 3.64 ms                                                | 3.21 ms: 1.14x faster                                                      |
| nqueens                 | 85.0 ms                                                | 75.8 ms: 1.12x faster                                                      |
| json_loads              | 26.2 us                                                | 23.9 us: 1.10x faster                                                      |
| richards                | 46.2 ms                                                | 42.2 ms: 1.09x faster                                                      |
| genshi_xml              | 52.1 ms                                                | 47.8 ms: 1.09x faster                                                      |
| scimark_fft             | 329 ms                                                 | 304 ms: 1.08x faster                                                       |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.08x faster                                                       |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.08 ms: 1.08x faster                                                      |
| json                    | 4.95 ms                                                | 4.60 ms: 1.07x faster                                                      |
| fannkuch                | 388 ms                                                 | 361 ms: 1.07x faster                                                       |
| deepcopy_memo           | 36.4 us                                                | 34.0 us: 1.07x faster                                                      |
| hexiom                  | 6.35 ms                                                | 5.93 ms: 1.07x faster                                                      |
| logging_silent          | 98.5 ns                                                | 92.0 ns: 1.07x faster                                                      |
| go                      | 143 ms                                                 | 134 ms: 1.07x faster                                                       |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                       |
| pickle_pure_python      | 304 us                                                 | 285 us: 1.07x faster                                                       |
| regex_compile           | 136 ms                                                 | 128 ms: 1.07x faster                                                       |
| chaos                   | 68.6 ms                                                | 64.5 ms: 1.06x faster                                                      |
| sympy_str               | 287 ms                                                 | 271 ms: 1.06x faster                                                       |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                                       |
| float                   | 76.3 ms                                                | 71.9 ms: 1.06x faster                                                      |
| pyflate                 | 417 ms                                                 | 394 ms: 1.06x faster                                                       |
| sympy_integrate         | 20.9 ms                                                | 19.8 ms: 1.05x faster                                                      |
| html5lib                | 63.2 ms                                                | 60.1 ms: 1.05x faster                                                      |
| scimark_monte_carlo     | 68.3 ms                                                | 65.2 ms: 1.05x faster                                                      |
| telco                   | 6.62 ms                                                | 6.33 ms: 1.05x faster                                                      |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.05x faster                                                      |
| deepcopy                | 344 us                                                 | 329 us: 1.04x faster                                                       |
| bench_thread_pool       | 810 us                                                 | 777 us: 1.04x faster                                                       |
| docutils                | 2.60 sec                                               | 2.49 sec: 1.04x faster                                                     |
| logging_simple          | 6.06 us                                                | 5.83 us: 1.04x faster                                                      |
| sqlglot_optimize        | 53.0 ms                                                | 50.9 ms: 1.04x faster                                                      |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                                      |
| genshi_text             | 22.1 ms                                                | 21.3 ms: 1.04x faster                                                      |
| sympy_expand            | 472 ms                                                 | 455 ms: 1.04x faster                                                       |
| pprint_pformat          | 1.44 sec                                               | 1.39 sec: 1.04x faster                                                     |
| mako                    | 9.85 ms                                                | 9.53 ms: 1.03x faster                                                      |
| spectral_norm           | 99.9 ms                                                | 96.8 ms: 1.03x faster                                                      |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                       |
| logging_format          | 6.62 us                                                | 6.42 us: 1.03x faster                                                      |
| raytrace                | 290 ms                                                 | 282 ms: 1.03x faster                                                       |
| regex_v8                | 22.3 ms                                                | 21.7 ms: 1.03x faster                                                      |
| 2to3                    | 257 ms                                                 | 251 ms: 1.03x faster                                                       |
| pycparser               | 1.17 sec                                               | 1.14 sec: 1.03x faster                                                     |
| scimark_lu              | 107 ms                                                 | 105 ms: 1.03x faster                                                       |
| tornado_http            | 96.6 ms                                                | 94.3 ms: 1.02x faster                                                      |
| mdp                     | 2.62 sec                                               | 2.56 sec: 1.02x faster                                                     |
| chameleon               | 6.41 ms                                                | 6.26 ms: 1.02x faster                                                      |
| coroutines              | 26.1 ms                                                | 25.5 ms: 1.02x faster                                                      |
| pprint_safe_repr        | 691 ms                                                 | 676 ms: 1.02x faster                                                       |
| deepcopy_reduce         | 2.97 us                                                | 2.91 us: 1.02x faster                                                      |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                                      |
| async_generators        | 359 ms                                                 | 354 ms: 1.01x faster                                                       |
| thrift                  | 752 us                                                 | 743 us: 1.01x faster                                                       |
| pickle_dict             | 31.4 us                                                | 31.0 us: 1.01x faster                                                      |
| xml_etree_process       | 53.8 ms                                                | 53.1 ms: 1.01x faster                                                      |
| crypto_pyaes            | 73.9 ms                                                | 73.1 ms: 1.01x faster                                                      |
| dulwich_log             | 63.9 ms                                                | 63.3 ms: 1.01x faster                                                      |
| coverage                | 101 ms                                                 | 99.5 ms: 1.01x faster                                                      |
| pidigits                | 199 ms                                                 | 198 ms: 1.01x faster                                                       |
| xml_etree_iterparse     | 103 ms                                                 | 102 ms: 1.01x faster                                                       |
| pickle_list             | 4.17 us                                                | 4.15 us: 1.01x faster                                                      |
| xml_etree_generate      | 76.2 ms                                                | 76.7 ms: 1.01x slower                                                      |
| meteor_contest          | 105 ms                                                 | 106 ms: 1.01x slower                                                       |
| regex_effbot            | 3.36 ms                                                | 3.40 ms: 1.01x slower                                                      |
| async_tree_io           | 1.31 sec                                               | 1.33 sec: 1.01x slower                                                     |
| django_template         | 32.5 ms                                                | 32.9 ms: 1.02x slower                                                      |
| sqlglot_transpile       | 1.66 ms                                                | 1.69 ms: 1.02x slower                                                      |
| unpickle_list           | 4.95 us                                                | 5.07 us: 1.02x slower                                                      |
| sqlglot_parse           | 1.37 ms                                                | 1.40 ms: 1.03x slower                                                      |
| regex_dna               | 203 ms                                                 | 210 ms: 1.04x slower                                                       |
| nbody                   | 95.0 ms                                                | 98.9 ms: 1.04x slower                                                      |
| python_startup          | 8.36 ms                                                | 8.72 ms: 1.04x slower                                                      |
| sqlite_synth            | 2.49 us                                                | 2.60 us: 1.04x slower                                                      |
| pickle                  | 9.79 us                                                | 10.3 us: 1.05x slower                                                      |
| python_startup_no_site  | 5.96 ms                                                | 6.25 ms: 1.05x slower                                                      |
| async_tree_memoization  | 625 ms                                                 | 667 ms: 1.07x slower                                                       |
| generators              | 72.2 ms                                                | 78.1 ms: 1.08x slower                                                      |
| mypy                    | 669 ms                                                 | 805 ms: 1.20x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (5): unpickle, async_tree_none, bench_mp_pool, unpack_sequence, async_tree_cpu_io_mixed
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230202-3.12.0a4+-fa5965d/bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal