import os

module_dir = os.path.dirname(os.path.abspath(__file__))

"""
The latex template file used if none is specified in command line args
"""
default_latex_template = os.path.join(module_dir, 'templates', 'latex',
	'default.tex')


"""
Either the bash command for pandoc, or path to pandoc binary
"""
pandoc_path = 'pandoc'


"""
The latex-to-pdf renderer used by Pandoc, and the argument used to denote it.

+ Use --latex-engine if using pandoc 1.*
+ Use --pdf-engine if using pandoc 2.*

Examples:
pdf_engine_args = ('--latex-engine', 'pdflatex')
pdf_engine_args = ('--pdf-engine', 'xelatex')
"""
pdf_engine_args = ('--latex-engine', 'pdflatex')


"""
Define the maximum memory usage for Pandoc. It can use a lot of memory
for certain applications, but 512MB is almost always sufficient for PDF's.

Examples:
memory_usage_args = ('+RTS', '-K2048m', '-RTS')
memory_usage_args = ('+RTS', '-K128m', '-RTS')
"""
memory_usage_args = ('+RTS', '-K512m', '-RTS')


"""
Pandoc has a ton of extensions. A lot of the most useful ones are enabled by
default. 

Run:
pandoc --list-available

to list all available extensions, and view their default status.
"""
input_format = 'markdown'
extension_list = [
	# '+lists_without_preceding_blankline',
	# '+hard_line_breaks',
	# '+ignore_line_breaks',
	# '+east_asian_line_breaks',
	# '+emoji',
	# '+tex_math_single_backslash',
	# '+tex_math_double_backslash',
	# '+markdown_attribute',
	# '+mmd_title_block',
	# '+abbreviations',
	'+autolink_bare_uris',
	'+ascii_identifiers',
	# '+mmd_link_attributes',
	# '+mmd_header_identifiers',
	# '+compact_definition_lists',
	# '+escaped_line_breaks',
	# '+blank_before_header',
	# '+header_attributes',
	# '+auto_identifiers',
	# '+implicit_header_references',
	# '+blank_before_blockquote',
	# '+fenced_code_blocks',
	# '+backtick_code_blocks',
	# '+fenced_code_attributes',
	# '+line_blocks'
	# '+fancy_lists',
	# '+startnum',
	# '+definition_lists',
	# '+example_lists',
	# '+pipe_tables'
	# '+table_captions',
	# '+simple_tables',
	# '+multiline_tables',
	# '+grid_tables',
	# '+pandoc_title_block'
	# '+yaml_metadata_block',
	# '+all_symbols_escapable',
	# '+strikeout',
	# '+superscript',
	# '+subscript',
	# '+inline_code_attributes',
	# '+tex_math_dollars',
	# '+raw_html',
	# '+markdown_in_html_blocks',
	# '+native_divs',
	# '+native_spans',
	# '+raw_tex',
	# '+latex_macros',
	# '+shortcut_reference_links',
	# '+implicit_figures',
	# '+link_attributes',
	# '+footnotes'
	# '+inline_notes',
	# '+citations',
]

input_args = ('--from', input_format + ''.join(extension_list))


"""
Output args

Can be:
output_args = ('--to', 'latex')
output_args = ('--to', 'html')
output_args = ('--to', 'docx')
"""
output_args = ('--to', 'latex')


"""
Highlight style
"""
highlight_args = ('--highlight-style', 'tango',)


"""
Geometry style

Examples:
-V geometry:"top=2cm, bottom=1.5cm, left=1cm, right=1cm"
-V geometry:"left=3cm, width=10cm"
"""
geometry_args = ('-V', 'geometry:margin=1in')


"""
Any extra args
"""
extra_args = ()
