n = gets.to_i
tA, dA = gets.split.map(&:to_i)
tB, dB = gets.split.map(&:to_i)
puts ['=', 'Bob', 'Alice'][2 * tA + dA * (n - 1) <=> 2 * tB + dB * (n - 1)]