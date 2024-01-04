#create a manifest that kills a process named killmenow
exec { 'killmeno':
command => 'pkill
killmenow',
onlyif => 'pgrep
killmenow',
path => ['/bin', '/usr/bin'],
refreshonly => true,
}
