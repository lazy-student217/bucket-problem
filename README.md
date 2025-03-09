This project consists of a python file: `bucket_problem.py`. This python script is used to execute BFS on the graph of the bucket problem.

This is designed for the private series "9up 小日常". Details can be found in `episode2.pdf`.

## Bucket problem

Bucket problem is a class of problems like this: If I have a 3L bucket and a 5L bucket, assuming I have infinite amount of water, how can I get a bucket with 4L of water? This project explores the state changes of buckets using basic graph thoery and related algorithm. 

## Usage

Execute the program, you may see a prompt `Buckets capacity: `. You can enter the capacity of buckets like this: `3|5`, each number represented the capacity of each bucket, sperated by `|`. Then, the program asked for the initital state, which can be leave out to use the default value (all buckets are empty), volumes of water in each bucket can be specified using the format above. 

This programs output the minimal steps to reach any reachable state (where state is denoted using the format above) and some data, including amount reachable of state, ideal amount of state and the cover rate.


