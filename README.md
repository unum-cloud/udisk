# UDisk

The fastest ACID-transactional persisted Key-Value store designed for NVMe block-devices with GPU-acceleration and SPDK to bypass the Linux kernel.

## Configuration Parameters

Most important parameters:

- `storage_disks`: Where to put the data? A RAID array?
- `main_dir_path`: Where to persist the schema? The boot drive?
- `mem_limit`: How much RAM to use? 80% of it?
- `unfixed_value_max_size`: How large the values can get?
- `gpu_devices`: Do you a have a GPU we can borrow for acceleration?

### Versioning

```json
"unumdb_version": 0.3.0
"options_file_version": 0.7
```

### Disk IO

Path where there database would store metadata:

```json
"main_dir_path": "./tmp"
```

Paths where the database would store data, with tuples containing the path and a limit:

```json
"storage_disks": [
    ["/mnt/md0/ukv/", 1e12],
    ["/mnt/md1/ukv/", 1e12]
]
```

Underlying IO mechanism, can be `pulling`, `posix`:

```json
"io_device_name": "pulling"
```

For asynchronous IO mechanisms you can set the queue depth:

```json
"io_device_queue_depth": 4096
```

### Random Access Memory

Limit the total amount of RAM available to the database:

```json
"mem_limit": 1000000000
```

Limit the amount of memory to be used for caching.
Greatly affects the performance of single reads.
Doesn't affect the performance of batch reads.

```json
"read_cache_capacity_bytes": 100000000
```

Limit the maximum number of entries to be collected in-memory (and in the Write Ahead Log), before flushing them into files.

```json
"write_cache_max_cnt": 100000
```

Limit the maximum combined size of entries to be collected in-memory (and in the Write Ahead Log), before flushing them into files.

```json
"write_cache_capacity_bytes": 100000000
```

### Hardware Acceleration

Background threads to be used for compactions and non-blocking garbage collection:

```json
"background_threads_cnt": 1
```

Define, how many threads may be accessing the database concurrently:

```json
"access_concurrency": 64
```

Optional array of integer identifiers for the GPUs to be used for background compactions:

```json
"gpu_devices": []
```

The amount of Video RAM available to UDisk on the GPU:

```json
"gpu_mem_limit": 1000000000
```

### Structure

Define, how large the biggest value can be:

```json
"unfixed_value_max_size": 4096
```

In some rare cases, you may have all of your values of the same size:

```json
"fixed_value_size": 0
```

Define, how much larger every layer of the Log-Structured-Merge Tree can get:

```json
"level_enlarge_factor": 4
```

How large the top-level of the Log-Structured-Merge Tree should be?

```json
"l0_capacity_bytes": 1000000000
```

### Transactions

The maximum number of entries to be updated with a single transaction:

```json
"txn_write_cache_max_cnt": 100000
```

The maximum capacity of a single transaction, limiting the size of all updates in it:

```json
"txn_write_cache_capacity_bytes": 100000000
```
