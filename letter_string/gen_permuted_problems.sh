#!/bin/zsh
   
for i in {1..2}; 
    do echo generating problem $i; python gen_problems.py --num_permuted $i;
done
