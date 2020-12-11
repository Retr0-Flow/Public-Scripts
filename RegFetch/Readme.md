# RegFetch
RegFetch is a tool for quickly querying single, multiple, or all values that may exist in a registry key and output their data to your terminal.

## RegFetch.py
A script that queries all specified registry keys and returns their value data to the command line:
* Information returned can, and is recommended, to be redirected to a file.
* `CommonRegKeys.txt` - A text file containing the registry keys and values to be queried, this file is required for the tool to work.

## CommonRegKeys.txt
A text file containing all the registry keys that you want to be queried.
* Format: `[Registry Location],[Registry Key],[Registry Key Value]`
  * Example (without quotes): "HKEY_LOCAL_MACHINE,SYSTEM\ControlSet001\Control\Session Manager,BootExecute"
    * Will query:
      * Registry Location: `HKEY_LOCAL_MACHINE`
      * Registry Key: `SYSTEM\ControlSet001\Control\Session Manager`
      * Registry Key Value: `BootExecute`
      
### Each line must follow the format:
* `[Registry Location],[Registry Key],[Registry Key Value]`
  * Registry Location:
    * `HKEY_CLASSES_ROOT`
    * `HKEY_CURRENT_USER`
    * `HKEY_LOCAL_MACHINE`
    * `HKEY_USERS`
    * `HKEY_CURRENT_CONFIG`
      * One of those locations per line
  * Registry Key:
    * Example - `SYSTEM\ControlSet001\Control\Session Manager`
  * Registry Key Value:
    * `ALL`: Will query and return data for every value in a registry key.
    * `[Specified Value]`: Will return data for the specified registry key value.
      * Example: `BootExecute`
