This is a presentation I did back in 2016. I've included the PPTx file, sample JSON files, and a partial JSON file that needs "fixing" to render properly (as well as a copy of the solution for that file). It's indispensible for a digital forensic examiner to understand JSON files. If you recover a partial JSON file, it will not decode properly. But you can manually decipher its content. You are also able to "fix" a partial JSON file so that it can be decoded properly for you rather than having to manually parse through it.


Since this presentation, SQLite has added support to query JSON data within a field. This negates the need to parse such a field manually with the help of string. Whereas back in 2016, not all SQLite browsing tool had this support. For example, DB Browser did not at the time, but the one demonstrated in the presentation did support it. The SQLite syntax to parse JSON in DB Browser for SQLite is the same as what was shown in this 2016 presentation.

For more info on SQLite functions and operators available to handle JSON data, see https://www.sqlite.org/json1.html.

