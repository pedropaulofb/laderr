@echo off
echo Running RDF Converter...
python "convert_from_ttl_to_all_formats.py"
if %ERRORLEVEL% NEQ 0 (
    echo An error occurred while running the script.
    pause
    exit /b %ERRORLEVEL%
)
echo Conversion completed successfully!
pause
