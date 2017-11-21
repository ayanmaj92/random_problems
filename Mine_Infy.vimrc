"Display line numbers
syntax on
" set nu
if has("gui_running")
     " Basics {
         colorscheme morning " my color scheme (only works in GUI)
         set columns=200 " perfect size for me
         "set guifont=Consolas:h10 " My favorite font
         set guioptions=agimrtT 
         "              ||
         "              |+-- use simple dialogs rather than pop-ups
         "              +  use GUI tabs, not console style tabs
         set lines=55 " perfect size for me
         set mousehide " hide the mouse cursor when typing
     " }

 endif

" To show line numbers
" set number
" To provide auto indentation
set cindent     
" To highlight the searched word
set hlsearch
" To disable the line and column number
set ruler
" To disable the search in circular way
"set nowrapscan
" To conver tabs to spaces
set expandtab
" To perform search as you type
set incsearch
" To search case insensitive
set ignorecase
"To get colors on solaris
set term=xtermc
" To set proper contrast between background and foreground
set background=light
" Specifies number of spaces that a tab counts for.
set tabstop=4
" Specifies number of spaces to use for each step of indentation
set shiftwidth=4
" To restrict the line width to 80 columns
"set columns=80
" While using diff in vim change of spaces will not be shown as difference
set diffopt=iwhite
" Default file format will be unix
set fileformat=unix
" Minibuffer 
" Path of the tags file
"set tags=/software/src/marlin/SIPSG
" To highlight the keywords etc.
syntax on
set backspace=indent,eol,start
set tags=$SOURCE/marlin/tags,./tags,/software/src/marlin/tags,~/tags
set mouse-=a
if has("cscope")
    if filereadable("/software/src/marlin/cscope.out")
         set mouse=a
         cs add /software/src/marlin/cscope.out
    " else add database pointed to by environment
    elseif $CSCOPE_DB != ""
        cs add $CSCOPE_DB
    endif
"    set csverb
endif
" colorscheme evening " my color scheme (only works in GUI)
" colorscheme  koehler " my color scheme (only works in GUI)
colorscheme  elflord " my color scheme (only works in GUI)

nmap <F2> :scs find s <C-R>=expand("<cword>")<CR><CR>
"nmap <F3> :scs find g <C-R>=expand("<cword>")<CR><CR>
nmap <F3> :Search .CC   : CC FSM : 
nmap <F4> :Search _VCON 
"nmap <F4> :scs find c <C-R>=expand("<cword>")<CR><CR>
"nmap <F5> :scs find t <C-R>=expand("<cword>")<CR><CR>
"nmap <F6> :scs find e <C-R>=expand("<cword>")<CR><CR>
"nmap <F7> :scs find f <C-R>=expand("<cfile>")<CR><CR>
""nmap <F8> :scs find i ^<C-R>=expand("<cfile>")<CR>$<CR>
""nmap <F9> :scs find d <C-R>=expand("<cword>")<CR><CR>
nmap <F11> :Search <C-R>=expand("<cword>")<CR><CR>
nmap <F12> :SearchReset <CR><CR>
map <S-Insert> <MiddleMouse>
map! <S-Insert> <MiddleMouse>

let g:MultipleSearchColorSequence = "blue,green,magenta,cyan,gray,brown,red,yellow,black,black,black,black,black,black,black,black,red,yellow,blue,green,magenta,cyan,gray,brown,red,yellow,blue,green,magenta,cyan,gray,brown,red,yellow,blue,green,magenta,cyan,gray,brown,red,yellow,blue,green,magenta,cyan,gray,brown,red,yellow,blue,green,magenta,cyan,gray,brown"

let g:MultipleSearchTextColorSequence = "white,black,white,black,black,black,black,black,red,yellow,blue,green,magenta,cyan,gray,brown,black,white,white,black,white,black,white,black,black,white,white,black,white,black,white,black,black,white,white,black,white,black,white,black,black,white,white,black,white,black,white,black,black,white"

"source ~/.vimrc1

set number
