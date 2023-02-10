# UDisk

The fastest ACID-transactional persisted Key-Value store designed for NVMe block-devices with GPU-acceleration and SPDK to bypass the Linux kernel.

## Configuration Parameters

Most important parameters:

- `directory_main`: Where to keep the configs, schemas, data, and logs? The boot drive?
- `memory_limit`: How much RAM to use? 80% of it?
- `value_max_size`: How large the values can get?

Tuning performance?

- `directories_data`: Want to separate large data and put it on some RAID array?
- `gpu_devices`: Do you a have a GPU we can borrow for acceleration?

### Versioning

```json
"udisk_version": 0.3.0
"options_file_version": 0.7
```

### Disk IO

Path where there database would store metadata:

```json
"directory": "/etc/udisk/"
```

Paths where the database would store data, with tuples containing the path and a limit:

```json
"data_directories": [
    {
        "path": "/mnt/md0/ukv/",
        "max_size": 1e12,
    },
    {
        "path": "/mnt/md1/ukv/",
        "max_size": 1e12,
    }
]
```

Choose the underlying IO mechanism:

```json
"io_mechanism": "posix"
"io_mechanism": "pulling"
"io_mechanism": "polling"
```

For asynchronous IO mechanisms you can set the queue depth:

```json
"io_queue_depth": 4096
```

### Random Access Memory

Limit the total amount of RAM available to the database:

```json
"memory_limit": 1000000000
```

Limit the amount of memory to be used for caching.
Greatly affects the performance of single reads.
Doesn't affect the performance of batch reads.

```json
"cache_limit": 100000000
```

Limit the maximum number of entries to be collected in-memory (and in the Write Ahead Log), before flushing them into files.

```json
"write_buffer_max_elements": 100000
```

Limit the maximum combined size of entries to be collected in-memory (and in the Write Ahead Log), before flushing them into files.

```json
"write_buffer_max_bytes": 100000000
```

### Hardware Acceleration

Background threads to be used for compactions and non-blocking garbage collection:

```json
"background_threads": 1
```

Define, how many threads may be accessing the database concurrently:

```json
"max_access_threads": 64
```

Optional array of integer identifiers for the GPUs to be used for background compactions:

```json
"gpu_devices": "all"
"gpu_devices": [0, 1, 2, 3]
```

The amount of Video RAM available to UDisk on the GPU:

```json
"gpu_memory_limit": 1000000000
```

### Structure

Define, how large the biggest value can be:

```json
"value_max_size": 4096
```

In some rare cases, you may have all of your values of the same size:

```json
"value_size": 0
```

Define, how much larger every layer of the Log-Structured-Merge Tree can get:

```json
"level_enlarge_factor": 4
```

How large the top-level of the Log-Structured-Merge Tree should be?

```json
"first_level_max_bytes": 1000000000
```

### Transactions

The maximum number of entries to be updated with a single transaction:

```json
"transaction_max_elements": 100000
```

The maximum capacity of a single transaction, limiting the size of all updates in it:

```json
"transaction_max_bytes": 100000000
```
