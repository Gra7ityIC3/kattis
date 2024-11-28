m, n, t = gets.split.map(&:to_i)

case t
when 1
  puts n < 13 && Math.gamma(n + 1) <= m ? 'AC' : 'TLE'
when 2
  puts n < 30 && 2 ** n <= m ? 'AC' : 'TLE'
when 3
  puts n ** 4 <= m ? 'AC' : 'TLE'
when 4
  puts n ** 3 <= m ? 'AC' : 'TLE'
when 5
  puts n ** 2 <= m ? 'AC' : 'TLE'
when 6
  puts n * Math.log2(n) <= m ? 'AC' : 'TLE'
else
  puts n <= m ? 'AC' : 'TLE'
end