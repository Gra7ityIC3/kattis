require 'prime'

while (x = gets.to_i) != 4
  cnt = 1
  until x.prime?
    x = x.prime_division.sum { |p, e| p * e }
    cnt += 1
  end
  puts "#{x} #{cnt}"
end