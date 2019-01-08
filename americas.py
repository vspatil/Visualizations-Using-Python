from pygal.maps.world import World

wm = World()
#wm.force_uri_protocol = 'http'
wm.title = 'North, Central, and South America'
#wm.title = 'North Americas!'

#wm.add('North America', {'ca':34126000,'mx':11342300,'us':309349000})
wm.add('North America',['ca','mx','us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
   'gy', 'pe', 'py', 'sr', 'uy', 've'])
wm.render_to_file('americas.svg')
#wm.render_to_file('na.svg')
