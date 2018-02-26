from bin_8 import cli, hello, bye, brain

n = cli.get_name()
hello.hello(n)
while True:
	s = cli.get_option()
	if s in ["A" or "a"]:
		q = input("Please enter a yes or no question\n")
		resp = brain.consider(q)
		print("<><><><>\n  {}\n<><><><>".format(resp))
	else:
		bye.bye(n)
		break

