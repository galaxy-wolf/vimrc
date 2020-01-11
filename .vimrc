" BASIC SETUP:
"
" " enter the current millenium
set nocompatible

" enable syntax and plugins (for netrw)
syntax enable
filetype plugin on

" Search down into subfolers
" Provides tab-completion for all file-ralated tasks
set path+=**

" Display all matching files whe we tab complete
set wildmenu

" Tweaks for browsing
let g:netrw_banner=0		" disable annoying banner
let g:netrw_browse_split=4	" open in prior window
let g:netrw_altv=1		" open splits to the right
let g:netrw_liststype=3		" tree view
let g:netrw_list_hide=netrw_gitignore#Hide()
let g:netrw_list_hide.=',\(&\|\s\s\)zs\.\S+'


" chinese encoding
set encoding=utf8
set fileencodings=ucs-bom,utf8,utf16,gbk,big5,gb18030,latin1

let mapleader=","
map <silent> <leader>ss :so ~/.vimrc<cr>
map <silent> <leader>ee :e ~/.vimrc<cr>
autocmd! bufwritepost .vimrc so ~/.vimrc

" font
set guifont=consolas:h12
set nu

" tabs
set tabstop=3
set shiftwidth=3
set expandtab

"back up
set backup
set backupext=.bak~
set backupdir=~/Backup/
set backupskip=~/Backup/

"swap dir
set dir=~/Backup/

