if has('python3')
    command! -nargs=1 Python python3 <args>
elseif has('python')
    command! -nargs=1 Python python <args>
else
    echo "Error: Requires Vim compiled with +python or +python3"
    finish
endif

fun! CalcSum()
Python << EOF
if 'vimeval' not in sys.modules:
    import vimeval
else:
    import imp
    # Reload python module to avoid errors when updating plugin
    vimeval = imp.reload(vimeval)
    print(vimeval.sum_range())
EOF
endfun

" init load script parent path :h:h
execute "Python import sys"
execute "Python sys.path.append(r'" . expand("<sfile>:p:h:h") . "')"

" register command
command! -range -register CalcSum call CalcSum()
