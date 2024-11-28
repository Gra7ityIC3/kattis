n, m = gets.split.map(&:to_i)
puts *([n, m].min + 1).upto([n, m].max + 1)