Vimeval
=======

Vimeval cals sum on visually selected numbers in vim.

Install
-------

Vim must be compiled with ``+python`` support.

If using https://github.com/junegunn/vim-plug add the following to
`.vimrc`.

    Plug 'https://github.com/delijati/vimeval.git'

Usage
-----

1. Select row in visual mode.
2. Call `CalSum` e.g. : ``:'<, '>CalcSum``
