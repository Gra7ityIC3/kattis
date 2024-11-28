_, code, guess = gets.split.map(&:chars)
c, d = code.tally, guess.tally
r = code.zip(guess).count { |a, b| a == b }
s = (c.keys & d.keys).sum { |k| [c[k], d[k]].min } - r
puts "#{r} #{s}"