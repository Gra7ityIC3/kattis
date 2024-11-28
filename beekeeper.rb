while (n = gets.to_i) != 0
  puts Array.new(n) { gets }.max_by { |x| x.scan(/(aa|ee|ii|oo|uu|yy)/).size }
end