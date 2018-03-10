import os
import sys
import argparse

import subprocess

program_name = 'math_md_to_pdf'
version = '0.1.1'

module_dir = os.path.dirname(os.path.abspath(__file__))
default_latex_template = os.path.join(module_dir, 'templates', 'latex',
	'default-1.17.0.2.tex')

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
		'-l', '--keep_latex', action='store_true',
		help="Keep LaTeX files used to generated PDF.")

	parser.add_argument(
		'-k', '--knit', action='store_true',
		help="Pass through RMarkdown's knitr first."
		)

	parser.add_argument(
		'-s', '--show_pdf', action='store_true',
		help="Show the PDF after rendering. Uses xdg-open."
		)

	parser.add_argument(
		'-v', '--verbose', action='store_true',
		help="Display verbose output messages.")

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
		knit_proc = subprocess.run([
		'Rscript', '-e', 
		"\"library(knitr); setwd('{:s}'); knit('{:s}', output='{:s}')\"".format(
			md_dir, 
			md_filename + '.md',
			md_filename + '.utf8.md'
			)
		],
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		universal_newlines=True)

		print(knit_proc.stdout, end='')
		print(knit_proc.stderr, end='')

		# Knitted, change intermediate markdown path
		md_intermediate_filepath = \
			os.path.join(md_dir, md_filename + '.utf8.md')

	# Render the PDF from the Markdown
	pdf_proc = subprocess.run(['pandoc',
		'+RTS', '-K512m', '-RTS', 
		md_intermediate_filepath,
		'--to', 'latex',
		'--from', 'markdown+' + \
					'autolink_bare_uris+' + \
					'ascii_identifiers+' + \
					'tex_math_single_backslash',
		'--output', os.path.join(md_dir, md_filename + '.pdf'),
		'--template', latex_template_path,
		'--highlight-style', 'tango',
		'--latex-engine', 'pdflatex',
		'--variable', 'graphics=yes',
		],
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		universal_newlines=True)

	print(pdf_proc.stdout, end='')
	print(pdf_proc.stderr, end='')

	# Render the latex that generated the PDF (kind of redundant, but necessary)
	if args.keep_latex:

		tex_proc = subprocess.run(['pandoc',
			'+RTS', '-K512m', '-RTS', 
			md_intermediate_filepath,
			'--to', 'latex',
			'--from', 'markdown+' + \
						'autolink_bare_uris+' + \
						'ascii_identifiers+' + \
						'tex_math_single_backslash',
			'--output', os.path.join(md_dir, md_filename + '.tex'),
			'--template', latex_template,
			'--highlight-style', 'tango',
			'--latex-engine', 'pdflatex',
			'--variable', 'graphics=yes',
			],
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE,
			universal_newlines=True)

		print(tex_proc.stdout, end='')
		print(tex_proc.stderr, end='')

	if args.show_pdf:
		# Open the PDF with nohupped XDG
		xdg_proc = subprocess.run(['nohup', 'xdg-open', 
			os.path.join(md_dir, md_filename + '.pdf')],
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE,
			universal_newlines=True)

		# print(xdg_proc.stdout, end='')
		# print(xdg_proc.stderr, end='')

if __name__ == '__main__':
	main()
