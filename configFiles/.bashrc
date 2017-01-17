#	~/.bashrc shell configuration file
#
#	This file contains configuration commands which will
#	be executed for each interactive non-login shell (e.g. 
#	a terminal emulator or which starts up (e.g., each
#	shell window, and most commands given to the shell).
#	Changes to this file will NOT take effect in existing
#	shells unless you give the shell-level command "source ~/.bash_profile",
#	but they WILL take effect in shells created after you
#	change this file.

# Begin by including the "standard" configuration file, which will
# configure this shell according to the local standard configuration.
# NOTE:  IF YOU DON'T DO THIS, YOU ARE RESPONSIBLE FOR TRACKING ANY
# CHANGES WHICH ARE MADE TO THE STANDARD CONFIGURATION!!!

##########source /usr/local/lib/config/Bash_Profile

# Here is where you should put any changes you wish to make to the 
# standard configuration (e.g., altering the search path, redefining
# the prompt, etc.)

alias l="ls"
alias la="ls -a"
alias ll="ls -l"
alias alrt="ls -alrt"

alias spawn="gnome-terminal &"

#Colors!
PS1='\u@\h \[\e[33m\]\W\[\e[m\] \[\e[33m\]\$\[\e[m\] '

# one-liner for every commit
alias gitlog="git log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

# lists each branch with age, name, and last committer
alias glist='for ref in $(git for-each-ref --sort=-committerdate --format="%(refname)" refs/heads/ refs/remotes ); do git log -n1 $ref --pretty=format:"%Cgreen%cr%Creset %C(yellow)%d%Creset %C(bold blue)<%an>%Creset%n" | cat ; done | awk '"'! a["'$0'"]++'"

PATH=$PATH:~/scripts

#custom stuff
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color'
    LS_COLORS='di=36:fi=0:ln=31:pi=41:ex=91:*.png=37:*.jpg=37:*.gif=37:*.js=32:*.html=32:*.css=32:*.java=32'
    export LS_COLORS
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi
