while (s = gets.strip) != '#'
  s[-1] = s.count('1').even? ^ (s[-1] == 'e') ? '1' : '0'
  puts s
end