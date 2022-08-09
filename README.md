# host_gen
host_gen is a simple `/etc/hosts` adblocker.

> All software in here is provided with absolutly no responsibillity and warrenty

## Installation and Usage
Clone the repository.
```bash
$ git clone https://github.com/michaeljo94/host_gen.git .
```

Create white- and blacklists to generate entries.
```bash
$ tree .
├── data
│   ├── blocklist
│   │   └── blocklist.txt
│   └── whitelist
│       └── whitelist.txt
├── host_gen
│   ├── __init__.py
│   └── __main__.py
└── README.md
```

Run the generator.
```bash
$python -m host_gen
```
