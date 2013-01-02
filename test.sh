#!/bin/bash
read_pipe=$1
write_pipe=$2

read <&$read_pipe line

echo "This is not shown in the readback but only in stdout"
echo "very nice $line" >&$write_pipe
echo "very bad error" >&2
