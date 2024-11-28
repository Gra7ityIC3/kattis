p, q, s = gets.split.map(&:to_i)
puts p.lcm(q) <= s ? 'yes' : 'no'