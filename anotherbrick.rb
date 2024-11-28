def solve(h, w, n)
  sum = 0
  gets.split.map(&:to_i).each do |x|
    sum += x
    if sum == w
      h -= 1
      return 'YES' if h == 0
      sum = 0
    elsif sum > w
      return 'NO'
    end
  end
  'NO'
end

puts solve(*gets.split.map(&:to_i))