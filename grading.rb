a, b, c, d, e = gets.split.map(&:to_i)
score = gets.to_i
puts score >= a ? 'A' : score >= b ? 'B' : score >= c ? 'C' : score >= d ? 'D' : score >= e ? 'E' : 'F'