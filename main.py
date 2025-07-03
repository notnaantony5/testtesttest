list(
    map(
        lambda a: open("result_names.txt", "a", encoding="utf-8").write(a + "\n"),
        map(
            lambda x: x.split(" ")[0] + " " + x.split(" ")[1][0] + ".",
            filter(
                lambda x: x.split(" ")[1].startswith("А"),
                open("names.txt", "r", encoding="utf-8"),
            ),
        ),
    )
)
