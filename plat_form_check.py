import platform


def get_distribution_info():
	# return distribution name and major version
	if platform.system() == "Linux":
		current_dist = platform.dist()
		print(current_dist[0].lower(), current_dist[1].rsplit('.')[0])

	elif platform.system() == "Darwin":
		current_dist = platform.mac_ver()
		print("macos", current_dist[0].rsplit('.', 1)[0]) 

get_distribution_info()