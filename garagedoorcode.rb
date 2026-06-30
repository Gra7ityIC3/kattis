require 'set'

k, n = gets.split.map(&:to_i)
ans = Array.new(n) { gets.chomp.chars.combination(k).map(&:join).to_set }.reduce(:&).sort
puts ans.size, ans