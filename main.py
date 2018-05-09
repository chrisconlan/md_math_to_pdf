import os
import sys
import argparse

import subprocess

from .config import *
from .utils import subprocess_exec

program_name = 'md_math_to_pdf'
version = '0.1.2'

def main():

	parser = argparse.ArgumentParser(
		prog=program_name + ' v' + version,
		description=program_name + ' v' + version + ': ' + \
			"""
			Utility for rendering math-enabled markdown documents to PDF format 
			and reserving latex output. Neatly packages the defaults of 
			RMarkdown's knitr, but without the code execution. Requires pandoc 
			and python. Requires R for knitr functionality.
			""",
		formatter_class=lambda prog:
			argparse.ArgumentDefaultsHelpFormatter(prog, max_help_position=20))	

	parser.add_argument(
		'mdfile', metavar='mdfile', type=str,
		help="""
			Math-enabled Markdown file to render.
			""")

	parser.add_argument(
		'-t', '--template', type=str, default=default_latex_template,
		help="""
		Latex template to render markdown.
		""")

	parser.add_argument(
		'-l', '--keep-latex', action='store_true',
		help="Keep LaTeX files used to generated PDF.")

	parser.add_argument(
		'-k', '--knit', action='store_true',
		help="Pass through RMarkdown's knitr first."
		)

	parser.add_argument(
		'-x', '--show-pdf-xdg', action='store_true',
		help="Show the PDF after rendering. Uses xdg-open."
		)

	parser.add_argument(
		'-c', '--show-pdf-chrome', action='store_true',
		help="Show the PDF after rendering using Google Chrome."
		)

	# parser.add_argument(
	# 	'-v', '--verbose', action='store_true',
	# 	help="Display verbose output messages.")

	args = parser.parse_args()

	# Save a littany of paths and dirs
	term_cwd = os.path.abspath(os.getcwd())

	md_basename = os.path.basename(args.mdfile)
	md_filename = os.path.splitext(md_basename)[0]
	md_filepath = os.path.abspath(args.mdfile)
	md_dir = os.path.dirname(md_filepath)

	md_intermediate_filepath = os.path.join(md_dir, md_filename + '.md')
	latex_template_path = os.path.abspath(args.template)

	os.chdir(md_dir)

	# Execute and interleave the code if you want, using knitr
	if args.knit:
		r_code_on_the_fly = \
			'library(knitr); setwd("{:s}"); knit("{:s}", output="{:s}")'.format(
				md_dir, 
				md_filename + '.md',
				md_filename + '.knit.md'
			)

		subprocess_exec(['Rscript', '-e', r_code_on_the_fly])

		# If knitted, change intermediate markdown path
		md_intermediate_filepath = \
			os.path.join(md_dir, md_filename + '.knit.md')

	pandoc_args = [pandoc_path,
		*memory_usage_args,
		md_intermediate_filepath,
		*output_args,
		*input_args,
		'--template', latex_template_path,
		*highlight_args,
		*pdf_engine_args,
		*geometry_args,
		*extra_args,
	]
	pdf_outpath = os.path.join(md_dir, md_filename + '.pdf')
	tex_outpath = os.path.join(md_dir, md_filename + '.tex')

	# Render the PDF from the Markdown
	subprocess_exec(pandoc_args + ['--output', pdf_outpath])

	# Render the latex that generated the PDF (redundant, but necessary)
	if args.keep_latex:
		subprocess_exec(pandoc_args + ['--output', tex_outpath])

	if args.show_pdf_xdg:
		# Open the PDF with nohupped XDG
		subprocess_exec([
			'nohup', 'xdg-open', 
			os.path.join(md_dir, md_filename + '.pdf')
			],
			verbose=False)

	if args.show_pdf_chrome:
		# Open the PDF with Chrome
		subprocess_exec([
			'google-chrome', 
			os.path.join(md_dir, md_filename + '.pdf')
			],
			verbose=False)


if __name__ == '__main__':
	main()
