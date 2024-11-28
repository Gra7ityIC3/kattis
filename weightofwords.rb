def solve(l, w)
  s = ''
  while w - l > 25
    s << 'z'
    w -= 26
    l -= 1
  end
  s + 'a' * (l - 1) + (w - l + 97).chr
end

l, w = gets.split.map(&:to_i)
puts l <= w && w <= 26 * l ? solve(l, w) : 'impossible'