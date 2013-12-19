# To make Python3 work with sublimetext

# 1. Go to tools/build system/build new system

# 2. Paste in this (if you have Anaconda installed)

{
    "cmd":  ["/Users/chrisralbon/anaconda/envs/python3/bin/python3", "-u", "$file"],
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.python"
}

