# Load packages
import unittest  # running tests
from pathlib import Path  # handling file paths
from unittest.mock import MagicMock, patch

# Local imports
from timesheet import command_line_interface_functions  # cli functions


class TestCommandLineInterfaceFunctions(unittest.TestCase):
    def test_build_command_line_interface(self):
        """Test command line parser is built"""

        # Build the command line interface parser
        parser = command_line_interface_functions.build_command_line_interface()

        # Check argument parser returned
        self.assertEqual(
            str(type(parser)),
            "<class 'argparse.ArgumentParser'>",
            "Check argument parser returned",
        )

    @patch("timesheet.command_line_interface_functions.run_cli_actions")
    def test_parse_command_line_arguments_parse_only(self, mock_run_cli_actions):
        """Test parse_command_line_arguments can behave as pure parse."""

        # Build the command line interface parser
        parser = command_line_interface_functions.build_command_line_interface()

        # Define the command line arguments and parse
        start_time = "09:00"
        end_time = "11:45"
        timesheet_file = Path("outputs/test_timesheet.csv")
        arguments = [
            "--file",
            str(timesheet_file),
            "--start",
            start_time,
            "--end",
            end_time,
        ]
        args = command_line_interface_functions.parse_command_line_arguments(
            parser, arguments, run_actions=False
        )

        # Check parser output
        self.assertEqual(args.file, str(timesheet_file), "Check file argument parsed")
        self.assertFalse(args.reset, "Check reset defaults to False")
        self.assertEqual(args.start, start_time, "Check start argument parsed")
        self.assertEqual(args.end, end_time, "Check end argument parsed")

        # Check no orchestration happens when explicitly disabled
        mock_run_cli_actions.assert_not_called()

    @patch("timesheet.command_line_interface_functions.timesheet.Timesheet")
    def test_run_cli_actions_orchestrates_timesheet_calls(self, mock_timesheet_class):
        """Test run_cli_actions orchestrates actions around Timesheet."""

        # Define arguments and mock timesheet
        args = MagicMock(
            file="outputs/test_timesheet.csv",
            reset=True,
            start="09:00",
            end="11:45",
        )
        mock_timesheet = MagicMock()
        mock_timesheet_class.return_value = mock_timesheet

        # Run orchestration
        command_line_interface_functions.run_cli_actions(args)

        # Check timesheet construction and action fan-out
        mock_timesheet_class.assert_called_once_with(file_name=Path(args.file))
        mock_timesheet.reset_timesheet.assert_called_once_with()
        mock_timesheet.add_start_time.assert_called_once_with(
            start_time_string=args.start
        )
        mock_timesheet.add_end_time.assert_called_once_with(end_time_string=args.end)

    @patch("timesheet.command_line_interface_functions.timesheet.Timesheet")
    def test_run_cli_actions_skips_non_requested_actions(self, mock_timesheet_class):
        """Test run_cli_actions does not execute optional actions when absent."""

        # Define arguments without optional actions
        args = MagicMock(
            file="outputs/test_timesheet.csv",
            reset=False,
            start=None,
            end=None,
        )
        mock_timesheet = MagicMock()
        mock_timesheet_class.return_value = mock_timesheet

        # Run orchestration
        command_line_interface_functions.run_cli_actions(args)

        # Check no optional methods are called
        mock_timesheet.reset_timesheet.assert_not_called()
        mock_timesheet.add_start_time.assert_not_called()
        mock_timesheet.add_end_time.assert_not_called()


if __name__ == "__main__":
    unittest.main()
