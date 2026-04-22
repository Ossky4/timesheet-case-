# Local imports
from timesheet import command_line_interface_functions  # cli functions


def main():

    # Build interface
    parser = command_line_interface_functions.build_command_line_interface()

    # Parse arguments
    args = command_line_interface_functions.parse_command_line_arguments(
        parser, run_actions=False
    )

    # Run actions
    command_line_interface_functions.run_cli_actions(args)


if __name__ == "__main__":
    main()
