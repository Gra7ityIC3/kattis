n, k = gets.split.map(&:to_i)
freq = Array.new(k, 0)
gets.split.map(&:to_i).each { |x| freq[x - 1] += 1 }
min = freq.min
ans = (1..k).select { |i| freq[i - 1] == min }
puts ans.size, ans.join(' ')