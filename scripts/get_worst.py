from report import Report
import click


@click.command()
@click.option(
    "--input",
    "-i",
    required=True,
    type=click.Path(exists=True, dir_okay=False),
    help="sta report",
)
def main(input):
    report = Report(input)

    max_vio = 0.00
    for path in report.paths:
        if path.slack < 0:
            max_vio = min(max_vio, path.slack)

    print(max_vio)

if __name__ == "__main__":
    main()
