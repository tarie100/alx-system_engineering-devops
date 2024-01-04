#!/usr/bin/env ruby
<<<<<<< HEAD
puts ARGV[0].scan(/(?<=from:|to:|flags:).+?(?=\])/).join(',')
=======
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
>>>>>>> 269dc26ac6c7424f908be15fa21b92766c9d7ab2
