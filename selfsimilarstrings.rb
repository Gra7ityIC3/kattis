$<.each do |s|
  ans = 0
  (1...s.length - 1).each do |d|
    freq = Hash.new(0)
    (0...s.length - d).each { |i| freq[s[i, d]] += 1}
    break if freq.values.any? { |v| v == 1 }
    ans = d
  end
  puts ans
end