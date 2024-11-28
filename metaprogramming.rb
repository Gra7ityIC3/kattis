h = {}
$<.each do |line|
  cmd = line.split
  if cmd[0] == 'define'
    h[cmd[2]] = cmd[1].to_i
  else
    x, y, z = cmd[1..]
    puts h[x] && h[z] ? eval("#{h[x]} #{y.gsub('=', '==')} #{h[z]}") : 'undefined'
  end
end