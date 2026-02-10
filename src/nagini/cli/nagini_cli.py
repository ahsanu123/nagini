from nagini.cli.nagini_cli_arg import NaginiCliArgsModel
import argparse


def cliMain():
    parser = argparse.ArgumentParser()
    parser.add_argument("credential", help="add your bearer credential", type=str)
    parser.add_argument("emitenCode", help="enter emiten code", type=str)

    argument = NaginiCliArgsModel.model_validate(vars(parser.parse_args()))

    print(argument)


if __name__ == "__main__":
    cliMain()
