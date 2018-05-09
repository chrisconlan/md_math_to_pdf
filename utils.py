import subprocess

def subprocess_exec(cmd_args, verbose=True):
	some_subprocess = subprocess.run(cmd_args, 
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		universal_newlines=True)

	if verbose:
		print(some_subprocess.stdout, end='')
		print(some_subprocess.stderr, end='')

	return some_subprocess
