def format_linter_error(error: dict) -> dict:
    return {
        'code': error['code'],
        'line': error['line_number'],
        'column': error['column_number'],
        'text': error['text'],
    }



def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        'file': file_path,
        'errors': [format_linter_error(error) for error in errors],
    }



def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file_path, errors)
        for file_path, errors in linter_report.items()
        if errors
    ]

