require 'prime'

while (n = gets.to_i) != 0
  i = 2 * n + 1
  i += 2 until i.prime?
  puts n.prime? ? i : "#{i} (#{n} is not prime)"
end