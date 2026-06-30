n = gets.to_i
trades = Array.new(n) { gets.split.map(&:to_i) }
trades.sort! do |(g1, r1), (g2, r2)|
  cmp = r2 * g1 <=> r1 * g2
  cmp.zero? ? g2 <=> g1 : cmp
end
trades.each { |g, r| puts "#{g} #{r}" }