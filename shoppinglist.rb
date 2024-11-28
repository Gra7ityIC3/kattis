require 'set'

n, m = gets.split.map(&:to_i)
ans = Array.new(n) { gets.split.to_set }.reduce(:&)
puts ans.size, ans.sort