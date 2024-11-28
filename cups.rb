Array.new(gets.to_i) do
  a, b = gets.split
  a.match?(/\D/) ? [b.to_i, a] : [a.to_i / 2, b]
end.sort!.each { |_, color| puts color }