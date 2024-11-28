a, n = gets.split.map(&:to_f)
puts n * n / 4 / Math::PI >= a ? 'Diablo is happy!' : 'Need more materials!'