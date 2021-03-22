local util = require("CONFIG.util")

util.O  ("hidden"         , true          )
util.O  ("termguicolors"  , true          )
util.O  ("hlsearch"       , true          )
util.O  ("incsearch"      , true          )
util.O  ("splitbelow"     , true          )
util.O  ("splitright"     , true          )
util.O  ("showmode"       , true          )
util.O  ("updatetime"     , 300           )
util.O  ("clipboard"      , "unnamedplus" )

util.W  ("number"         , true  )
util.W  ("relativenumber" , true  )
util.W  ("cursorline"     , true  )
util.W  ("wrap"           , false )
util.W  ("scrolloff"      , 8     )
util.WO ("sidescrolloff"  , 8     )
util.WO ("signcolumn"     , "yes" )

util.BO ("undofile"       , true)
util.BO ("tabstop"        , 4)
util.BO ("shiftwidth"     , 4)
