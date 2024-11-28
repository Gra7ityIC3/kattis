L, H = gets.split.map(&:to_i)
ans = (L..H).count do |c|
  digits = c.digits
  digits.uniq.size == 6 && digits.all? { |d| d != 0 && c % d == 0 }
end
puts ans