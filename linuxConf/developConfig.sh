#!/bin/bash

tmux has-session -t development
if [ $? != 0 ]
then
    tmux new-session -s development -n basic -d
    tmux new-window -n go -t development
    tmux new-window -n docker -t development
    
    tmux send-keys -t development:0 'cd /root/' C-m 'clear' C-m
    tmux send-keys -t development:1 'cd /root/coding/leego/' C-m 'clear' C-m
    tmux send-keys -t development:2 'cd /root/coding/leedocker' C-m 'clear' C-m
    tmux select-window -t development:0
fi
tmux -2 attach -t development