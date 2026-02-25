import argparse 
from argparse import Namespace


def run_cli() -> Namespace:
    """
    Builds and parses CLI arguments and returns the parsed Namespace.
    """
    print("step3: CLI")
    #Create Parser
    parser = argparse.ArgumentParser(description="Track your expenses!")

    # Create subparser
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Create subcommands
    add_parser = subparsers.add_parser("add")
    update_parser = subparsers.add_parser("update")
    delete_parser = subparsers.add_parser("delete")
    list_parser = subparsers.add_parser("list")
    summary_parser = subparsers.add_parser("summary")

    # Create arguments for the "add" subcommand
    add_parser.add_argument("--description", required=True)
    add_parser.add_argument("--amount", type=int, required=True)

    # Create arguments for the "update" subcommand
    update_parser.add_argument("--id", type=int, required=True)
    update_parser.add_argument("--description", type=str, required=True)
    update_parser.add_argument("--amount", type=int, required=True)

    # Create arguments for the "delete" subcommand
    delete_parser.add_argument("--id", type=int, required=True)

    # Create arguments for the "summary" subcommand
    summary_parser.add_argument("--month", type=int, choices=range(1,13))

    # Read and validate what the user wrote in the terminal
    args = parser.parse_args()

    
    return args 



   



