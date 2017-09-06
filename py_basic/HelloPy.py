#from nester import print_lol
import nester

movies = [
    "The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
    [
        "Graham Chapman",
        [
            "Michael Palin", "Jon Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones",
            "Robert Deniro",
            [
                "Intern", "Heat", "God Father"
            ]
        ]
    ]
]

nester.print_lol(movies, True, 2)