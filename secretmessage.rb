gets.to_i.times do
  m = gets.chomp!
  L = m.length
  K = ((L - 1) ** 0.5 + 1).to_i
  ans = Array.new(K) { Array.new(K, '') }
  L.times { |i| ans[i % K][K - 1 - i / K] = m[i] }
  puts ans.join
end