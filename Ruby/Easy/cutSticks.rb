#!/bin/ruby

require 'json'
require 'stringio'

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr)
    # Write your code here
    rel = []
    while arr.length > 0
        rel.push(arr.length)
        arr.delete(arr.min)
    end
    return rel;
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

n = gets.strip.to_i

arr = gets.rstrip.split.map(&:to_i)

result = cutTheSticks arr

fptr.write result.join "\n"
fptr.write "\n"

fptr.close()
