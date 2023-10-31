#!/usr/bin/env ruby
def match_string(input)
  regex = /^h.n$/
  if input.match?(regex)
    puts "The string '#{input}' matches the regular expression!"
  else
    puts "The string '#{input}' does not match the regular expression."
  end
end

# Accepting user input as argument
argument = ARGV[0]

# Calling the method with the provided argument
match_string(argument)
