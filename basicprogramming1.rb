n, t = gets.split.map(&:to_i)
a = gets.split.map(&:to_i)
case t
when 1
  puts 7
when 2
  puts a[0] > a[1] ? 'Bigger' : a[0] == a[1] ? 'Equal' : 'Smaller'
when 3
  puts a[0..2].sort![1]
when 4
  puts a.sum
when 5
  puts a.select(&:even?).sum
when 6
  puts a.map { |x| (x % 26 + 97).chr }.join
else
  def solve(a, n)
    i = 0
    loop do
      a[i], i = -1, a[i]
      return 'Out' if i >= n
      return 'Done' if i == n - 1
      return 'Cyclic' if a[i] == -1
    end
  end
  puts solve(a, n)
end