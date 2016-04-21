# Bash.profile script written for me by Henry.
# V.1.0_21/04/16

# .bash_profile

# This get's the aliases and functions
if [ -f ~/.bashrc ]; then
    . ~/.bashrc
fi

# Here I can specify my environment and startup programs. If you edit this, then refresh your current connection to Icerberg.

PATH=$PATH:$HOME/bin
PATH=$PATH:/usr/local/extras/Genomics/bin
PATH=$PATH:/home/bop15job/mrbayes-3.2.6

export PATH
