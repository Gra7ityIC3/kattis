def solve(v)
  return 0, v[-1] if v.uniq.size == 1
  d, x = solve(v.each_cons(2).map { |a, b| b - a })
  [d + 1, x + v[-1]]
end

_, *v = gets.split.map(&:to_i)
puts solve(v).join(' ')