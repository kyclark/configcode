-- ./company.dhall

let Prelude =
      https://prelude.dhall-lang.org/v11.1.0/package.dhall sha256:99462c205117931c0919f155a6046aec140c70fb8876d208c7c77027ab19c2fa


let Author = { name : Text, email : Text }

let authors
    : List Author
    = [ { name = "Chris Schnaufer", email = "schnaufer@arizona.edu" }
      , { name = "Ken Youens-Clark", email = "kyclark@arizona.edu" }
      ]

let contributors
    : List Text
    = [ "Jacob van der Leeuw" ]

let Variable = { name : Text, unit : Text, label: Text }
let variables
    : List Variable
    = [ { name = "excess greenness index"
        , unit = "[-510:510]"
        , label = "excess_greenness_index" 
        }
      , { name = "green leaf index"
        , unit = "[-1:1]"
        , label = "green_leaf_index" 
        }
      ]

in  { authors = authors
    , contributors = contributors
    , version = "1.0"
    , citation = 
        { author = "Clairessa Brown"
        , title = "Woebbecke, D.M. et al"
        , year = 2020
        }
    , variables = variables
    , write_betydb_csv = True
    , write_geostreams_csv = False
    }

