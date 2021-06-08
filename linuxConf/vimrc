set nocompatible


" Specify a directory for plugins
call plug#begin('~/.vim/plugged')

Plug 'junegunn/vim-easy-align'

"colorscheme
Plug 'morhetz/gruvbox'

"gutentags
Plug 'ludovicchabant/vim-gutentags'

"ale
"Plug 'w0rp/ale'

"leaderF instead of tagbar
"Plug 'yggdroot/leaderf'

"signify
Plug 'mhinz/vim-signify'

"vim-cpp-enhanced-highlight
Plug 'octol/vim-cpp-enhanced-highlight'

"easy-motion
Plug 'easymotion/vim-easymotion'

"YCM
Plug 'Valloric/YouCompleteMe'

"delimitmate instead of auto-pairs
Plug 'raimondi/delimitmate'

"multiple-cursors
Plug 'terryma/vim-multiple-cursors'

"airline
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

"cscope
Plug 'chazy/cscope_maps'

"indentline
Plug 'yggdroot/indentline'

"nerd commenter
Plug 'scrooloose/nerdcommenter'

"延迟加载
"nerdtree
Plug 'scrooloose/nerdtree', { 'on':  'NERDTreeToggle' }

"end of 延迟加载

" Initialize plugin system
call plug#end()

"vim own setting"


"use256 color
set t_Co=256

"语法高亮
syntax enable

"colorscheme
set background=dark
colorscheme  gruvbox

" 定义快捷键的前缀，即<Leader>
let mapleader=";"

" 总是显示状态栏
set laststatus=2
" 显示光标当前位置
set ruler
" 开启行号显示
set number
" 高亮显示当前行/列
set cursorline
set cursorcolumn
" 高亮显示搜索结果
set hlsearch
set incsearch

"禁止光标闪烁
set gcr=a:block-blinkon0
" 禁止显示滚动条
set guioptions-=l
set guioptions-=L
set guioptions-=r
set guioptions-=R

" 将制表符扩展为空格
set expandtab
" 设置编辑时制表符占用空格数
set tabstop=4
" 设置格式化时制表符占用空格数
set shiftwidth=4
" 让 vim 把连续数量的空格视为一个制表符
set softtabstop=4
" 基于缩进或语法进行代码折叠
"set foldmethod=indent
set foldmethod=syntax
" 启动 vim 时关闭折叠代码
set nofoldenable
"show partial commands in the last line of the screen
set showcmd
set showmode
"enable use of the mouse for all modes
set mouse=a
"backspace to the uppper line
:set backspace=2

"vi中所有数字都为10机制
set nrformats=

"vi man page
source $VIMRUNTIME/ftplugin/man.vim
cmap man Man
nmap K :Man <cword><CR>

"to the end of line
inoremap <leader>e <esc>A

set scrolljump=5
set scrolloff=5
set sidescroll=3
set sidescrolloff=3

"定义折叠方式 
set fdm=indent

"设置字体
set guifont=Monaco:h16


"修改vi编码格式以使其支持中文
set fileencodings=utf-8,gb2312,gb18030,gbk,ucs-bom,cp936,latin1

"end of vim own setting

"修复macvim No module name encodings
if has('python3')
    command! -nargs=1 Py py3 <args>
    set pythonthreedll=/usr/local/Frameworks/Python.framework/Versions/3.6/Python
    set pythonthreehome=/usr/local/Frameworks/Python.framework/Versions/3.6
else
    command! -nargs=1 Py py <args>
    set pythondll=/usr/local/Frameworks/Python.framework/Versions/2.7/Python
    set pythonhome=/usr/local/Frameworks/Python.framework/Versions/2.7
endif

"end of macvim repair

"tags config
set tags=./tags;,.tags

"plugin config

"guntentags config
" gutentags 搜索工程目录的标志，碰到这些文件/目录名就停止向上一级目录递归
let g:gutentags_project_root = ['.root', '.svn', '.git', '.hg', '.project']

" 所生成的数据文件的名称
let g:gutentags_ctags_tagfile = 'tags'

" 将自动生成的 tags 文件全部放入 ~/.cache/tags 目录中，避免污染工程目录
let s:vim_tags = expand('~/.cache/tags')
let g:gutentags_cache_dir = s:vim_tags

" 配置 ctags 的参数
let g:gutentags_ctags_extra_args = ['--fields=+niazS', '--extra=+q']
let g:gutentags_ctags_extra_args += ['--c++-kinds=+px']
let g:gutentags_ctags_extra_args += ['--c-kinds=+px']

" 检测 ~/.cache/tags 不存在就新建
if !isdirectory(s:vim_tags)
    silent! call mkdir(s:vim_tags, 'p')
endif

"end of guntentags config



"easymotion config
map <Leader> <Plug>(easymotion-prefix)
"end of easymotion confi



"NERD tree config
" 使用 NERDTree 插件查看工程文件。设置快捷键，速记：file list
nmap <Leader>fl :NERDTreeToggle<CR>
" 设置NERDTree子窗口宽度
let NERDTreeWinSize=32
" 设置NERDTree子窗口位置
let NERDTreeWinPos="left"
" 显示隐藏文件
let NERDTreeShowHidden=1
" NERDTree 子窗口中不显示冗余帮助信息
let NERDTreeMinimalUI=1
" 删除文件时自动删除文件对应 buffer
let NERDTreeAutoDeleteBuffer=1
"end of NERD tree config

"airline config
"airline
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tagbar#enabled = 0
let g:airline#extensions#tabline#left_sep = ' '
let g:airline#extensions#tabline#left_alt_sep = '|'
let g:airline_section_b='%{strftime("%T")}'

let g:airline#extensions#tabline#buffer_idx_mode = 1
nmap <leader>1 <Plug>AirlineSelectTab1
nmap <leader>2 <Plug>AirlineSelectTab2
nmap <leader>3 <Plug>AirlineSelectTab3
nmap <leader>4 <Plug>AirlineSelectTab4
nmap <leader>5 <Plug>AirlineSelectTab5
nmap <leader>6 <Plug>AirlineSelectTab6
nmap <leader>7 <Plug>AirlineSelectTab7
nmap <leader>8 <Plug>AirlineSelectTab8
nmap <leader>9 <Plug>AirlineSelectTab9

"airline scheme
let g:airline_theme='deus'
"end of airline config

"multiple cursors config
"let g:multi_cursor_use_default_mapping=0
"default mapping
let g:multi_cursor_next_key='<C-n>'
let g:multi_cursor_prev_key='<C-p>'
let g:multi_cursor_skip_key='<C-x>'
let g:multi_cursor_quit_key='<Esc>'
"end of mutiple cursors

"gundo tree config
"nnoremap <Leader>ud :GundoToggle<CR>
"let g:gundo_width = 60
"end of gundo tree config

"indentline
let g:indentLine_color_gui = '#A4E57E'


"nerd commenter config
" Add spaces after comment delimiters by default
let g:NERDSpaceDelims = 1

" Use compact syntax for prettified multi-line comments
let g:NERDCompactSexyComs = 1

" Align line-wise comment delimiters flush left instead of following code indentation
let g:NERDDefaultAlign = 'left'

" Set a language to use its alternate delimiters by default
let g:NERDAltDelims_java = 1

" Add your own custom formats or override the defaults
let g:NERDCustomDelimiters = { 'c': { 'left': '/**','right': '*/' } }

" Allow commenting and inverting empty lines (useful when commenting a region)
let g:NERDCommentEmptyLines = 1

" Enable trimming of trailing whitespace when uncommenting
let g:NERDTrimTrailingWhitespace = 1
"end of nerd commenter

"vim-cpp-enhanced-highlight
let g:cpp_class_scope_highlight = 1
let g:cpp_member_variable_highlight = 1
let g:cpp_class_decl_highlight = 1
let g:cpp_experimental_template_highlight = 1
let g:cpp_concepts_highlight = 1
"end of vim-cpp-enhanced-highlight


"end of plugin config
