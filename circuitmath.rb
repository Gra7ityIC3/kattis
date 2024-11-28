gets
values = gets.split.map { |c| c == 'T' }
stack = []
gets.split.each do |c|
  case c
  when '*' then stack.push(stack.pop & stack.pop)
  when '+' then stack.push(stack.pop | stack.pop)
  when '-' then stack.push(!stack.pop)
  else stack.push(values[c.ord - 65])
  end
end
puts stack.pop ? 'T' : 'F'