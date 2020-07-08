-- ./company.dhall

let Prelude =
      https://prelude.dhall-lang.org/v11.1.0/package.dhall sha256:99462c205117931c0919f155a6046aec140c70fb8876d208c7c77027ab19c2fa


let Author = { name : Text, email : Text }

let authors
    : List Author
    = [ { name = "Chris Schnaufer", email = "schnaufer@arizona.edu" }
      , { name = "Ken Youens-Clark", email = "kyclark@arizona.edu" }
      ]

in  { authors = authors
    , version = "1.0"
    , write_betydb_csv = True
    }

