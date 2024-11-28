s = ''
gets.each_char { |c| c == '<' ?  s.chop! : s << c }
puts s