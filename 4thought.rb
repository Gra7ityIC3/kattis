ops = ['+', '-', '*', '/']
h = Hash.new('no solution')
ops.product(ops, ops).each do |a, b, c|
  n = eval(ans = "4 #{a} 4 #{b} 4 #{c} 4")
  h[n] = "#{ans} = #{n}"
end
gets.to_i.times { puts h[gets.to_i] }