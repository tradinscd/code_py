# Running iPython with Anaconda's Python 3

1. Open the terminal

2. Run:

export PATH=/Users/chrisralbon/anaconda/envs/py3k/bin:$PATH
ipython notebook

# How to install a module, in this case pandas

export PATH=/Users/chrisralbon/anaconda/envs/py3k/bin:$PATH
pip install pandas 

# To make Python3 work with sublimetext

1. Go to tools/build system/build new system

2. Paste in this (if you have Anaconda installed)

{
	"cmd":  ["/Users/chrisralbon/anaconda/envs/py3k/bin/python3", "-u", "$file"],
	"file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
	"selector": "source.python"
}
