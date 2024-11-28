n, p = gets.split.map(&:to_i)
puts p == 100 ? 'impossible' : ((p * n - gets.split.map(&:to_i).sum) / (100.0 - p)).ceil